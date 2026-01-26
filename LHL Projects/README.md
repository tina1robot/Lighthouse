# LHL Cybersecurity Projects Portfolio

Author: Tina (Christina McNeice)
Program: Lighthouse Labs Cybersecurity Course
Date: July 2024

---

## Overview

This folder contains four cybersecurity projects completed during the Lighthouse Labs cybersecurity training program. The projects progress from network analysis to risk assessment and incident response planning.

## Projects

| Project | Title | Focus |
|---------|-------|-------|
| P1 | Dirty Dog Labs Network Analysis | Network security assessment and vulnerability scanning |
| P2 | Big Dog Risk Assessment | Comprehensive security risk analysis |
| P2 (Exec) | Big Dog Executive Summary | Risk findings summary for leadership |
| P3 | Cat in Box Incident Response Playbook | Phishing attack response procedures |

---

## Project Details

### P1: Dirty Dog Labs Network Analysis

Date: July 1, 2024
File: P1__Dirty_Dog_Labs_Network_Analysis.pdf

What it covers

A network security assessment of a virtualized lab environment containing three machines:
- Windows 11 system (10.0.2.4 / 24)
- Kali Linux penetration testing machine (10.0.2.8 / 24)
- Ubuntu Linux Server (10.0.3.15 / 24)

Key findings

- Network is stable with limited minor vulnerabilities
- Virtual machine architecture is well-managed
- Needs firewall between host and internet provider
- Limited hardware resources causing potential performance issues

Tools used

- Nmap for vulnerability scanning and port enumeration
- Wireshark for network packet analysis
- CLI commands for system verification (ifconfig, ip addr, arp, neofetch, fastfetch)
- Zenmap for GUI-based nmap visualization

Security recommendations

1. Firewall between main computer and internet provider
2. VLAN segmentation for separate networks
3. Patch management with automated antivirus and software updates
4. Strong authentication with password policies and multi-factor authorization
5. Review network service configurations
6. Restrict network access with access control for critical data
7. Network traffic monitoring for suspicious activity detection

Deliverables

- Executive summary with current network topology
- Device information (hostnames, IP addresses, MAC addresses, OS versions)
- Proposed future topology with firewall implementation
- 21 screen captures showing CLI outputs and network analysis

---

### P2: Big Dog Risk Assessment & Executive Summary

Date: July 2024
Files: P2__Big_Dog_Risk_Assessment.pdf and P2__Exec_Summary_for_Big_Dog_Risk_Assessment.pptx

What it covers

A comprehensive risk assessment for Big Dog Manufacturing analyzing:
- Current security posture
- Identified vulnerabilities and threats
- Business impact analysis
- Risk prioritization matrix
- Remediation roadmap
- Cost-benefit analysis

Executive summary

The PowerPoint provides a high-level overview for leadership including:
- Key findings and actionable insights
- Visual risk matrices
- Prioritized recommendations with timelines
- Budget impact summary

Analysis areas

- Assets at risk and critical systems
- Threat landscape assessment
- Vulnerability gap analysis
- Business impact and financial consequences
- Likelihood and impact scoring for risk prioritization

Deliverables

- Comprehensive written risk assessment
- Executive presentation
- Risk matrix visualizations
- Prioritized action plan with timelines
- Budget considerations for remediation

---

### P3: Cat in Box Manufacturing - Incident Response Playbook

Date: July 18, 2024
File: P4__Cyber_Security_Response__Playbook_for_Cat___Box.pdf

What it covers

A complete incident response framework for Cat in Box Manufacturing focusing on phishing attack procedures.

Organizational roles

- SOC Team: continuous monitoring
- Cat (MSSP Consultant): primary coordinator
- Percy (CEO): escalation contact
- Misha and Minka (Production Managers): operational impact assessment
- Dusty (Database Specialist), Lucky (IT Support), Ned (Network Admin): technical response

Response phases

Detection and analysis: SOC identifies incident, initial severity assessment, evidence collection

Classification: Risk level determined and appropriate teams notified

Containment and remediation: Response team assembled, privileges revoked, credentials reset, systems scanned

Recovery: Systems restored to normal operations, post-compromise monitoring

Post-incident: Full analysis, root cause determination, playbook improvements

Incident classification

- Major impact: notify production managers immediately
- Escalated issues: notify CEO
- Unresolved after 24 hours: CEO escalation required

Communication templates

Two templates included for incident notification:
- Technical letter to MSSP consultant with detailed incident information
- Non-technical letter to CEO with business impact summary

Frameworks used

