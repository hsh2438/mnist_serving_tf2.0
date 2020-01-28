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
sh start_serving.sh
```

### test
You can test rest api.
```
python3 client_test.py
```
