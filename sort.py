import sys
import sorting_files


def main():
    try:
        sorting_files.sort_create_files(sys.argv[1])

    except (IndexError, FileNotFoundError):
        print("Please input correct path to sort folder")
        pass


if __name__ == '__main__':
    main()
