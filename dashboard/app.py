from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
EVE_LOG_PATH = "../logs/eve.json"

def load_alerts():
    alerts = []
    if os.path.exists(EVE_LOG_PATH):
        with open(EVE_LOG_PATH) as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get("event_type") == "alert":
                        alerts.append(data)
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
        proto = alert.get("proto")
        category = alert.get("alert", {}).get("category")
        signature = alert.get("alert", {}).get("signature")

        if protocol_filter and protocol_filter != proto:
            continue
        if category_filter and category_filter != category:
            continue
        if signature_filter and signature_filter != signature:
            continue

        filtered.append(alert)

    protocols = sorted(set(a.get("proto") for a in alerts if a.get("proto")))
    categories = sorted(set(a.get("alert", {}).get("category") for a in alerts if a.get("alert")))
    signatures = sorted(set(a.get("alert", {}).get("signature") for a in alerts if a.get("alert")))

    return render_template(
        "index.html",
        alerts=filtered[-100:],  # show last 100 alerts
        protocols=protocols,
        categories=categories,
        signatures=signatures
    )

if __name__ == "__main__":
    app.run(debug=True)
