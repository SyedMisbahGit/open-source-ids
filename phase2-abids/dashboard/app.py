from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

MODE_FILE = "dashboard/mode_state.txt"
PCAP_PATH = "dataset/CIC-IDS2017-sample.pcap"

# Load current mode from file
def get_current_mode():
    try:
        with open(MODE_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "live"

# Save selected mode
def set_current_mode(mode):
    with open(MODE_FILE, "w") as f:
        f.write(mode)

@app.route('/')
def index():
    current_mode = get_current_mode()
    return render_template('index.html', mode=current_mode)

@app.route('/set_mode', methods=['GET'])
def set_mode():
    mode = request.args.get('type')
    if mode not in ['live', 'dataset']:
        return jsonify({'status': 'error', 'message': 'Invalid mode'})
    
    set_current_mode(mode)
    
    if mode == "live":
        os.system("sudo systemctl restart suricata")  # Ensure Suricata is running on live iface
    else:
        os.system("sudo systemctl stop suricata")  # Optional: pause Suricata during replay

    return jsonify({'status': 'success', 'mode': mode})

@app.route('/replay_dataset', methods=['POST'])
def replay_dataset():
    if get_current_mode() != "dataset":
        return jsonify({'status': 'error', 'message': 'Switch to dataset mode first'})

    replay_command = f"sudo tcpreplay -i lo {PCAP_PATH}"
    os.system(replay_command)

    return jsonify({'status': 'success', 'message': 'Dataset traffic replayed'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
