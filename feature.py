#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, os.path, numpy, caffe
#import sys, os, os.path, numpy as np, caffe


#MEAN_FILE = 'python/caffe/imagenet/ilsvrc_2012_mean.npy'
#MODEL_FILE = 'examples/imagenet/imagenet_feature.prototxt'
#PRETRAINED = 'examples/imagenet/caffe_reference_imagenet_model'
#MEAN_FILE  = os.path.join(CAFFE_DIR, '/home/nmiyake/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy')
#MODEL_FILE = os.path.join(CAFFE_DIR, '/home/nmiyake/caffe/models/bvlc_reference_caffenet/deploy.prototxt')
#PRETRAINED = os.path.join(CAFFE_DIR, '/home/nmiyake/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel')
MEAN_FILE  = '/home/nmiyake/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy'
MODEL_FILE = '/home/nmiyake/caffe/models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = '/home/nmiyake/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'

#LAYER = 'fc6wi'
#LAYER = 'fc7'
LAYER = 'fc8'
INDEX = 4

net = caffe.Classifier(MODEL_FILE, PRETRAINED)
#caffe.set_phase_test()
caffe.set_mode_cpu()
net.transformer.set_mean('data', numpy.load(MEAN_FILE))
net.transformer.set_raw_scale('data', 255)
net.transformer.set_channel_swap('data', (2,1,0))

image = caffe.io.load_image(sys.argv[1])
net.predict([ image ])
feat = net.blobs[LAYER].data[INDEX].flatten().tolist()
#print(' '.join(map(str, feat)))

formatted_feat_array = [str(index+1)+':'+str(f_i) for index, f_i in enumerate(feat)]
print str(1) + " " + " ".join(formatted_feat_array)

