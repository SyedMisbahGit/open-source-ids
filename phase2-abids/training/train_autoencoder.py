# train_autoencoder.py

import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import regularizers
from tensorflow.keras.models import load_model
from joblib import dump

# Paths
CLEANED_DATA_PATH = "../cleaned_data/cleaned_dataset.csv"
MODEL_PATH = "../models/autoencoder_model.h5"
SCALER_PATH = "../models/minmax_scaler.pkl"

# Create models directory if not exists
os.makedirs("../models", exist_ok=True)

# 1. Load cleaned dataset
df = pd.read_csv(CLEANED_DATA_PATH)

# 2. Drop the label column if exists
if "Label" in df.columns:
    df.drop("Label", axis=1, inplace=True)

# 3. Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df)

# Save the scaler
dump(scaler, open(SCALER_PATH, "wb"))

# 4. Autoencoder architecture
input_dim = X_scaled.shape[1]
encoding_dim = 14

input_layer = Input(shape=(input_dim,))
encoder = Dense(encoding_dim, activation="relu", activity_regularizer=regularizers.l1(1e-5))(input_layer)
encoder = Dense(7, activation="relu")(encoder)
decoder = Dense(7, activation="relu")(encoder)
decoder = Dense(input_dim, activation="sigmoid")(decoder)

autoencoder = Model(inputs=input_layer, outputs=decoder)
autoencoder.compile(optimizer="adam", loss="mean_squared_error")

# 5. Train the model
autoencoder.fit(
    X_scaled, X_scaled,
    epochs=20,
    batch_size=64,
    shuffle=True,
    validation_split=0.2,
    verbose=1
)

# 6. Save the trained model
autoencoder.save(MODEL_PATH)
print(f"\n✅ Autoencoder model saved to: {MODEL_PATH}")
print(f"✅ Scaler saved to: {SCALER_PATH}")
