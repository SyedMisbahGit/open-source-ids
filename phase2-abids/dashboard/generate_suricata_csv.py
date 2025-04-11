import json
import csv
import os

# Adjust paths
input_path = '../../phase1-sids/logs/eve.json'
output_path = '../../phase1-sids/suricata_alerts.csv'

# Ensure directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
    fieldnames = ['timestamp', 'src_ip', 'dest_ip', 'proto', 'alert_msg', 'type']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for line in infile:
        try:
            event = json.loads(line)
            if event.get('event_type') == 'alert':
                writer.writerow({
                    'timestamp': event.get('timestamp'),
                    'src_ip': event.get('src_ip'),
                    'dest_ip': event.get('dest_ip'),
                    'proto': event.get('proto'),
                    'alert_msg': event['alert']['signature'],
                    'type': 'Signature'
                })
        except:
            continue

print("[✓] suricata_alerts.csv generated successfully.")
