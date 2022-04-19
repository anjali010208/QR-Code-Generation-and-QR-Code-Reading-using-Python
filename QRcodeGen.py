import qrcode
import pandas as pd
import os
df = pd.read_csv("flipKartProducts.csv")
for index, values in df.iterrows():
  unique_id = values["uniq_id"]
  product_url = values["product_url"]
  product_name = values["product_name"]
  pid = values["pid"]
  retail_price = values['retail_price']
  discounted_price = values['discounted_price']
  data = f'''
  unique id: {unique_id}\n
  product url: {product_url}\n
  product name: {product_name}\n
  product id: {pid}\n
  retail price: {retail_price}\n
  discounted price: {discounted_price}\n
  '''
  qr_img = qrcode.make(data)
  print(data)
  dir = os.getcwd()
  dir=dir + "/QRCodes"
  name=f"{product_name}_{unique_id}.jpg"
  f=os.path.join(dir,name)
  qr_img.save(f)
 
