

# Mitigation Techniques CLI

This program reads a list of mitigation IDs from a CSV file, finds the related techniques from the MITRE ATT&CK data, and saves the results to another CSV file.

## Requirements

- Python 3
- `pandas` library
- `mitreattack` library

.

## How to Use

1. **Prepare your files:**
   - `Mitigation_List.csv`: This file should have a list of mitigation IDs. Example: `M0817,M0931,M0926,M0801,M0804,M0936,M0949,M0951`
   - `enterprise-attack.json`: This is the MITRE ATT&CK data file. You can download it from the MITRE website.

2. **Run the script:**

```sh
python mitigation_techniques_cli.py /path/to/Mitigation_List.csv /path/to/output/Mitigation_Techniques.csv /path/to/enterprise-attack.json
```

Replace `/path/to/Mitigation_List.csv`, `/path/to/output/Mitigation_Techniques.csv`, and `/path/to/enterprise-attack.json` with the actual paths to your files.

## Arguments

- `input_csv`: The path to your input CSV file that contains the list of mitigation IDs.
- `output_csv`: The path where you want the output CSV file to be saved.
- `attack_json`: The path to the MITRE ATT&CK data JSON file.

## Example

```sh
python mitigation_techniques_cli.py Mitigation_List.csv Mitigation_Techniques.csv enterprise-attack.json
```

This command will read the `Mitigation_List.csv` file, find the techniques related to each mitigation ID, and save the results to `Mitigation_Techniques.csv`.

## Contact

If you have any questions, please ask for help.
```

This `README.md` should be easy to understand for someone who is not a native English speaker. If you need any changes or additional information, feel free to ask!
