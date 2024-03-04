import os

def list_dir_files(path):
    all_items = os.listdir(path)
    dirs = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", dirs)
    print("Files:", files)
    print("All Items:", all_items)