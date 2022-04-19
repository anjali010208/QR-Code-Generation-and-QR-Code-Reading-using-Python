import os
from PIL import Image
from pyzbar.pyzbar import decode
import pandas as pd
dir = os.getcwd()
dir=dir + "/QRCodes"
data1={}
for name in os.listdir(dir):
  f = os.path.join(dir,name)
  if os.path.isfile(f) and name.endswith('.jpg'):
    data = decode(Image.open(f))
    data1[str(name)]=repr(data[0][0].decode('utf-8'))
    print(data[0][0].decode('utf-8'))
df=pd.DataFrame.from_dict(data1,orient='index',columns=["Product Details"])
df.to_csv('store.csv')
