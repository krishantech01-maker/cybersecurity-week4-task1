import os
import time

def execute_incident_response_simulation():
    # Ensuring output logging directory path exists
    os.makedirs('logs', exist_ok=True)
    log_path = os.path.join('logs', 'simulation_output.txt')
    
    with open(log_path, 'w') as f:
        print("=== [CRITICAL SECURITY EXERCISE] NIST INCIDENT RESPONSE SIMULATION STARTED ===")
        f.write("=== NIST INCIDENT RESPONSE AUTOMATED EXERCISE AUDIT LOG ===\n\n")
        
        # 1. Detection Phase
        time.sleep(1)
        alert_msg = "[09:30:12] [DETECTION] ALERT: Unauthorized large database dump query detected on Asset ID: DB_09!\n"
        print(alert_msg, end="")
        f.write(alert_msg)
        
        # 2. Containment Phase
        time.sleep(1)
        contain_msg = "[09:31:05] [CONTAINMENT] ACTION: Quarantining compromised Database Node. Disconnecting network interface and disabling active session token matrix.\n"
        print(contain_msg, end="")
        f.write(contain_msg)
        
        # 3. Eradication Phase
        time.sleep(1)
        eradicate_msg = "[09:32:15] [ERADICATION] ACTION: Cleaning persistence indicators. Identified and terminated unauthorized interactive python web shell backdoor.\n"
        print(eradicate_msg, end="")
        f.write(eradicate_msg)
        
        # 4. Recovery Phase
        time.sleep(1)
        recover_msg = "[09:33:40] [RECOVERY] ACTION: Restoring database records from trusted read-only point-in-time snapshot. Running strict compliance asset checks.\n"
        print(recover_msg, end="")
        f.write(recover_msg)
        
        # 5. Lessons Learned Phase
        time.sleep(1)
        lessons_msg = "[09:35:00] [LESSONS LEARNED] CONCLUSION: Root cause identified as SQLi credential theft. Recommendation updated: Enforce prepared query parameters and restrict database egress ports.\n"
        print(lessons_msg, end="")
        f.write(lessons_msg)
        
        final_status = "\n[SUCCESS] Simulated Incident Handling Exercise executed smoothly. Output captured inside 'logs/simulation_output.txt'.\n"
        print(final_status)
        f.write(final_status)

if __name__ == "__main__":
    execute_incident_response_simulation()
