# Open Source IDS - Phase 1: Signature-based IDS

This phase focuses on setting up a signature-based IDS using Suricata.

## 📌 Components
- Suricata configuration and rules
- Sample PCAP files for testing
- Logs stored in EVE JSON format

## 🚀 How to Run
1. Install Suricata: `sudo apt install suricata`
2. Update `suricata.yaml` for EVE JSON output
3. Add custom rules in `local.rules`
4. Run using:
```bash
sudo suricata -c ./phase1-sids/suricata-config/suricata.yaml -i eth0 -l ./phase1-sids/logs

