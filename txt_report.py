# Load libraries
from nlp_functions import read_str
import argparse

# Create a help message and define arguments for parser
parser = argparse.ArgumentParser(description = 'Summarize inputted text file')
required_args = parser.add_argument_group('required arguments')
required_args.add_argument('-i', help='Input string', required=True)
parser.add_argument("-n", help="Number of lemmas to return (default = 3)", default=3)

# Load arguments into args variable
args = parser.parse_args()

#-----------------------------------------------------------
# If user inputted a file that isn't .txt, throw error
if args.i[-4:] != '.txt':
    print("Error: txt_report only supports .txt files")
    quit()

#-----------------------------------------------------------
# Load file
with open(args.i, 'r') as f:
    text = f.read().replace('\n', '')

# Run read_str on the string
read_str(text, int(args.n))
