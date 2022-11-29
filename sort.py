import sys
import sorting_files


def main():
    try:
        sorting_files.sort_create_files(sys.argv[1])

    except:
        pass
    else:
        print("Well Done!")


if __name__ == '__main__':
    main()
