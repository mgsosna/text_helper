# Load libraries
from nlp_functions import read_str
import argparse

# Create a help message and define arguments for parser
parser = argparse.ArgumentParser(description = 'Summarize inputted string')
required_args = parser.add_argument_group('required arguments')
required_args.add_argument('-i', help='Input string', required=True)
parser.add_argument("-n", help="Number of lemmas to return (default = 3)", default=3)

# Load arguments into args variable
args = parser.parse_args()

# Call read_str function
read_str(args.i, int(args.n))
