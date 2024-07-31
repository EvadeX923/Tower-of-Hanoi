import sys
from Stack import Stack

def delimiter_check(filename):
    match = {'(':')',  '[':']', '{':'}'}
    s = Stack()
    with open(filename) as f:
        stuff = f.read()
    for char in stuff:
        if char in match.keys():
            s.push(char)
        elif char in match.values():
            if match[s.peek()] != char:
                return False
            s.pop()
    return True
  

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python Delimiter_Check.py file_to_check.py')
    else:
        if delimiter_check(sys.argv[1]):
            print('The file contains balanced delimiters.')
        else:
            print('The file contains IMBALANCED DELIMITERS.')


