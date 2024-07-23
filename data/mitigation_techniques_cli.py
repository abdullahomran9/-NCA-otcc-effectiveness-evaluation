import csv
import pandas as pd
import argparse
from mitreattack.stix20 import MitreAttackData

def get_techniques_by_mitigation(mitigation_id, mitre_attack_data):
    mitigations = mitre_attack_data.get_mitigations()
    mitigation = next((m for m in mitigations if m.external_references[0]['external_id'] == mitigation_id), None)
    if mitigation:
        mitigation_stix_id = mitigation.id
        mitigation_name = mitigation.name
        techniques = mitre_attack_data.get_techniques_mitigated_by_mitigation(mitigation_stix_id)
        return [(mitigation_id, mitigation_name, mitre_attack_data.get_attack_id(tech['object'].id), tech['object'].name) for tech in techniques]
    return []

def main(input_csv, output_csv, attack_json):
    # Initialize MitreAttackData with the path to the MITRE ATT&CK data file
    mitre_attack_data = MitreAttackData(attack_json)

    # Read the list of mitigation IDs from the CSV file
    mitigation_ids = []
    with open(input_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            mitigation_ids.extend(row)

    # Collect data for each mitigation ID
    data = []
    for mitigation_id in mitigation_ids:
        data.extend(get_techniques_by_mitigation(mitigation_id, mitre_attack_data))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["Mitigation ID", "Mitigation Name", "Technique ID", "Technique Name"])

    # Write the DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f"Data has been written to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch techniques mitigated by mitigations and save to CSV")
    parser.add_argument('input_csv', type=str, help="Path to the input CSV file with mitigation IDs")
    parser.add_argument('output_csv', type=str, help="Path to the output CSV file")
    parser.add_argument('attack_json', type=str, help="Path to the MITRE ATT&CK data JSON file")

    args = parser.parse_args()
    main(args.input_csv, args.output_csv, args.attack_json)
