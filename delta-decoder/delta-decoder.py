import sys, getopt
from conversor import Conversor


short_options = "hi:"
long_options = ["help", "input="]

# Default address
conv_val = "1001"

# Get command-line arguments
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]


try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-h", "--help"):
        print("\nDigital Address conversor for Marklin Delta decoders with 4 or 8 DIP-switches.\n\nOptions:\n\t -i, --input= \t The digital address or DIP switch configuration to convert.\n\t -h, --help \t Displays this help and exits.")
        quit()
    elif current_argument in ("-i", "--input"):
        conv_val = current_value

print(Conversor().convert(conv_val))
