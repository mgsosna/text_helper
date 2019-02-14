# Load libraries
import sys
from nlp_functions import read_str

# If user doesn't input anything, tell them to write something
if len(sys.argv) < 2:
    print("Oops - don't forget to input some text!")
    quit()

# Call read_str function
read_str(sys.argv[1])
