import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Cargar los datos
data = pd.read_excel("dataset_anomalias.xlsx")

# Normalizar nombres de columnas
data.columns = data.columns.str.lower()

# Variables predictoras (X) y variable objetivo (y)
X = data[['realvalue', 'units', 'pointindex', 'axis']]  # Variables predictoras
y = data['anomaly']  # Variable objetivo

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

# Guardar el modelo entrenado
joblib.dump(model, "model_anomalias.joblib")

print("Modelo entrenado y guardado como 'model.joblib'.")
