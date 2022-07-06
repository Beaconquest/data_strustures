# main.py
# file to use and test the stack

from stack import Stack


def main():
    s = Stack()

    s.push("First")
    s.push("Second")
    print(s)
    s.pop()
    print(s)
    s.pop()
    s.push('Third')
    s.peek()
    print(s)
    print(s.size())
    print(s.is_empty())
    s.is_empty()
    s.pop()
    s.pop()

if __name__ == '__main__':
    main()