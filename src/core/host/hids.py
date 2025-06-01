from typing import List, Dict, Optional
import logging
from pathlib import Path
import json
from datetime import datetime
import psutil

class HostIDS:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.event_log_path = Path('logs/host/events.log')
        self.rules = self._load_rules()

    def _load_rules(self) -> Dict[str, Dict]:
        """Load host-based detection rules"""
        rules = {
            'cpu_threshold': 90,  # CPU usage threshold
            'memory_threshold': 90,  # Memory usage threshold
            'disk_threshold': 90,  # Disk usage threshold
            'new_process_threshold': 10,  # Number of new processes in interval
            'network_threshold': 1000,  # Network connections threshold
        }
        return rules

    def _check_cpu(self) -> List[Dict]:
        """Check CPU usage for anomalies"""
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > self.rules['cpu_threshold']:
            return [{
                'timestamp': datetime.now().isoformat(),
                'category': 'Resource Usage',
                'signature': 'High CPU Usage',
                'severity': 4,
                'details': {
                    'cpu_percent': cpu_percent,
                    'threshold': self.rules['cpu_threshold']
                }
            }]
        return []

    def _check_memory(self) -> List[Dict]:
        """Check memory usage for anomalies"""
        mem = psutil.virtual_memory()
        if mem.percent > self.rules['memory_threshold']:
            return [{
                'timestamp': datetime.now().isoformat(),
                'category': 'Resource Usage',
                'signature': 'High Memory Usage',
                'severity': 4,
                'details': {
                    'memory_percent': mem.percent,
                    'total': mem.total,
                    'available': mem.available,
                    'threshold': self.rules['memory_threshold']
                }
            }]
        return []

    def _check_disk(self) -> List[Dict]:
        """Check disk usage for anomalies"""
        disk = psutil.disk_usage('/')
        if disk.percent > self.rules['disk_threshold']:
            return [{
                'timestamp': datetime.now().isoformat(),
                'category': 'Resource Usage',
                'signature': 'High Disk Usage',
                'severity': 4,
                'details': {
                    'disk_percent': disk.percent,
                    'total': disk.total,
                    'free': disk.free,
                    'threshold': self.rules['disk_threshold']
                }
            }]
        return []

    def _check_processes(self) -> List[Dict]:
        """Check for suspicious processes"""
        alerts = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_percent']):
                try:
                    if proc.info['memory_percent'] > 10.0:  # Example threshold
                        alerts.append({
                            'timestamp': datetime.now().isoformat(),
                            'category': 'Process Activity',
                            'signature': 'High Memory Process',
                            'severity': 3,
                            'details': {
                                'pid': proc.info['pid'],
                                'name': proc.info['name'],
                                'username': proc.info['username'],
                                'memory_percent': proc.info['memory_percent']
                            }
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        except Exception as e:
            self.logger.error(f"Error checking processes: {str(e)}")
        return alerts

    def get_recent_alerts(self, limit: int = 100) -> List[Dict]:
        """Get recent host-based alerts"""
        alerts = []
        try:
            # Check system metrics
            alerts.extend(self._check_cpu())
            alerts.extend(self._check_memory())
            alerts.extend(self._check_disk())
            alerts.extend(self._check_processes())

            # Sort by timestamp and limit results
            alerts = sorted(alerts, key=lambda x: x['timestamp'], reverse=True)[:limit]

        except Exception as e:
            self.logger.error(f"Error getting recent alerts: {str(e)}")
        return alerts

    def get_rule_count(self) -> int:
        """Get number of active rules"""
        return len(self.rules)

    def get_system_metrics(self) -> Dict:
        """Get current system metrics"""
        return {
            'cpu': psutil.cpu_percent(interval=None),
            'memory': psutil.virtual_memory().percent,
            'disk': psutil.disk_usage('/').percent,
            'process_count': len(psutil.pids()),
            'network_connections': len(psutil.net_connections())
        }
