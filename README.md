# Open-Source IDS/XDR Project

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/github/workflow/status/SyedMisbahGit/open-source-ids/CI)](https://github.com/SyedMisbahGit/open-source-ids/actions)

An open-source, scalable Intrusion Detection System (IDS) that evolves into a full Extended Detection & Response (XDR) system. This project combines rule-based, anomaly-based, and host-based detection under a unified dashboard using modern Python and open-source tools.

## 🚀 Features

- 🛡️ **Signature-based IDS (S-IDS)**
  - Real-time network traffic inspection
  - Suricata NIDS integration
  - Rule-based threat detection
  - Custom signature management

- 🧠 **Anomaly-based IDS (A-IDS)**
  - Deep learning autoencoder for anomaly detection
  - CIC-IDS 2017 dataset integration
  - Real-time traffic analysis
  - Anomaly scoring and thresholding

- 🛡️ **Host-based IDS (H-IDS)**
  - Host-level threat detection
  - System event monitoring
  - File integrity checking
  - Process monitoring

- 📊 **Unified Dashboard**
  - Real-time traffic visualization
  - Alert correlation
  - Threat intelligence integration
  - Advanced filtering and search

## 📦 Technology Stack

- **Backend**
  - Python 3.10+
  - Flask
  - SQLAlchemy
  - Redis (optional)
  - Elasticsearch (optional)

- **Frontend**
  - HTML5/CSS3
  - JavaScript
  - Bootstrap
  - Chart.js

- **Machine Learning**
  - TensorFlow
  - Scikit-learn
  - Autoencoder model

- **Security**
  - JWT authentication
  - bcrypt password hashing
  - CSRF protection
  - Rate limiting

## 🛠️ Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.8+
- Git

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/SyedMisbahGit/open-source-ids.git
cd open-source-ids
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy environment file and configure:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize database (if using SQLAlchemy):
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Start the application:
```bash
flask run
```

### Development Setup

1. Install development dependencies:
```bash
pip install -e .[dev]
```

2. Run tests:
```bash
pytest
```

3. Run linters:
```bash
flake8 src/
black src/
mypy src/
```

4. Generate documentation:
```bash
make docs
```

## 📂 Project Structure

```
open-source-ids/
├── src/                     # Source code directory
│   ├── core/               # Core IDS components
│   │   ├── signature/      # Signature-based IDS
│   │   ├── anomaly/        # Anomaly-based IDS
│   │   └── host/           # Host-based IDS
│   ├── config/             # Configuration files
│   │   └── suricata/      # Suricata configuration
│   ├── models/             # Database models
│   │   ├── base.py        # Base model
│   │   └── alert.py       # Alert model
│   ├── templates/          # Flask templates
│   │   └── dashboard/     # Main dashboard templates
│   └── static/             # Static assets
│       ├── css/           # Stylesheets
│       └── js/            # JavaScript
├── data/                   # Data storage
│   ├── raw/               # Raw network data
│   └── processed/         # Processed data
├── logs/                   # Log files
│   ├── suricata/          # Suricata logs
│   └── app/              # Application logs
├── requirements.txt        # Python dependencies
├── Makefile               # Build automation
└── README.md              # Documentation
```

## 📚 Documentation

- [API Documentation](docs/api.md)
- [Configuration Guide](docs/config.md)
- [Deployment Guide](docs/deployment.md)
- [Troubleshooting](docs/troubleshooting.md)

## 📊 Database Schema

The project uses SQLAlchemy ORM with the following entities:

```sql
-- Alerts Table
CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    source_ip VARCHAR(15) NOT NULL,
    dest_ip VARCHAR(15) NOT NULL,
    source_port INTEGER,
    dest_port INTEGER,
    protocol VARCHAR(10),
    category VARCHAR(50),
    signature VARCHAR(255),
    severity INTEGER,
    additional_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Signatures Table
CREATE TABLE signatures (
    id SERIAL PRIMARY KEY,
    signature_id VARCHAR(50) UNIQUE,
    category VARCHAR(50),
    severity INTEGER,
    description TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Host Events Table
CREATE TABLE host_events (
    id SERIAL PRIMARY KEY,
    host_id VARCHAR(50),
    event_type VARCHAR(50),
    event_data JSONB,
    timestamp TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 📈 Performance

- Real-time processing
- Efficient memory usage
- Scalable architecture
- Caching support

## 🛡️ Security

- JWT authentication
- Role-based access control
- Secure password hashing
- Rate limiting
- CSRF protection

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the Suricata community
- Thanks to the TensorFlow team
- Thanks to all contributors

## 📞 Support

For support, email [your-email@example.com](mailto:your-email@example.com) or create an issue in the repository.

---

## 📌 Project Overview

| Phase | Component                         | Description |
|-------|-----------------------------------|-------------|
| 1     | Signature-Based IDS               | Suricata NIDS + Flask Dashboard to parse and visualize Suricata alerts (eve.json). |
| 2     | Anomaly-Based IDS (ABIDS)         | Deep learning autoencoder model trained on CIC-IDS 2017 to detect anomalous traffic. |
| 3     | Merged Dashboard                  | Unified Flask-based dashboard to display alerts from Suricata and the ABIDS module. |
| 4     | Host-Based IDS (HIDS)             | Integrate a lightweight host agent (like OSSEC or Wazuh). |
| 5     | Threat Intelligence + Correlation | Fuse alerts from different modules with enrichment, deduplication, and correlation. |

---

## 🚀 Phase 1: Signature-Based IDS

- **Tool Used**: Suricata
- **Features**:
  - Real-time network traffic inspection
  - Alert generation based on rule signatures
- **Dashboard**: Flask app parses Suricata's `eve.json` and displays filtered alerts.

### ✅ Completed:
- [x] Suricata installed and configured
- [x] eve.json parsing setup
- [x] Flask dashboard to view alerts

---

## 🧠 Phase 2: Anomaly-Based IDS (ABIDS)

- **Tool Used**: Autoencoder (Keras/TensorFlow)
- **Dataset**: CIC-IDS 2017
- **Pipeline**:
  1. Preprocess and clean dataset
  2. Train autoencoder on benign samples
  3. Evaluate reconstruction error on unseen data
  4. Store anomaly scores in `anomaly_results.csv`

### ✅ Completed:
- [x] Autoencoder training script

---

## 📊 Phase 3: Unified Dashboard (Work In Progress)

- Merge Phase 1 (Suricata alerts) and Phase 2 (ABIDS alerts) into a single dashboard
- Use tabs or filters to switch between:
  - Signature Alerts
  - Anomaly Alerts
  - Correlated Alerts (future)

### 🔧 To Do:
- [ ] Flask blueprint restructuring
- [ ] Combined HTML templates
- [ ] Integrate Suricata + ABIDS data sources
- [ ] Add filters (IP, time, label, etc.)

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.10 or higher
- PostgreSQL (optional, for production)
- Redis (optional, for caching)
- Elasticsearch (optional, for advanced search)
- Kafka (optional, for distributed logging)

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/SyedMisbahGit/open-source-ids.git
cd open-source-ids
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy environment file and configure:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize database (if using SQLAlchemy):
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Start the application:
```bash
flask run
```

### Development Setup

1. Install development dependencies:
```bash
pip install -e .[dev]
```

2. Run tests:
```bash
pytest
```

3. Run linters:
```bash
flake8 src/
black src/
mypy src/
```

4. Generate documentation:
```bash
make docs
```

---

## 📂 Project Structure

```
open-source-ids/
├── src/                     # Source code directory
│   ├── core/               # Core IDS components
│   │   ├── signature/      # Signature-based IDS
│   │   ├── anomaly/        # Anomaly-based IDS
│   │   └── host/           # Host-based IDS
│   ├── config/             # Configuration files
│   │   └── suricata.py     # Suricata configuration
│   ├── utils/              # Utility functions
│   │   ├── parsers/        # Data parsing utilities
│   │   └── validators/     # Input validation
│   ├── models/             # Machine learning models
│   │   ├── autoencoder/    # Autoencoder model code
│   │   └── signatures/     # Signature database
│   └── api/                # API endpoints
│       ├── routes/         # API route handlers
│       └── schemas/        # Request/response schemas
├── data/                   # Data storage
│   ├── raw/                # Raw network data
│   ├── processed/          # Processed data
│   └── models/             # Trained models
├── logs/                   # Log files
│   ├── suricata/          # Suricata logs
│   ├── autoencoder/       # Autoencoder logs
│   └── host/              # Host IDS logs
├── templates/              # Flask templates
│   ├── dashboard/         # Main dashboard templates
│   └── components/        # Reusable UI components
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript
│   └── images/            # Images
├── requirements.txt        # Python dependencies
└── README.md              # Documentation
```

## 📚 Documentation

- [API Documentation](docs/api.md)
- [Configuration Guide](docs/config.md)
- [Deployment Guide](docs/deployment.md)
- [Troubleshooting](docs/troubleshooting.md)

## 📊 Database Schema

The project uses SQLAlchemy ORM with the following entities:

```sql
-- Alerts Table
CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    source_ip VARCHAR(15) NOT NULL,
    dest_ip VARCHAR(15) NOT NULL,
    source_port INTEGER,
    dest_port INTEGER,
    protocol VARCHAR(10),
    category VARCHAR(50),
    signature VARCHAR(255),
    severity INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Signatures Table
CREATE TABLE signatures (
    id SERIAL PRIMARY KEY,
    signature_id VARCHAR(50) UNIQUE,
    category VARCHAR(50),
    severity INTEGER,
    description TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Host Events Table
CREATE TABLE host_events (
    id SERIAL PRIMARY KEY,
    host_id VARCHAR(50),
    event_type VARCHAR(50),
    event_data JSONB,
    timestamp TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```bash
open-source-ids/
├── src/                     # Source code directory
│   ├── core/               # Core IDS components
│   │   ├── signature/      # Signature-based IDS
│   │   ├── anomaly/        # Anomaly-based IDS
│   │   └── host/           # Host-based IDS
│   ├── config/             # Configuration files
│   │   ├── suricata.py     # Suricata configuration
│   │   ├── autoencoder.py  # Autoencoder model config
│   │   └── host.py         # Host IDS config
│   ├── utils/              # Utility functions
│   │   ├── parsers/        # Data parsing utilities
│   │   └── validators/     # Input validation
│   ├── models/             # Machine learning models
│   │   ├── autoencoder/    # Autoencoder model code
│   │   └── signatures/     # Signature database
│   └── api/                # API endpoints
│       ├── routes/         # API route handlers
│       └── schemas/        # Request/response schemas
├── data/                   # Data storage
│   ├── raw/                # Raw network data
│   ├── processed/          # Processed data
│   └── models/             # Trained models
├── logs/                   # Log files
│   ├── suricata/          # Suricata logs
│   ├── autoencoder/       # Autoencoder logs
│   └── host/              # Host IDS logs
├── templates/              # Flask templates
│   ├── dashboard/         # Main dashboard templates
│   └── components/        # Reusable UI components
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript
│   └── images/            # Images
├── requirements.txt        # Python dependencies
└── README.md              # Documentation
```

---

## 📌 Future Enhancements

- 🔄 Real-time data ingestion using Kafka
- 🌐 Threat intelligence API integrations
- 📁 SIEM-like alert management (archiving, tagging, acknowledgment)
- 📊 Dashboard enhancement with role-based access control
- 📦 Dockerization for full-stack deployment

---

Feel free to contribute or suggest improvements! 🚀

