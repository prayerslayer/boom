import epicbox
import sys
import os

epicbox.configure(
    profiles=[
        epicbox.Profile('python', 'python:3.6.5-alpine')
    ]
)
DIR = os.path.dirname(__file__)
VERY_HIGH_VALUE = 50_000_000
with open(f'{DIR}/bomb.zip', 'rb') as bomb:
    with open(f'{DIR}/extract.py', 'rb') as code:
        files = [{'name': 'archive.zip', 'content': bomb.read()}, {'name': 'extract.py', 'content': code.read()}]
        limits = {'memory': 128, 'realtime': VERY_HIGH_VALUE, 'cputime': VERY_HIGH_VALUE, 'file_size': 1024 * 1024}
        result = epicbox.run('python', 'python3 extract.py archive.zip', files=files, limits=limits)
        print(result)
        sys.exit(result['exit_code'])
