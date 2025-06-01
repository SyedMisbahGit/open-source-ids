SURICATA_CONFIG = {
    # Database configuration
    'DATABASE_URL': 'sqlite:///ids_data.db',
    'DATABASE_TYPE': 'sqlite',
    
    # Logging configuration
    'LOG_PATH': '/var/log/suricata/eve.json',
    'LOG_LEVEL': 'info',
    
    # Rule configuration
    'RULES_DIR': '/etc/suricata/rules',
    'RULES_URL': 'https://rules.emergingthreatspro.com/rules/emerging.rules.tar.gz',
    'RULES_UPDATE_INTERVAL': 24,  # hours
    
    # Network configuration
    'INTERFACE': 'eth0',
    'BPF_FILTER': 'not port 22',  # Exclude SSH traffic
    
    # Performance settings
    'MAX_PACKETS': 10000,
    'MAX_EVENTS': 1000,
    'MAX_ALERTS': 100,
    
    # Alert configuration
    'ALERT_THRESHOLD': 5,  # alerts per second
    'ALERT_TIMEOUT': 300,  # seconds
    
    # Anomaly detection
    'ANOMALY_THRESHOLD': 3.0,
    'ANOMALY_WINDOW': 60,  # seconds
    
    # Host-based IDS
    'HOST_RULES_DIR': '/etc/ids/host_rules',
    'HOST_LOG_PATH': '/var/log/ids/host_events.log',
    
    # API configuration
    'API_HOST': '0.0.0.0',
    'API_PORT': 5000,
    'API_DEBUG': True,
    
    # Security
    'SECRET_KEY': 'your-secret-key-here',  # Change in production
    'JWT_SECRET_KEY': 'your-jwt-secret-key-here',  # Change in production
    
    # Metrics
    'METRICS_PORT': 9090,
    'METRICS_PATH': '/metrics',
    
    # External integrations
    'ELASTICSEARCH_HOST': 'localhost',
    'ELASTICSEARCH_PORT': 9200,
    'KAFKA_HOST': 'localhost',
    'KAFKA_PORT': 9092,
    
    # Monitoring
    'PROMETHEUS_HOST': 'localhost',
    'PROMETHEUS_PORT': 9090,
    'GRAFANA_HOST': 'localhost',
    'GRAFANA_PORT': 3000
}
