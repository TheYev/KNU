import random
import os

images_path = 'data/images'
labels_path = 'data/labels'

images = os.listdir(images_path)
labels = os.listdir(labels_path)

images.sort()
labels.sort()

random.seed(42)
random.shuffle(images)

split = int(0.8 * len(images))

train_labels = labels[:split]
test_labels = labels[split:]

train_images = [i.replace('.txt', '.jpg') for i in train_labels]
test_images = [i.replace('.txt', '.jpg') for i in test_labels]

import shutil


os.makedirs('data/train/images', exist_ok=True)
os.makedirs('data/train/labels', exist_ok=True)
os.makedirs('data/valid/images', exist_ok=True)
os.makedirs('data/valid/labels', exist_ok=True)

for image in train_images:
    shutil.copy(os.path.join(images_path, image), os.path.join('data/train/images', image))

for image in test_images:
    shutil.copy(os.path.join(images_path, image), os.path.join('data/valid/images', image))

for label in train_labels:
    shutil.copy(os.path.join(labels_path, label), os.path.join('data/train/labels', label))

for label in test_labels:
    shutil.copy(os.path.join(labels_path, label), os.path.join('data/valid/labels', label))