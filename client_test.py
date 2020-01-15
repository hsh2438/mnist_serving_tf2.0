import json
import requests
from PIL import Image
import numpy as np

test_image = Image.open('test_image.jpg')
pixels = np.array(test_image)/255.0

address = 'http://localhost:8501/v1/models/mnist:predict'
data = json.dumps({'instances':pixels.tolist()})

result = requests.post(address, data=data)
predictions = json.loads(str(result.content, 'utf-8'))['predictions']

for prediction in predictions:
  print(np.argmax(prediction))
