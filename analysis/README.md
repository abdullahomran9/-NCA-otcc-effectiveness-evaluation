# Implementing and Evaluating NCA OTCC Controls in a Virtual ICS Environment

This repository contains a case study that evaluates the implementation and effectiveness of selected controls from the National Cybersecurity Authority of Saudi Arabia (NCA) Operational Technology Cybersecurity Controls (OTCC) within a virtual Industrial Control System (ICS) environment.

## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Virtual ICS Lab Setup](#virtual-ics-lab-setup)
- [OTCC Controls Implemented](#otcc-controls-implemented)
- [Results and Analysis](#results-and-analysis)
- [Conclusion](#conclusion)
- [Files in this Repository](#files-in-this-repository)
- [Contributing](#contributing)

## Overview




As industrial control systems (ICS) become increasingly interconnected, they face heightened cybersecurity threats. This case study explores the implementation of specific OTCC controls in a virtual ICS environment, focusing on network management, identity and access management (IAM), security information and event management (SIEM), and system protection.

## Objectives

- Evaluate the effectiveness of selected OTCC controls in enhancing ICS cybersecurity.
- Identify challenges and limitations in applying these controls to real-world scenarios.
- Provide insights into the practical application of OTCC guidelines within a virtual ICS environment.

## Virtual ICS Lab Setup

The virtual ICS environment is set up using Oracle VM VirtualBox and includes the following components:

- **Factory I/O:** Simulates the physical processes.
- **OpenPLC:** Manages multiple PLCs within the OT network.
- **ScadaBR:** Provides SCADA functionality in the IT network.
- **Wazuh SIEM:** Serves as the security information and event management solution.
- **PfSense:** Configures routers and firewalls to segment networks.

### Key Considerations

- The simulation is divided into three parts due to computational constraints.
- This setup represents a simplified version of an ICS network.

### Network Diagram

Below is the network diagram illustrating the setup of the virtual ICS environment:

![Network Diagram](OTCC%20Controls3.drawio.png)

## OTCC Controls Implemented

The following OTCC controls were selected and implemented:

1. **Network Segmentation (Control 2-4):** Isolates network segments to enhance security.
2. **Identity and Access Management (Control 2-2):** Implements authentication and authorization mechanisms.
3. **Cybersecurity Event Logs and Monitoring (Control 2-11):** Establishes logging and monitoring for threat detection.
4. **System and Processing Facilities Protection (Control 2-3):** Secures systems against unauthorized access and modifications.

## Results and Analysis

The implementation revealed several key findings:

- **Network Segmentation:** Effectively isolated critical components, demonstrating improved security through controlled communication paths.
- **Identity and Access Management:** Highlighted the need for stronger authentication methods to prevent unauthorized access.
- **Cybersecurity Event Logs and Monitoring:** Successfully captured and logged security events, although further refinement is required for identifying critical systems.
- **System Protection:** Emphasized the challenges in protecting legacy systems and the need for additional security layers to counteract inherent vulnerabilities in protocols like Modbus.

## Conclusion

The case study demonstrates that while the OTCC controls provide a foundational approach to enhancing cybersecurity in ICS environments, there is a need for more detailed guidance specific to ICS. The insights gained underscore the importance of continuous improvement and adaptation of cybersecurity strategies in response to evolving threats.

## Files in this Repository

- **NCA_OTCC.xlsx:** Contains all OTCC controls in spreadsheet format.
- **OTCC Controls3.drawio.png:** Visual representation of the virtual ICS environment.
- **openplc_config.xml:** Sample configuration file for the OpenPLC used in the ICS setup.

## Contributing

We welcome contributions to enhance the implementation and evaluation of OTCC controls. Potential areas for further contributions include:

- Improving the virtual ICS lab setup with more realistic scenarios.
- Expanding the range of controls tested and analyzed.
- Developing detailed guidelines for specific OT environments.

Please feel free to submit issues or pull requests with suggestions and improvements.

---

Thank you for your interest in this project. For any questions or further information, please contact [Your Name](mailto:your-email@example.com).
