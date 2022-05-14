import sys

class Example:
    def __init__(self, text):
        self.text = text

    def printme(self):
        print(self.text)

def main():
    in_ = input("Enter the text : ")
    ex = Example(text=in_)
    #sys.stdout = open("new.txt", "w")
    ex.printme()
    #sys.stdout.close()

if __name__ == '__main__':
    main()


"""
from contextlib import redirect_stdout

with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        print('it now prints to `help.text`')
"""

"""
or just use
$ python file_name.py > log_file.txt
"""
