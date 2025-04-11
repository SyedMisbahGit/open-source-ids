import numpy as np
import pickle
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Load preprocessed data from .npz
data = np.load("preprocessed_ids_data.npz", allow_pickle=True)
X_train = data["X_train"]
X_test = data["X_test"]
y_train = data["y_train"]
y_test = data["y_test"]
feature_names = data["feature_names"]

# Save feature names used during training
with open("dataset/feature_names.pkl", "wb") as f:
    pickle.dump(feature_names.tolist(), f)

# Convert y to one-hot encoding
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaler
with open("dataset/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Build the model
model = Sequential([
    Dense(128, input_dim=X_train_scaled.shape[1], activation='relu'),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(y_train_cat.shape[1], activation='softmax')
])

# Compile and train
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_scaled, y_train_cat, epochs=5, batch_size=32, validation_split=0.1)

# Save the trained model
model.save("dataset/abids_model.h5")

# Evaluate on test set
print("✅ Model trained and saved as 'abids_model.h5'")
loss, accuracy = model.evaluate(X_test_scaled, y_test_cat)
print(f"📊 Test Accuracy: {accuracy * 100:.2f}%")
