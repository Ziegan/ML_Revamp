import os
from cProfile import label

os.environ["CUDA_VISIBLE_DEVICES"] = ""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

##DATASET
dataset = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = dataset.load_data()
class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

print(
    f"SHAPE OF THE TRAIN IMAGE AND TOTAL LABELS: {train_images.shape}, {len(train_labels)}"
)
print(
    f"SHAPE OF THE TEST IMAGE AND TOTAL LABELS: {test_images.shape}, {len(test_labels)}"
)

class_dict = dict(zip(set(train_labels), class_names))
print("CLASSES:")
for key, val in class_dict.items():
    print(f"{key} == {val}")

plt.imshow(train_images[0])
plt.title(class_dict[train_labels[0]])
plt.show()

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i])
    plt.xlabel(class_names[train_labels[i]])
plt.show()

##SCALING THE INPUT IMAGES
train_images = train_images / 255.0
test_images = test_images / 255.0

##MODEL BUILDING
