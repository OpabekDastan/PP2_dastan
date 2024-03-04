def count_lines_using_readlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))
