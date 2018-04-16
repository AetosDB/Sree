def hello():
    print("Hello world")
    import sys
    print(sys.modules.keys())


def main():
    hello()


if __name__ == '__main__':
    main()
