from BingImages import BingImages
from PIL import Image
import requests
import os
from io import BytesIO


# Search n Bing and scrap data
detail = {}
names = ["Toyota", "Mercedes", "Lamborghini", "Kia"]
detail[names[0]] = list(BingImages("JavaScript Code", type="photo", count=5).get())
detail[names[1]] = list(BingImages("Java code", color="red", count=5).get())
detail[names[2]] = list(BingImages("C++ code", type="photo", count=5).get())
detail[names[3]] = list(BingImages("Kotlin Code", licensetype="publicDomain", count=5).get())

print(detail[names[2]][2])

# URL of the image
url = detail[names[2]][2]
# Download the image                
response = requests.get(url)
filename = "image.jpg"
with open(filename, "wb") as f:
    f.write(response.content)

# Display the image
img = Image.open(filename)
img.show()

# Delete the image file
os.remove(filename)
