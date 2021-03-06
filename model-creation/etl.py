from glob import glob
from pathlib import Path
from PIL import Image


def get_image_names(img_directory, labels):
    img_names = [
        path.split('\\')[-1] for path in glob(f'{img_directory}/*.ppm') if path.split('\\')[-1] in labels
    ]
    return img_names



if __name__ == '__main__':
    new_smile_dir = 'data/transformed/smile'
    new_non_smile_dir ='data/transformed/non_smile'
    test_dir = 'data/transformed/test'
    Path(new_smile_dir).mkdir(parents=True, exist_ok=True)
    Path(new_non_smile_dir).mkdir(parents=True, exist_ok=True)
    Path(test_dir).mkdir(parents=True, exist_ok=True)

    with open('data/labels/SMILE_list.txt') as f:
        smile_labels = f.read().split('\n')
        smile_labels = [label.replace('.jpg', '.ppm') for label in smile_labels]

    with open('data/labels/NON-SMILE_list.txt') as f:
        non_smile_labels = f.read().split('\n')
        non_smile_labels = [label.replace('.jpg', '.ppm') for label in non_smile_labels]

    original_dir = 'data/images/faces'
    smile_image_names = get_image_names(original_dir, smile_labels)
    non_smile_image_names = get_image_names(original_dir, non_smile_labels)
    
    test_image_names = [
        path.split('\\')[-1] for path in glob(f'{original_dir}/*.ppm') 
        if path.split('\\')[-1] not in smile_labels + non_smile_labels
    ]

    for name in smile_image_names:
        im = Image.open(f"{original_dir}/{name}")
        im.save(f"{new_smile_dir}/{name.replace('.ppm', '.jpg')}")
    for name in non_smile_image_names:
        im = Image.open(f"{original_dir}/{name}")
        im.save(f"{new_non_smile_dir}/{name.replace('.ppm', '.jpg')}")

    for name in test_image_names:
        im = Image.open(f"{original_dir}/{name}")
        im.save(f"{test_dir}/{name.replace('.ppm', '.jpg')}")