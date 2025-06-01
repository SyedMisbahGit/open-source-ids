from typing import List, Dict, Optional
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import load_model
import logging
from pathlib import Path
from datetime import datetime

class AnomalyIDS:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.model_path = Path('models/autoencoder/model.h5')
        self.scaler = StandardScaler()
        self.model = self._load_model()
        self.threshold = 3.0  # Default threshold for anomaly detection

    def _load_model(self) -> Optional[tf.keras.Model]:
        """Load the trained autoencoder model"""
        try:
            if not self.model_path.exists():
                self.logger.warning(f"Model not found at {self.model_path}")
                return None
            
            model = load_model(self.model_path)
            self.logger.info("Autoencoder model loaded successfully")
            return model
        except Exception as e:
            self.logger.error(f"Error loading model: {str(e)}")
            return None

    def _preprocess_data(self, data: pd.DataFrame) -> np.ndarray:
        """Preprocess network traffic data for the model"""
        try:
            # Select relevant features (example features)
            features = ['duration', 'protocol_type', 'service', 'flag',
                       'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
                       'urgent', 'hot', 'num_failed_logins', 'logged_in',
                       'num_compromised', 'root_shell', 'su_attempted',
                       'num_root', 'num_file_creations', 'num_shells',
                       'num_access_files', 'num_outbound_cmds',
                       'is_host_login', 'is_guest_login']
            
            # Convert categorical features to numeric
            data = pd.get_dummies(data, columns=['protocol_type', 'service', 'flag'])
            
            # Select and scale features
            X = data[features].values
            X_scaled = self.scaler.fit_transform(X)
            return X_scaled
        except Exception as e:
            self.logger.error(f"Error preprocessing data: {str(e)}")
            return np.array([])

    def detect_anomalies(self, data: pd.DataFrame) -> List[Dict]:
        """Detect anomalies in network traffic data"""
        if self.model is None:
            self.logger.warning("Model not loaded")
            return []

        try:
            # Preprocess data
            X_scaled = self._preprocess_data(data)
            if X_scaled.size == 0:
                return []

            # Get reconstruction error
            predictions = self.model.predict(X_scaled)
            reconstruction_error = np.mean(np.square(X_scaled - predictions), axis=1)

            # Identify anomalies
            anomalies = []
            for i, error in enumerate(reconstruction_error):
                if error > self.threshold:
                    anomalies.append({
                        'timestamp': datetime.now().isoformat(),
                        'reconstruction_error': float(error),
                        'category': 'Anomaly',
                        'signature': 'Autoencoder Detection',
                        'severity': 4,  # Higher severity for anomalies
                        'details': data.iloc[i].to_dict()
                    })

            return anomalies

        except Exception as e:
            self.logger.error(f"Error detecting anomalies: {str(e)}")
            return []

    def get_recent_alerts(self, limit: int = 100) -> List[Dict]:
        """Get recent anomaly alerts"""
        # In a real implementation, this would fetch from a database
        return []

    def get_model_count(self) -> int:
        """Get number of trained models"""
        return 1 if self.model is not None else 0

    def get_model_metrics(self) -> Dict:
        """Get model performance metrics"""
        if self.model is None:
            return {}
        
        return {
            'threshold': self.threshold,
            'status': 'active' if self.model is not None else 'inactive',
            'last_update': datetime.now().isoformat()
        }
