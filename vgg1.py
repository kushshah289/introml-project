import numpy as np
import tensorflow as tf
import download
import os

url = "https://s3.amazonaws.com/cadl/models/vgg16.tfmodel"


path_graph = "vgg16.tfmodel"



#def mdownload():
 #   print("Downloading VGG16 Params ...")
  #  download.weights_download(url=url) 


class VGG16:
    
    tensor_name_input_image = "images:0"

    tensor_name_dropout = 'dropout/random_uniform:0'
    tensor_name_dropout1 = 'dropout_1/random_uniform:0'

    
    lnames = ['conv1_1/conv1_1', 'conv1_2/conv1_2',
                   'conv2_1/conv2_1', 'conv2_2/conv2_2',
                   'conv3_1/conv3_1', 'conv3_2/conv3_2', 'conv3_3/conv3_3',
                   'conv4_1/conv4_1', 'conv4_2/conv4_2', 'conv4_3/conv4_3',
                   'conv5_1/conv5_1', 'conv5_2/conv5_2', 'conv5_3/conv5_3']

    def __init__(self):
        self.graph = tf.Graph()

        with self.graph.as_default():

            with tf.gfile.FastGFile(path_graph, 'rb') as file:
                graph_def = tf.GraphDef()

                graph_def.ParseFromString(file.read())

                tf.import_graph_def(graph_def, name='')

            self.input = self.graph.get_tensor_by_name(self.tensor_name_input_image)

            self.ltensors = [self.graph.get_tensor_by_name(name + ":0") for name in self.lnames]

    def get_layer_tensors(self, ids):
        return [self.ltensors[idx] for idx in ids]

    def get_lnames(self, ids):
        return [self.lnames[idx] for idx in ids]

    def create_feed_dict(self, image):
        image = np.expand_dims(image, axis=0)
        feed_dict = {self.tensor_name_input_image: image}

        return feed_dict
