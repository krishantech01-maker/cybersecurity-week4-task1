# NIST SP 800-61 r2 Incident Response Playbook Plan

## 1. Preparation (Taiyari)
- Deploy centralized logging via SIEM infrastructure.
- Implement strict Identity and Access Management (IAM) controls with mandatory Multi-Factor Authentication (MFA).
- Establish communication matrices for the Cyber Incident Response Team (CIRT).

## 2. Detection & Analysis (Pehchan)
- Monitor anomaly-based alerts signaling concurrent logins from disparate physical geographic locations.
- Analyze host-based logs for unauthorized administrative process injection or database dumps.

## 3. Containment, Eradication & Recovery (Action)
- **Containment:** Quarantine compromised endpoint nodes immediately at the network switch or firewall layer. Expire active administrative OAuth tokens.
- **Eradication:** Locate and delete persistence artifacts (cron jobs, registry runs). Terminate unauthorized backdoors.
- **Recovery:** Perform point-in-time system state restorations from trusted read-only database backups.

## 4. Post-Incident Activity (Lessons Learned)
- Document the threat vector timeline from initial access to detection.
- Patch the architectural weakness exploited during the breach to prevent future zero-day events.
