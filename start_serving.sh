docker run -p 8501:8501 --mount type=bind,source=/root/mnist/saved,target=/models/saved -e MODEL_NAME=saved -t tensorflow/serving:2.1.0-rc1
