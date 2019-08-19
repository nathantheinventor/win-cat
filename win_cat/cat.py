import sys


def main():
    if len(sys.argv) < 2:
        try:
            sys.stdout.write(sys.stdin.read())
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        