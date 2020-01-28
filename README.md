# mnist serving example
mnist serving example using Tensorflow 2.0 & python3

### train
Training mnist with simple network and save as a saved model format
```
python3 train.py
```

### install docker
You can download docker from below.

https://docs.docker.com/install/

### serving using docker
Serving model using docker.
```
docker run -p 8501:8501 --mount type=bind,source=$PWD/mnist,target=/models/mnist -e MODEL_NAME=mnist -td tensorflow/serving:2.1.0-rc1
```

### test
You can test rest api.
```
python3 client_test.py
```

<br>
https://seokhyun2.tistory.com/39
