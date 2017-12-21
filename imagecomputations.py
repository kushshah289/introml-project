import PIL.Image
import vgg1
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from IPython.display import Image, display

def get_image(fname):
    image = PIL.Image.open(fname)
    return np.float32(image)

def plot_final_image(image):
    image = image.astype(np.uint8)

    display(PIL.Image.fromarray(image))

def plot_images(Cimage, Simage, Mimage):
    fig, axes = plt.subplots(1, 3, figsize=(10, 10))

    fig.subplots_adjust(hspace=0.1, wspace=0.1)

    ax = axes.flat[0]
    ax.imshow(Cimage/255.0)
    ax.set_xlabel("Content Image")
    
    ax = axes.flat[2]
    ax.imshow(Simage/255.0)
    ax.set_xlabel("Style Image")


    ax = axes.flat[1]
    ax.imshow(Mimage/255.0)
    ax.set_xlabel("Output Image")

    
    for ax in axes.flat:
        ax.set_xticks([])
        ax.set_yticks([])
    
    plt.show()