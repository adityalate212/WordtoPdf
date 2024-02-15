import os
import sys
from docx2pdf import convert

# Get the input file path from the command-line argument
input_file = sys.argv[1]

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f'Error: File {input_file} does not exist')
    sys.exit()

# Check if the input file is a Word file
if not input_file.lower().endswith('.docx'):
    print(f'Error: Only Word files can be converted to PDF')
    sys.exit()

# Convert the input file to PDF
try:
    convert(input_file)
    print('File converted successfully')
except Exception as e:
    print(f'Error: {e}')
