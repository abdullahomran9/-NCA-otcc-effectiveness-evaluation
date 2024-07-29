# ICS Cybersecurity Standards Mapping to MITRE ATT&CK

This repository contains mappings of industrial control system (ICS) cybersecurity standards to the MITRE ATT&CK for ICS framework. The mapped standards are:

- NIST SP 800-82
- IEC 62443
- NCA OTCC (Saudi National Cybersecurity Authority Operational Technology Cybersecurity Controls)

## Contents

- Heat map visualizations (PNG images)
- MITRE Navigator layer files (JSON)
- STIX mapping files (JSON)

### Heat Maps

The heat maps visually represent the coverage of each standard across the MITRE ATT&CK for ICS tactics and techniques:

- `NIST_heatmap.png`
- `IEC62443_heatmap.png`
- `NCA_OTCC_heatmap.png`

These images provide a quick overview of which areas of the ATT&CK framework are addressed by each standard.

### MITRE Navigator Layers

The following JSON files can be imported into the MITRE ATT&CK Navigator tool to interactively explore the mappings:

- `NIST_navigator_layer.json`
- `IEC62443_navigator_layer.json`
- `NCA_OTCC_navigator_layer.json`

To use these files:
1. Go to [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
2. Click "Open Existing Layer"
3. Select "Upload from Local" and choose one of these JSON files

### STIX Mapping Files

These files contain the detailed mappings in STIX format, which can be imported into the MITRE ATT&CK Workbench or other compatible tools:

- `NIST_STIX_mapping.json`
- `IEC62443_STIX_mapping.json`
- `NCA_OTCC_STIX_mapping.json`

## Usage

These mappings can be used to:

- Compare coverage of different ICS cybersecurity standards
- Identify gaps in security controls
- Align security practices with the MITRE ATT&CK for ICS framework
- Enhance threat modeling and risk assessment for ICS environments

## Contributing

Contributions to improve or expand these mappings are welcome. Please submit a pull request with your proposed changes.


## Acknowledgements

This work builds upon the MITRE ATT&CK for ICS framework and the referenced cybersecurity standards. We acknowledge the efforts of these organizations in developing these valuable resources for the ICS security community.
