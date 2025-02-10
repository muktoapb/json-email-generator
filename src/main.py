#!/usr/bin/env python3

import json
import argparse
from pathlib import Path
from typing import List, Set, Dict

class EmailDomainManager:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.input_dir = self.base_dir / "data" / "input"
        self.output_dir = self.base_dir / "data" / "output"
        
    def read_domains_from_file(self, file_path: Path) -> Set[str]:
        """Read domains from input file, handling both quoted and unquoted formats."""
        domains = set()
        
        if not file_path.exists():
            print(f"Input file {file_path.name} not found!")
            return domains
            
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, 1):
                try:
                    # Clean the line - remove all quotes and commas
                    domain = (
                        line.strip()               # Remove whitespace
                        .replace('"', '')          # Remove double quotes
                        .replace("'", '')          # Remove single quotes
                        .rstrip(',')              # Remove trailing comma
                        .strip()                  # Remove any remaining whitespace
                    )
                    
                    # Skip empty lines or comment lines
                    if not domain or domain.startswith('#'):
                        continue
                        
                    # Basic domain validation
                    if '.' not in domain:
                        print(f"Warning: Line {line_number} in {file_path.name} doesn't look like a valid domain: {domain}")
                        continue
                        
                    # Store clean domain in lowercase
                    domains.add(domain.lower())
                except Exception as e:
                    print(f"Error processing line {line_number} in {file_path.name}: {str(e)}")
                    continue
                    
        if domains:
            print(f"Found {len(domains)} valid domains in {file_path.name}")
        else:
            print(f"No valid domains found in {file_path.name}")
            
        return domains

    def load_existing_json(self, json_path: Path) -> List[str]:
        """Load existing domains from JSON file."""
        if not json_path.exists():
            return []
            
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("domains", [])
        except json.JSONDecodeError:
            print(f"Error reading {json_path.name}. Starting fresh.")
            return []

    def save_domains_to_json(self, domains: List[str], json_path: Path, minified: bool = False) -> None:
        """Save domains to JSON file."""
        # Sort domains alphabetically
        sorted_domains = sorted(domains)
        
        # Create JSON structure
        data = {"domains": sorted_domains}
        
        # Save regular JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            if minified:
                json.dump(data, f)
            else:
                json.dump(data, f, indent=4)
        
        # Save minified version
        minified_path = json_path.parent / f"{json_path.stem}.min{json_path.suffix}"
        with open(minified_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'))
        
        print(f"Successfully saved {len(sorted_domains)} domains to:")
        print(f"- Regular: {json_path.name}")
        print(f"- Minified: {minified_path.name}")

    def process_all_files(self):
        """Process all txt files in input directory."""
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Get all txt files from input directory
        txt_files = list(self.input_dir.glob("*.txt"))
        
        if not txt_files:
            print("No .txt files found in input directory!")
            return
            
        print(f"Found {len(txt_files)} txt files to process...")
        
        for txt_file in txt_files:
            print(f"\nProcessing {txt_file.name}...")
            
            # Determine output JSON filename
            json_file = self.output_dir / f"{txt_file.stem}.json"
            
            # Read new domains
            new_domains = self.read_domains_from_file(txt_file)
            if not new_domains:
                print(f"No domains found in {txt_file.name}")
                continue

            # Load existing domains
            existing_domains = set(self.load_existing_json(json_file))
            
            # Find new unique domains
            unique_new_domains = new_domains - existing_domains
            
            if unique_new_domains:
                print(f"Found {len(unique_new_domains)} new domains in {txt_file.name}")
                # Merge and save
                all_domains = existing_domains | new_domains
                self.save_domains_to_json(list(all_domains), json_file)
            else:
                print(f"No new domains found in {txt_file.name}")

def main():
    parser = argparse.ArgumentParser(description='JSON Email Generator')
    parser.add_argument('command', choices=['make'])
    parser.add_argument('type', choices=['json'])
    
    args = parser.parse_args()
    
    if args.command == 'make' and args.type == 'json':
        manager = EmailDomainManager()
        manager.process_all_files()
    else:
        print("Invalid command. Use 'make json' to process all files")

if __name__ == "__main__":
    main()
