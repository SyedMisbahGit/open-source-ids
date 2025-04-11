import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pickle
import os

# Define paths
MODEL_PATH = "dataset/abids_model.h5"
SCALER_PATH = "dataset/scaler.pkl"
DATA_PATH = "dataset/portscan.csv"
OUTPUT_PATH = "dataset/predictions_output.csv"
ERRORS_PATH = "dataset/mismatches.csv"

# Load model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at: {MODEL_PATH}")
model = load_model(MODEL_PATH)

# Load scaler
if not os.path.exists(SCALER_PATH):
    raise FileNotFoundError(f"Scaler not found at: {SCALER_PATH}")
with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

# Load CSV data
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Data file not found at: {DATA_PATH}")
df = pd.read_csv(DATA_PATH)

# Handle label column
y_true = None
if 'Label' in df.columns:
    y_true = df['Label']
    df = df.drop(columns=['Label'])

# Drop non-numeric columns if any
df = df.select_dtypes(include=[np.number])

# Replace inf/-inf with NaN, then fill NaNs with 0
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(0, inplace=True)

# Scale features
try:
    X = scaler.transform(df)
except Exception as e:
    raise ValueError(f"Error scaling input features: {e}")

# Predict
preds = model.predict(X)
predicted_classes = np.argmax(preds, axis=1)
confidences = np.max(preds, axis=1)

# Map numeric predictions to class names
label_map = {0: 'BENIGN', 1: 'ATTACK'}
labels = [label_map.get(cls, "UNKNOWN") for cls in predicted_classes]

# Show top 10 predictions
print("\n🔍 Top 10 Predictions:")
for i in range(min(10, len(labels))):
    print(f"Sample {i+1}: Predicted = {labels[i]}, Confidence = {confidences[i]:.4f}")

# Save predictions to CSV
df_output = df.copy()
df_output['Predicted_Class'] = labels
df_output['Confidence'] = confidences

# Add true labels if available
if y_true is not None:
    df_output['True_Label'] = y_true
    # Calculate accuracy
    # Convert string labels to 0/1 if needed
    y_true_encoded = y_true.map({'BENIGN': 0, 'ATTACK': 1}).fillna(-1).astype(int)
    correct_preds = predicted_classes == y_true_encoded
    accuracy = np.sum(correct_preds) / len(y_true_encoded)
    print(f"\n✅ Accuracy on this CSV file: {accuracy * 100:.2f}%")

    # Save mismatches
    mismatches = df_output[~correct_preds]
    mismatches.to_csv(ERRORS_PATH, index=False)
    print(f"❌ Mismatches saved to: {ERRORS_PATH}")

# Save all predictions
df_output.to_csv(OUTPUT_PATH, index=False)
print(f"\n📁 Predictions saved to: {OUTPUT_PATH}")
