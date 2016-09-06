import os
import re

PATTERN = re.compile(r'.+(?:Тайо\W+?|машинки\.) +(?P<title>.*?)\.*? Серия (?P<ep>\d{1,})')

def replace(string):
    name = re.search(PATTERN, string).groupdict()
    return '{:02d} {}.mp4'.format(int(name['ep']), name['title'])

if __name__ == '__main__':
    os.chdir('d:/temp')
    _, _, files = list(os.walk('.')).pop()

    for f in files:
        os.rename(f, replace(f))
