"""
This is the nice solution, but in an interview prioritize solving the problem as fast as possible!
"""

import sys
import os

LIMIT = 50


def validate_arguments() -> bool:
    """ Returns True if arguments are valid. """
    if len(sys.argv) != 3:
        return False
    try:
        num = int(sys.argv[1])
        if num > LIMIT:
            return False
    except ValueError:
        return False
    if not os.path.exists(sys.argv[2]):
        return False
    return True


def count_lines(path: str) -> int:
    """ Return total number of lines in log file. """
    count = 0
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            count += 1
    return count


def display_lines(n: int, path: str) -> None:
    """
    Count how many lines the log has.
    Display last n.
    """
    #with open(path, 'r') as file:
    #    print(file.read())#TMP
    num_lines = count_lines(path)
    #print(f"{num_lines = }")#TMP
    if num_lines < 1:
        sys.exit("Either empty file or there was an error reading from the file. ")
    with open(path, 'r') as file:
        while num_lines:
            line = file.readline()
            if not line:
                break
            if num_lines <= n:
                print(line, end='')
            num_lines -= 1


def main() -> None:
    """
    Read & display n bottom lines from path file, one line at a time.
    """
    if not validate_arguments():
        sys.exit(f"This script expects: N (int <= {LIMIT}), and path/to/logfile. ")
    n = int(sys.argv[1])
    path = sys.argv[2]
    #print(f"Read {n} lines from bottom of {path} file!")#TMP
    display_lines(n, path)


if __name__ == '__main__':
    main()

