import def_sort


def main():
    sort_path = input("Enter path to directory to sort: ")
    try:
        def_sort.sort_create_files(sort_path)
    except:
        pass
    else:
        print("Well Done!")


if __name__ == '__main__':
    main()
