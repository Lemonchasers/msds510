#2

import sys

input1 = sys.argv[1]
output2 = sys.argv[2]

def main(input1,output2):
    """The main function within this file converts csv to a utf8 csv file.
    It takes two arguments, the file directory that needs to be converted and the file
    directory to output the file."""
    with open(input1,'rb') as a:
        avengers = a.read()

    avengers_decoded = avengers.decode('iso-8859-1')
    avengers_encoded = avengers_decoded.encode('utf8')

    with open(output2, 'wb') as b:
        b.write(avengers_encoded)

    print(output2)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
