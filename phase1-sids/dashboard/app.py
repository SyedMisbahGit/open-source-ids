from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
EVE_LOG_PATH = "/var/log/suricata/eve.json"

def load_alerts():
    alerts = []
    if os.path.exists(EVE_LOG_PATH):
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
                except json.JSONDecodeError:
                    continue
    return alerts

@app.route("/", methods=["GET"])
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

    return render_template(
        "index.html",
        alerts=filtered[-100:],  # Last 100 alerts
        protocols=protocols,
        categories=categories,
        signatures=signatures
    )

if __name__ == "__main__":
    app.run(debug=True)
