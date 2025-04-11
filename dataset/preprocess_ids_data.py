import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load original dataset (CSV or similar)
df = pd.read_csv("dataset/your_dataset.csv")  # Update path accordingly

# Separate features and labels
X = df.drop(columns=['Label'])  # Or whatever your label column is named
y = df['Label']

# Save feature names before converting to numpy
feature_names = X.columns.to_numpy()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save as .npz (including feature_names)
np.savez("preprocessed_ids_data.npz",
         X_train=X_train.to_numpy(),
         X_test=X_test.to_numpy(),
         y_train=y_train.to_numpy(),
         y_test=y_test.to_numpy(),
         feature_names=feature_names)
