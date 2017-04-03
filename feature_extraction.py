#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, os.path, numpy as np, caffe

# path to git-cloned caffe dir
CAFFE_DIR  = os.getenv('CAFFE_ROOT')

MEAN_FILE  = os.path.join(CAFFE_DIR, '/home/nmiyake/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy')
MODEL_FILE = os.path.join(CAFFE_DIR, '/home/nmiyake/caffe/models/bvlc_reference_caffenet/deploy.prototxt')
PRETRAINED = os.path.join(CAFFE_DIR, '/home/nmiyake/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel')

LAYER = 'fc7'
INDEX = 4

class FeatureExtraction:

    def __init__(self):
        net = caffe.Classifier(MODEL_FILE, PRETRAINED)
        caffe.set_mode_cpu()
        net.transformer.set_mean('data', np.load(MEAN_FILE))
        net.transformer.set_raw_scale('data', 255)
        net.transformer.set_channel_swap('data', (2,1,0))
        self.net = net

    def extract_features(self):
        imageDirPath = sys.argv[1]
        previousLabelName = ''
        labelIntValue = 0
        for root, dirs, files in os.walk(imageDirPath):
            for filename in files:
                if filename == '.DS_Store': 
                    continue
                fullPath  = os.path.join(root, filename)
                dirname   = os.path.dirname(fullPath)
                labelName = dirname.split("/")[-1]
                if labelName != previousLabelName:
                    labelIntValue += 1
                    previousLabelName = labelName
                image = caffe.io.load_image(fullPath)
                feat = self.extract_features_from_image(image)
                self.print_feature_with_libsvm_format(labelIntValue, feat)

    def build_test_data(self, imagePaths):
        for fullPath in imagePaths:
            image = caffe.io.load_image(fullPath)
            feat = self.extract_features_from_image(image)
            self.print_feature_with_libsvm_format(-1, feat)

    def extract_features_from_image(self, image):
        self.net.predict([image])
        feat = self.net.blobs[LAYER].data[INDEX].flatten().tolist()
        return feat 

    def print_feature_with_libsvm_format(self, labelIntValue, feat):
        formatted_feat_array = [str(index+1)+':'+str(f_i) for index, f_i in enumerate(feat)]
        print str(labelIntValue) + " " + " ".join(formatted_feat_array)

