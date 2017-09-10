# this does nothing
from time import sleep


def runforever():
    while True:
        print("test")
        sleep(1)


def main():
    runforever()


if __name__ == '__main__':
    main()