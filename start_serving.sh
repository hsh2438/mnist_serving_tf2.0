docker run -p 8501:8501 --mount type=bind,source=$PWD/mnist,target=/models/mnist -e MODEL_NAME=mnist -td tensorflow/serving:2.1.0-rc1
