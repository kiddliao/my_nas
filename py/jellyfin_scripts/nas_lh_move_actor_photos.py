import shutil
import platform
import os
import glob

if platform.system() == 'Linux':
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
else:
    input_dir = r'Y:'
    output_dir = r'\\10.168.1.119\docker\jellyfin_latest\metadata\People'

actors_dir = glob.glob(os.path.join(input_dir, '*', '*', '.actors', '*')) + \
             glob.glob(os.path.join(input_dir, '*', '*', '*', '.actors', '*'))
path_dict = {}

for i, image_path in enumerate(actors_dir):
    print(f'{i + 1}/{len(actors_dir)}')
    image_name = os.path.basename(image_path)
    output_dir_name = os.path.join(output_dir, image_name[0], image_name.split('.')[0])
    os.makedirs(output_dir_name, exist_ok=True)
    
    if output_dir_name not in path_dict:
        path_dict[output_dir_name] = []
    path_dict[output_dir_name].append(image_path)

for i, output_dir_name in enumerate(path_dict.keys()):
    image_paths = path_dict[output_dir_name]
    print(f'{i + 1}/{len(path_dict)}', end=' ')
    for j, image_path in enumerate(image_paths):
        if j == 0:
            dst_path = os.path.join(output_dir_name, 'folder.jpg')
            shutil.copy(image_path, dst_path)
            print(f"移动图片{image_path}到{dst_path}")
        else:
            dst_path = os.path.join(output_dir_name, f'folder_{j + 1}.jpg')
            shutil.copy(image_path, dst_path)
            print(f"移动图片{image_path}到{dst_path}")
