from __future__ import print_function

import sys
import argparse

if sys.version_info[0] == 2:
    # Python 2
    FileNotFoundError = IOError

NUMBER_ALL = 1
NUMBER_NONBLANK = 2

parser = argparse.ArgumentParser(prog="cat", description="Concatenate FILE(s) to standard output.\n\nWith no FILE or when FILE is -, read standard input.")
parser.add_argument("files", metavar="FILE", type=str, nargs="*", help="A file to print or - for standard input")
parser.add_argument("-A", "--show-all", action="store_true", help="equivalent to -vET") #
parser.add_argument("-b", "--number-nonblank", action="store_true", help="number nonempty output lines, overrides -n") #
parser.add_argument("-e", action="store_true", help="equivalent to -vE") #
parser.add_argument("-E", "--show-ends", action="store_true", help="display $ at the end of each line") #
parser.add_argument("-n", "--number", action="store_true", help="number all output lines") #
parser.add_argument("-s", "--squeeze-blank", action="store_true", help="suppress repeated empty output lines")
parser.add_argument("-t", action="store_true", help="equivalent to -vT") #
parser.add_argument("-T", "--show-tabs", action="store_true", help="display TAB character as ^I") #
parser.add_argument("-u", action="store_true", help="(ignored)") #
parser.add_argument("-v", "--show-nonprinting", action="store_true", help="use ^ and M- notation, except for LFD and TAB") #
parser.add_argument('-vE', action="store_true", help=argparse.SUPPRESS)
parser.add_argument('-vT', action="store_true", help=argparse.SUPPRESS)
parser.add_argument('-vET', action="store_true", help=argparse.SUPPRESS)


replacements = {}
numbering = None

def v_replacements():
    for i in range(9):
        replacements[i] = "^" + chr(i + 64)
    for i in range(11, 32):
        replacements[i] = "^" + chr(i + 64)
    for i in range(128, 160):
        replacements[i] = "M-^" + chr(i - 64)
    for i in range(160, 255):
        replacements[i] = "M-" + chr(i - 128)
    replacements[255] = "M-^?"

def get_replacements(args):
    global numbering
    # Set the replacement characters
    if args.show_all or args.vET:
        v_replacements()
        replacements[10] = "$\n"
        replacements[9] = "^I"
    if args.e or args.vE:
        v_replacements()
        replacements[10] = "$\n"
    if args.show_ends:
        replacements[10] = "$\n"
    if args.t or args.vT:
        v_replacements()
        replacements[9] = "^I"
    if args.show_tabs:
        replacements[9] = "^I"
    if args.show_nonprinting:
        v_replacements()
    
    # Set the numbering scheme
    if args.number_nonblank:
        numbering = NUMBER_NONBLANK
    elif args.number:
        numbering = NUMBER_ALL


def display_data(data):
    output = ""
    for c in data:
        if ord(c) in replacements:
            output += replacements[ord(c)]
        else:
            output += c
    sys.stdout.write(output)

def main():
    args = parser.parse_args()
    get_replacements(args)

    if len(args.files) == 0:
        try:
            while True:
                c = sys.stdin.read(1)
                if c == "":
                    sys.exit(0)
                display_data(c + sys.stdin.readline())
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
    else:
        for filename in args.files:
            if filename == "-":
                try:
                    while True:
                        c = sys.stdin.read(1)
                        if c == "":
                            sys.exit(0)
                        display_data(c + sys.stdin.readline())
                except KeyboardInterrupt:
                    sys.exit(0)
                except EOFError:
                    sys.exit(0)
            else:
                try:
                    with open(filename, "rb") as f:
                        display_data(f.read())
                except FileNotFoundError:
                    print("cat: %s: No such file or directory" % filename, file=sys.stderr)
                except IsADirectoryError:
                    print("cat: %s: Is a directory" % filename, file=sys.stderr)


if __name__ == "__main__":
    main()
