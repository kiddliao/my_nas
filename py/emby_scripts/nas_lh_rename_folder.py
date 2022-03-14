import shutil
import platform
import os
import glob
import sys

if platform.system() == 'Linux':
    input_dir = sys.argv[1]
    log_path = sys.argv[2]
else:
    input_dir = r'Y:'
    log_path = r'py\emby_scripts\test\test.txt'

actors_dirs = glob.glob(os.path.join(input_dir, '*', '*16466*')) + \
    glob.glob(os.path.join(input_dir, '*', '*', '*16466*'))
actors_dirs = list(filter(lambda x: os.path.isdir(x), actors_dirs))
for v in actors_dirs:
    print(v)
print(len(actors_dirs))

f = open(log_path, 'w', encoding='utf-8')
for i, actors_dir in enumerate(actors_dirs):
    if actors_dir[-1].isdigit():
        new_path = actors_dir.split('16466')[0]
        if new_path in actors_dir:
            # shutil.move(actors_dir, new_path)
            res = f'{i + 1}/{len(actors_dirs)} rename folder {os.path.basename(actors_dir)} as {os.path.basename(new_path)}'
            
        else:
            res = f'{i + 1}/{len(actors_dirs)} dont rename {os.path.basename(actors_dir)}'
    else:
        res = f'{i + 1}/{len(actors_dirs)} dont rename {os.path.basename(actors_dir)}'
    print(res)
    f.write(res + '\n')

f.close()
