import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import os

# Paths
cleaned_data_path = '../cleaned_data/cleaned_dataset.csv'
model_path = '../models/autoencoder_model.h5'
output_path = '../evaluation/anomaly_results.csv'

# Load data
print("🔄 Loading cleaned dataset...")
df = pd.read_csv(cleaned_data_path)

# Drop non-numeric or categorical features
df_numeric = df.select_dtypes(include=[np.number])
print(f"✅ Dataset shape (numeric only): {df_numeric.shape}")

# Scale data
print("🔧 Scaling data...")
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df_numeric)

# Load trained model
print("📦 Loading trained autoencoder model...")
autoencoder = load_model(model_path)

# Reconstruct inputs and compute reconstruction error
print("🧠 Performing inference & calculating reconstruction errors...")
X_pred = autoencoder.predict(X_scaled)
reconstruction_error = np.mean(np.square(X_scaled - X_pred), axis=1)

# Set threshold (you can make this dynamic later)
threshold = np.percentile(reconstruction_error, 95)
print(f"⚙️ Threshold (95th percentile): {threshold}")

# Detect anomalies
anomalies = reconstruction_error > threshold
df_results = df.copy()
df_results['reconstruction_error'] = reconstruction_error
df_results['is_anomaly'] = anomalies.astype(int)

# Save results
os.makedirs('../evaluation', exist_ok=True)
df_results.to_csv(output_path, index=False)
print(f"✅ Anomaly results saved to: {output_path}")
