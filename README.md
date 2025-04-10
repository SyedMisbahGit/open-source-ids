# Open-Source IDS/XDR Project

This is an open-source, phase-wise implementation of an Intrusion Detection System (IDS) that evolves into a full Extended Detection & Response (XDR) system. The goal is to combine rule-based, anomaly-based, and host-based detection under a unified dashboard using free and open-source tools.

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
- [x] Anomaly evaluation script
- [x] Mini-dashboard to view anomaly results

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

```bash
# Clone the repo
$ git clone https://github.com/SyedMisbahGit/open-source-ids.git
$ cd open-source-ids

# Setup virtual environment
$ python3 -m venv venv310
$ source venv310/bin/activate

# Install dependencies
(venv310) $ pip install -r requirements.txt

# Run dashboard (example)
(venv310) $ cd phase1-sids/dashboard
(venv310) $ python3 app.py
```

---

## 📂 Directory Structure (WIP)

```bash
open-source-ids/
├── phase1-sids/
│   ├── dashboard/           # Flask dashboard for Suricata
│   └── suricata-config/     # Suricata rules, logs
├── phase2-abids/
│   ├── training/            # Autoencoder model training scripts
│   ├── evaluation/          # Anomaly detection output (CSV)
│   └── dashboard/           # Flask dashboard for ABIDS
├── phase3-merged-dashboard/ # Unified dashboard (in progress)
├── README.md
└── requirements.txt
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

