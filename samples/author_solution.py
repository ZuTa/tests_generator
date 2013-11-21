import sys

def main():
    f = sys.stdin

    a,b = map(int, f.readline().strip().split())

    print a + b

if __name__ == '__main__':
    main()
