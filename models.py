from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import date

# Inicializa SQLAlchemy aquí
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    rut = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    images = db.relationship('Image', backref='user', lazy=True)
    excel_files = db.relationship('ExcelFile', backref='user', lazy=True)  # Relación con ExcelFile
    _is_active = db.Column(db.Boolean, default=True, nullable=False)  # Campo interno

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ExcelFile(db.Model):
    __tablename__ = 'excel_file'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    classification = db.Column(db.String(50), nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Default añadido
    graphs = db.relationship('Graph', backref='excel_file', lazy=True)  # Relación con Graph

    def __repr__(self):
        return f'<ExcelFile {self.filename} uploaded by {self.uploaded_by}>'

class Graph(db.Model):
    __tablename__ = 'graph'
    id = db.Column(db.Integer, primary_key=True)
    graph_path = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Categoría: Aceleración, Velocidad o Envolvente
    excel_file_id = db.Column(db.Integer, db.ForeignKey('excel_file.id'), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    start_date = db.Column(db.Date, nullable=False, server_default=str(date.today()))  # Fecha inicial del período trabajado
    end_date = db.Column(db.Date, nullable=False, server_default=str(date.today()))    # Fecha final del período trabajado

    def __repr__(self):
        return f'<Graph {self.category} at {self.graph_path}>'

class SupportMessage(db.Model):
    __tablename__ = 'support_message'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<SupportMessage {self.email}>'
