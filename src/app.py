from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
import os
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the root directory of the project
ROOT_DIR = Path(__file__).parents[2]
EVE_LOG_PATH = os.getenv('SURICATA_LOG_PATH', str(ROOT_DIR / 'logs' / 'eve.json'))

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(EVE_LOG_PATH), exist_ok=True)

def load_alerts():
    alerts = []
    try:
        if not os.path.exists(EVE_LOG_PATH):
            logger.warning(f"Suricata log file not found at {EVE_LOG_PATH}")
            return []

        try:
            with open(EVE_LOG_PATH) as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        if data.get("event_type") == "alert":
                            # Flatten required fields
                            alerts.append({
                                "timestamp": data.get("timestamp"),
                                "category": data.get("alert", {}).get("category"),
                                "signature": data.get("alert", {}).get("signature"),
                                "proto": data.get("proto"),
                                "src_ip": data.get("src_ip"),
                                "dest_ip": data.get("dest_ip"),
                            })
                    except json.JSONDecodeError as e:
                        logger.error(f"Error parsing JSON line: {str(e)}")
                        continue
        except PermissionError:
            logger.error(f"Permission denied accessing {EVE_LOG_PATH}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error reading alerts: {str(e)}")
            return []

    except Exception as e:
        logger.error(f"Error in load_alerts: {str(e)}")
        return []
    
    return alerts

@app.route("/")
def index():
    protocol_filter = request.args.get("protocol")
    category_filter = request.args.get("category")
    signature_filter = request.args.get("signature")

    alerts = load_alerts()
    filtered = []

    for alert in alerts:
        if protocol_filter and protocol_filter != alert.get("proto"):
            continue
        if category_filter and category_filter != alert.get("category"):
            continue
        if signature_filter and signature_filter != alert.get("signature"):
            continue
        filtered.append(alert)

    protocols = sorted(set(a.get("proto") for a in alerts if a.get("proto")))
    categories = sorted(set(a.get("category") for a in alerts if a.get("category")))
    signatures = sorted(set(a.get("signature") for a in alerts if a.get("signature")))

    # Get traffic statistics
    traffic_count = len(alerts)
    
    # Get unique signatures count
    signatures_count = len(set(a.get("signature") for a in alerts if a.get("signature")))
    
    return render_template(
        "index.html",
        alerts=filtered[-100:],  # Last 100 alerts
        protocols=protocols,
        categories=categories,
        signatures=signatures,
        traffic_count=traffic_count,
        signatures_count=signatures_count
    )

if __name__ == "__main__":
    app.run(debug=True)
