# coding: utf-8
import sys

def main(av):
    """ Main program """
    file = open('token', 'r') 
    res = ""
    for i,c in enumerate(file.read()):
        res += chr(ord(c) - i)
    print(res)
    return 0

if __name__ == "__main__":
    main(sys.argv)