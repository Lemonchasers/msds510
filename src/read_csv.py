#3a
import sys

input1 = sys.argv[1]

def main(input1):
    """The main function within this file takes a csv and reads it into rows.
    The function takes one argument, the directory of the csv file."""
    with open(input1,'r') as c:
        rows = c.readlines()

    print(rows[161])

if __name__ == '__main__':
    main(sys.argv[1])
