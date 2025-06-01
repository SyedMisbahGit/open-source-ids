from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path
import json
import logging
from src.config.suricata import SURICATA_CONFIG

class SignatureIDS:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.log_path = Path(SURICATA_CONFIG['LOG_PATH'])
        self.rules_dir = Path(SURICATA_CONFIG['RULES_DIR'])
        self.rules = self._load_rules()

    def _load_rules(self) -> Dict[str, Dict]:
        """Load and parse Suricata rules"""
        rules = {}
        for rule_file in self.rules_dir.glob('*.rules'):
            try:
                with open(rule_file) as f:
                    for line in f:
                        if line.strip() and not line.startswith('#'):
                            # Parse rule (simplified example)
                            rule_id = self._extract_rule_id(line)
                            if rule_id:
                                rules[rule_id] = {
                                    'signature': line.strip(),
                                    'category': self._extract_category(line),
                                    'severity': self._extract_severity(line)
                                }
            except Exception as e:
                self.logger.error(f"Error loading rules from {rule_file}: {str(e)}")
        return rules

    def _extract_rule_id(self, rule: str) -> Optional[str]:
        """Extract rule ID from Suricata rule format"""
        # Simplified rule ID extraction
        parts = rule.split()
        if len(parts) > 1:
            return parts[1]
        return None

    def _extract_category(self, rule: str) -> str:
        """Extract category from Suricata rule format"""
        # Simplified category extraction
        return "unknown"

    def _extract_severity(self, rule: str) -> int:
        """Extract severity from Suricata rule format"""
        return 3  # Default severity

    def get_recent_alerts(self, limit: int = 100) -> List[Dict]:
        """Get recent alerts from Suricata logs"""
        alerts = []
        try:
            if not self.log_path.exists():
                self.logger.warning(f"Suricata log file not found: {self.log_path}")
                return []

            with open(self.log_path) as f:
                for line in f:
                    try:
                        alert = json.loads(line)
                        if alert.get('event_type') == 'alert':
                            alerts.append({
                                'timestamp': alert.get('timestamp'),
                                'source_ip': alert.get('src_ip'),
                                'dest_ip': alert.get('dest_ip'),
                                'source_port': alert.get('src_port'),
                                'dest_port': alert.get('dest_port'),
                                'protocol': alert.get('proto'),
                                'category': alert.get('alert', {}).get('category'),
                                'signature': alert.get('alert', {}).get('signature'),
                                'severity': alert.get('alert', {}).get('severity', 3)
                            })
                    except json.JSONDecodeError:
                        continue

            return sorted(alerts, key=lambda x: x['timestamp'], reverse=True)[:limit]

        except Exception as e:
            self.logger.error(f"Error getting recent alerts: {str(e)}")
            return []

    def get_signatures(self) -> List[Dict]:
        """Get all loaded signatures"""
        return list(self.rules.values())

    def get_traffic_count(self) -> int:
        """Get total number of alerts"""
        try:
            if not self.log_path.exists():
                return 0

            with open(self.log_path) as f:
                return sum(1 for line in f if line.strip() and not line.startswith('#'))
        except Exception as e:
            self.logger.error(f"Error getting traffic count: {str(e)}")
            return 0
