import sys


def main():
    if len(sys.argv) < 2:
        try:
            while True:
                print(input())
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
    else:
        for filename in sys.argv[1:]:
            try:
                with open(filename) as f:
                    print(f.read())
            except FileNotFoundError:
                print("cat: %s: No such file or directory" % filename, file=sys.stderr)
            except IsADirectoryError:
                print("cat: %s: Is a directory" % filename, file=sys.stderr)
