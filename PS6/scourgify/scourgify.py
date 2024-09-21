import csv
import sys

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Open the input CSV file
        with open(input_file, newline='') as infile:
            reader = csv.DictReader(infile)
            
            # Open the output CSV file
            with open(output_file, 'w', newline='') as outfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                
                # Write the header
                writer.writeheader()
                
                # Read each row from the input and process the name
                for row in reader:
                    try:
                        first, last = row['name'].split()
                        writer.writerow({'first': first, 'last': last, 'house': row['house']})
                    except ValueError:
                        sys.exit("Error: Name does not have exactly two parts.")
    
    except FileNotFoundError:
        sys.exit(f"Error: Could not read file {input_file}.")

if __name__ == "__main__":
    main()
