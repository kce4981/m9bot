import pathlib

root = pathlib.Path(__file__).absolute().parents[1]
data = root / 'data'

if __name__ == '__main__':
    print(root, data)