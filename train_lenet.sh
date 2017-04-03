#!/usr/bin/env sh
set -e

#./build/tools/caffe train --solver=examples/mnist/lenet_solver.prototxt $@
../../build/tools/caffe train --solver=lenet_solver.prototxt $@ 
