import numpy as np
import pandas as pd
import os

# Load dataset
csv_file = "dataset/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
output_file = "cleaned_data/cleaned_dataset.csv"

# Load CSV
df = pd.read_csv(csv_file)

# Drop rows with NaN or Infinity
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Drop non-numeric and unneeded columns
drop_cols = ['Flow ID', 'Source IP', 'Destination IP', 'Timestamp', 'Label']
X = df.drop(columns=drop_cols, errors='ignore')

# Save cleaned data
os.makedirs("cleaned_data", exist_ok=True)
X.to_csv(output_file, index=False)

print(f"✅ Cleaned data saved to: {output_file}")
