import glob
import brotli
import pathlib
import numpy

def process(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        compressed = brotli.compress(data, brotli.MODE_GENERIC, 11, 22, 0)
        new_name = 'dest-img/' + filename[11:] + '.br'
        new_path = pathlib.Path(new_name)
        new_path.parent.mkdir(parents=True, exist_ok=True)
        with open(new_name, 'wb') as f:
            f.write(compressed)

        print(filename, len(data), len(compressed), len(compressed) / len(data))
        return len(data) / len(compressed)

stats = { 'png': [], 'jpg': [] }

for filename in glob.glob('source-img/**/*.jpg', recursive=True):
    res = process(filename)
    stats['jpg'].append(res)

for filename in glob.glob('source-img/**/*.jpeg', recursive=True):
    res = process(filename)
    stats['jpg'].append(res)

for filename in glob.glob('source-img/**/*.png', recursive=True):
    res = process(filename)
    stats['png'].append(res)

for key in stats:
    print(key, 'Max', numpy.max(stats[key]))
    print(key, 'Avg', numpy.mean(stats[key]))
    print(key, 'Med', numpy.median(stats[key]))
    print(key, 'Min', numpy.min(stats[key]))