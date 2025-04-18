# 🚨 Open Source Hybrid IDS (Intrusion Detection System) 🚨  
A centralized-controlled, hybrid, open-source Intrusion Detection System that combines Signature-based IDS (S-IDS), Anomaly-based IDS (A-IDS using Deep Learning), and Host-based IDS (H-IDS) into a unified dashboard-driven detection-only architecture.

---

## 📁 Repository Structure

open-source-ids/ ├── dashboard/ # Flask-based Central Dashboard │ ├── templates/ # HTML templates (index.html, etc.) │ ├── static/ # JS, CSS, Icons │ └── app.py # Flask backend with control panel ├── models/ # Deep Learning models (Bi-LSTM, etc.) ├── datasets/ # CIC-IDS 2017 & other test datasets ├── scripts/ # tcpreplay, Suricata triggers, etc. ├── hids/ # H-IDS tools like OSSEC/Wazuh configs ├── logs/ # Suricata eve.json and model predictions └── README.md # You're here!


---

## 🌐 System Architecture Overview

        +---------------------------+
        |     Incoming/Outgoing     |
        |         Traffic           |
        +-------------+-------------+
                      |
                +-----v------+
                |   S-IDS    | (Signature-Based)
                +-----+------+
                      |
    +-----------------+-------------------+
    | Match Found?                         |
    | Yes → 🚨 Alert Dashboard             |
    | No  → Granularize → Forward to A-IDS |
    +-----------------+-------------------+
                      |
                +-----v------+
                |   A-IDS    | (Bi-LSTM DL Model)
                +-----+------+
                      |
    +-----------------+-------------------------+
    | Anomaly Found?                             |
    | Yes → 🚨 Alert Dashboard + 🧠 Update S-IDS |
    | No → Possibly Malicious → Alert Dashboard  |
    +-----------------+-------------------------+
                      |
               Internal Network
                      |
                +-----v-----+
                |   H-IDS   |
                +-----------+

---

## 🧠 Features & Capabilities

| Component | Description |
|----------|-------------|
| 🔐 **S-IDS (Suricata)** | Scans for known attack signatures |
| 🤖 **A-IDS (Bi-LSTM)** | Detects unseen patterns in granular traffic |
| 🧱 **H-IDS** | Detects internal and post-NIDS threats |
| 📊 **Dashboard** | Real-time alert visualization, traffic control, mode switch |
| 🔁 **Mode Switch** | Toggle between Live Traffic ↔ Dataset-based Simulation |
| 🎯 **Traffic Granularization** | Extracts packet-level features for anomaly detection |
| 🔒 **Encrypted Traffic Handling** | Partial visibility via metadata & statistical patterns |

---

## 🎓 Research Basis

- 📚 **Dataset**: [CIC-IDS 2017](https://www.unb.ca/cic/datasets/ids-2017.html)  
- 🤖 **Model**: Bi-LSTM used to capture bi-directional flow behavior  
- 🧪 **Simulation**: tcpreplay used to replay `.pcap` files as synthetic traffic  
- 📄 **Papers Studied**: 10+ IDS research papers + real-world tools compared (Snort, Suricata, OSSEC, etc.)

---

## ✅ Completed Milestones

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | S-IDS Setup with Suricata + Dashboard | ✅ Complete |
| Phase 2 | A-IDS Planning with Bi-LSTM + Granular Dataset | ✅ Planned |
| Phase 3 | Dashboard Merge + Control Panel UI | ✅ Complete |
| Phase 4 | Presentation & Research Prep | ✅ Complete |
| Phase 5 | H-IDS Planning with OSSEC/Wazuh | 🕐 Upcoming |

---

## 🛠 How to Run

### ⚙️ Prerequisites

```bash
sudo apt update
sudo apt install suricata tcpreplay python3 python3-pip
pip3 install flask pandas scikit-learn matplotlib tensorflow

