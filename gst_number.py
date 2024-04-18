import csv

# Taxpayer types list
taxpayer_types = [
    "Normal",
    "Composite",
    "Casual",
    "Input Service Distributon",
    "Tax Collector",
    "Tax Deductor",
    "Nonresident Foreign Taxpayers (NRI)",
    "UN Bodies, Embassies, etc.",
    "Other Notified Persons",
    "Tax Return Preparer",
    "Temporary ID"
]

# Function to determine taxpayer type based on GST number
def determine_taxpayer_type(gst_number):
    # Example: Replace this with your logic to determine taxpayer type
    if gst_number.startswith("18"):
        return "Normal"
    elif gst_number.startswith("13"):
        return "Composite"
    elif gst_number.startswith("24"):
        return "Casual"
    else:
        return "Unknown"

# Function to read GSTIN numbers from input CSV and determine taxpayer type
def read_gstin_and_determine_type(input_file, output_file):
    with open(input_file, mode='r') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header
        gstin_numbers = [row[0] for row in reader]

    gstin_data = []
    for gstin in gstin_numbers:
        taxpayer_type = determine_taxpayer_type(gstin)
        gstin_data.append((gstin, taxpayer_type))

    # Write GSTIN numbers along with taxpayer types to output CSV file
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['GSTIN', 'Taxpayer Type'])
        writer.writerows(gstin_data)

# Input and output file paths
input_file = 'output.csv'
output_file = 'output_with_types.csv'

# Read GSTIN numbers, determine taxpayer types, and write to output CSV
read_gstin_and_determine_type(input_file, output_file)
