import os
from pathlib import Path

def main():

    file_path = os.path.join('file_paths', 'rando-file.txt')
    # Option 1 - os.path.getsize()
    # file_size = os.path.getsize(file_path)
    # Option 2 - os.stat().st_size
    # file_size = os.stat(file_path).st_size
    # Option 3 - pathlib.Path.stat().st_size
    file_size = Path(file_path).stat().st_size
    with open(file_path, 'r') as file:
        print(file.read())
    print(f'Size of {file_path} (In Bytes) = {file_size}')

if __name__ == '__main__':
    main()