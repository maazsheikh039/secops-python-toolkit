import json
import pandas as pd

class IAMRiskScorer:
    '''
    Identity and Access Management Risk Scoring System
    Analyzes user behavior, permissions, and anomalies to calculate risk scores
    '''
    
    def __init__(self, data_file):
        '''Initialize the risk scorer with user data'''
        with open(data_file, 'r') as f:
            self.users = json.load(f)
        self.risk_scores = []
    
    def calculate_permission_risk(self, permissions):
        '''
        Calculate risk score based on permissions granted
        
        Args:
            permissions: List of permission strings
        
        Returns:
            Integer risk score (0-30)
        '''
        risk_score = 0
        high_risk_perms = ["admin", "sudo", "config_change", "delete"]
        medium_risk_perms = ["deploy", "database_access"]
        
        for perm in permissions:
            if perm in high_risk_perms:
                risk_score += 10
            elif perm in medium_risk_perms:
                risk_score += 5
            else:
                risk_score += 1
        
        return min(risk_score, 30)  # Cap at 30
    
    def calculate_behavior_risk(self, activity):
        '''
        Calculate risk score based on user behavior patterns
        
        Args:
            activity: Dictionary containing activity metrics
        
        Returns:
            Integer risk score (0-40)
        '''
        risk_score = 0
        
        # Failed login attempts (high risk indicator)
        if activity["failed_logins"] > 10:
            risk_score += 15
        elif activity["failed_logins"] > 5:
            risk_score += 8
        
        # Off-hours access
        if activity["off_hours_access"] > 20:
            risk_score += 12
        elif activity["off_hours_access"] > 10:
            risk_score += 6
        
        # Privilege escalation attempts
        risk_score += activity["privilege_escalation_attempts"] * 5
        
        # Excessive data downloads
        if activity["data_downloads"] > 40:
            risk_score += 8
        
        return min(risk_score, 40)  # Cap at 40
    
    def calculate_account_hygiene_risk(self, last_password_change):
        '''
        Calculate risk based on account security hygiene
        
        Args:
            last_password_change: Days since last password change
        
        Returns:
            Integer risk score (0-30)
        '''
        if last_password_change > 180:
            return 30
        elif last_password_change > 90:
            return 20
        elif last_password_change > 60:
            return 10
        else:
            return 5
    
    def score_all_users(self):
        '''
        Calculate comprehensive risk scores for all users
        '''
        for user in self.users:
            perm_risk = self.calculate_permission_risk(user["permissions"])
            behavior_risk = self.calculate_behavior_risk(user["activity"])
            hygiene_risk = self.calculate_account_hygiene_risk(user["last_password_change"])
            
            total_risk = perm_risk + behavior_risk + hygiene_risk
            
            if total_risk >= 70:
                risk_level = "CRITICAL"
            elif total_risk >= 50:
                risk_level = "HIGH"
            elif total_risk >= 30:
                risk_level = "MEDIUM"
            else:
                risk_level = "LOW"
            
            self.risk_scores.append({
                "username": user["username"],
                "role": user["role"],
                "department": user["department"],
                "permission_risk": perm_risk,
                "behavior_risk": behavior_risk,
                "hygiene_risk": hygiene_risk,
                "total_risk_score": total_risk,
                "risk_level": risk_level
            })
    
    def generate_report(self):
        '''Generate and display risk assessment report'''
        df = pd.DataFrame(self.risk_scores)
        df = df.sort_values('total_risk_score', ascending=False)
        
        print("\n" + "="*80)
        print("IAM RISK ASSESSMENT REPORT")
        print("="*80)
        print(df.to_string(index=False))
        print("\n" + "="*80)
        
        print("\nRISK SUMMARY:")
        print(f"Total Users Analyzed: {len(self.risk_scores)}")
        print(f"Critical Risk: {len(df[df['risk_level'] == 'CRITICAL'])}")
        print(f"High Risk: {len(df[df['risk_level'] == 'HIGH'])}")
        print(f"Medium Risk: {len(df[df['risk_level'] == 'MEDIUM'])}")
        print(f"Low Risk: {len(df[df['risk_level'] == 'LOW'])}")
        print(f"Average Risk Score: {df['total_risk_score'].mean():.2f}")
        
        df.to_csv('risk_report.csv', index=False)
        print("\nDetailed report saved to: risk_report.csv")

if __name__ == "__main__":
    scorer = IAMRiskScorer('iam_data.json')
    scorer.score_all_users()
    scorer.generate_report()