- NIST Incident Response Lifecycle
- MITRE ATT&CK
- SANS Incident Handler's Handbook
- CISA Guidelines

Deliverables

- 10-page incident response playbook
- Detailed workflow for phishing attacks
- Role and responsibility matrix
- Communication templates
- Escalation procedures and timelines

---

## Technical Skills

Tools and software
- Nmap for network scanning and vulnerability assessment
- Wireshark for packet capture and analysis
- Zenmap for graphical network mapping
- Kali Linux for penetration testing
- Linux and Windows command line

Assessment methodologies
- Network topology analysis and design
- Vulnerability scanning and port enumeration
- Packet analysis and traffic examination
- Risk assessment and threat identification
- Incident response planning and procedures

Documentation and communication
- Technical security reports
- Executive summaries for leadership
- Operational procedures and playbooks
- Risk analysis and prioritization
- Incident notification procedures

Security frameworks and standards
- NIST Special Publication 800-61 Incident Handling Guide
- MITRE ATT&CK Framework
- SANS Incident Handler's Handbook
- CISA Incident Response Guidelines
- Federal Government Cybersecurity Playbooks

---

## Metrics and Results

P1 Network Analysis

Devices scanned: 3 machines
Ports analyzed: 1000+ per device
ARP ping scan time: 93.81 seconds
Open services identified: HTTP (80/tcp), MSRPC (135/tcp), NetBIOS (139/tcp), Microsoft-DS (445/tcp)
Vulnerabilities found: Limited minor vulnerabilities
Recommendations: 6 major security enhancements

P3 Incident Response

Threat type: Phishing attacks
Response phases: 7 stages from detection to post-incident
Escalation timeline: 24-hour threshold for CEO notification
Roles defined: 8 specific personnel responsibilities
Communication channels: Technical and executive templates

---

## Project Progression

How these projects connect

P1 Foundation: Network Analysis
- Establishes baseline security posture
- Identifies network architecture and vulnerabilities

P2 Assessment: Risk Analysis
- Uses P1 findings as baseline
- Expands to enterprise-level risk evaluation
- Prioritizes remediation efforts
- Presents findings to leadership

P3 Response: Incident Playbook
- Develops response procedures for realistic scenarios
- Defines roles and communication channels
- Establishes incident response framework

Learning progression

1. Hands-on technical skills: network scanning, packet analysis, system enumeration
2. Risk analysis and strategy: risk assessment, prioritization, business impact analysis
3. Operational security planning: incident response procedures, communication frameworks, team coordination

---

## How to Use This Portfolio

For job interviews

Highlight the progression from technical assessment to strategic planning. Key talking points include:
- Conducted comprehensive security assessments using industry-standard tools
- Developed risk assessment and prioritization frameworks
- Created incident response procedures aligned with NIST and CISA guidelines
- Produced communication strategies for both technical and executive audiences

For continuing education

- Use P1 as reference for network assessment procedures
- Reference P3 playbook for incident response best practices
- Study P2 for risk assessment methodologies

For implementation

- Adapt P3 playbook for your organization
- Use communication templates as starting points
- Reference role definitions for incident response team structure

---

## Important Notes

All projects use fictional company names and scenarios. Network analysis was performed in a controlled lab environment. Playbook procedures follow industry-standard frameworks. Implementation should be customized for your specific environment.

---

## References

NIST resources
- NIST Special Publication 800-61 Revision 2: Computer Security Incident Handling Guide

Federal guidelines
- Federal Government Cybersecurity Incident & Vulnerability Response Playbooks
- CISA Incident Detection, Response, and Prevention

Industry standards
- MITRE ATT&CK Framework
- SANS Incident Handler's Handbook

Tools documentation
- Nmap: https://nmap.org
- Wireshark: https://www.wireshark.org
- Kali Linux: https://www.kali.org

---

## Summary of Capabilities

This portfolio demonstrates competency in:

- Network security assessment: scanning, enumeration, topology analysis
- Vulnerability identification: port analysis, service enumeration, risk evaluation
- Risk assessment and analysis: threat prioritization, business impact analysis
- Incident response planning: procedure development, role definition, communication strategies
- Technical communication: report writing, executive summaries, procedural documentation
- Leadership engagement: translating technical findings for executive stakeholders
- Framework application: NIST, MITRE, SANS, CISA standards implementation
- Team coordination: role definition, escalation procedures, cross-functional communication

---

## Contact

Prepared by: Tina (Christina McNeice)
Training program: Lighthouse Labs Cybersecurity
Completion date: July 2024

---

Last updated: January 2026

