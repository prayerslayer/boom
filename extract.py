import argparse
from zipfile import ZipFile

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('file', metavar='file', type=str,
                    help='File')

args = parser.parse_args()
with ZipFile(args.file) as z:
    print(z.infolist())
    z.extractall()

