import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Simular un conjunto de datos para entrenamiento
data = pd.DataFrame({
    'realvalue': [0.1, 0.5, 1.0, 1.5],
    'label': [0, 1, 1, 0]
})

X = data[['realvalue']]
y = data['label']

# Entrenar el modelo
model = RandomForestClassifier()
model.fit(X, y)

# Guardar el modelo entrenado
joblib.dump(model, "model.joblib")

