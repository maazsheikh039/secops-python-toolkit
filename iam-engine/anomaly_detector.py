import json
import statistics

class AnomalyDetector:
    '''
    Detect anomalous behavior patterns in user activities
    '''
    
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            self.users = json.load(f)
    
    def detect_anomalies(self):
        '''
        Identify users with anomalous behavior patterns
        '''
        login_counts = [u["activity"]["login_count"] for u in self.users]
        failed_logins = [u["activity"]["failed_logins"] for u in self.users]
        off_hours = [u["activity"]["off_hours_access"] for u in self.users]
        
        login_mean = statistics.mean(login_counts)
        login_std = statistics.stdev(login_counts) if len(login_counts) > 1 else 0
        
        failed_mean = statistics.mean(failed_logins)
        failed_std = statistics.stdev(failed_logins) if len(failed_logins) > 1 else 0
        
        off_hours_mean = statistics.mean(off_hours)
        off_hours_std = statistics.stdev(off_hours) if len(off_hours) > 1 else 0
        
        print("\n" + "="*80)
        print("ANOMALY DETECTION REPORT")
        print("="*80)
        
        anomalies_found = False
        
        for user in self.users:
            anomalies = []
            activity = user["activity"]
            
            if login_std > 0 and activity["login_count"] > login_mean + (2 * login_std):
                anomalies.append(f"Excessive logins: {activity['login_count']}")
            
            if failed_std > 0 and activity["failed_logins"] > failed_mean + (2 * failed_std):
                anomalies.append(f"High failed logins: {activity['failed_logins']}")
            
            if off_hours_std > 0 and activity["off_hours_access"] > off_hours_mean + (2 * off_hours_std):
                anomalies.append(f"Unusual off-hours access: {activity['off_hours_access']}")
            
            if activity["privilege_escalation_attempts"] > 0:
                anomalies.append(f"Privilege escalation attempts: {activity['privilege_escalation_attempts']}")
            
            if anomalies:
                anomalies_found = True
                print(f"\nUSER: {user['username']} ({user['role']})")
                print(f"Department: {user['department']}")
                print("Anomalies detected:")
                for anomaly in anomalies:
                    print(f"  - {anomaly}")
        
        if not anomalies_found:
            print("\nNo significant anomalies detected.")
        
        print("\n" + "="*80)

if __name__ == "__main__":
    detector = AnomalyDetector('iam_data.json')
    detector.detect_anomalies()
