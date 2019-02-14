# Load libraries
import sys
from nlp_functions import read_str

#-----------------------------------------------------------
# Possible errors
# 1. If user did not input a file, tell them to include one
if len(sys.argv) < 2:
    print("Oops - don't forget to input a text file!")
    quit()

# 2. If user inputted a file that isn't .txt, throw error
if sys.argv[1][-4:] != '.txt':
    print("Error: txt_report only supports .txt files")
    quit()

#-----------------------------------------------------------
# Load file
file = sys.argv[1]

with open(file, 'r') as f:
    text = f.read().replace('\n', '')

# Run read_str on the string
read_str(text)
