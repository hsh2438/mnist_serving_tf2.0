# mnist serving example
mnist serving example using Tensorflow 2.0 & python3

### train
Training mnist with simple network and save as a saved model format
```
python train.py
```

### serving using docker
You should have docker to use this example.
```
sh start_serving.sh
```

### test
You can test rest api.
```
python client_test.py
```
