import random, requests, shutil, os, time
from bs4 import BeautifulSoup

# Request the page
req = requests.get("https://workhardanywhere.com/wallpapers/")
content = req.content

# Create an instance of BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Get the image on the page. approx 30
images = soup.findAll("div", {"class": "image_holder"})

# capture their urls
sources = [img.find("img")['src'].replace("-550x550", "") for img in images]
index = random.randint(2, 30)

wallpaper = sources[index]
data = requests.get(wallpaper, stream=True)
with open('wallpaper.jpg', 'wb') as out_file:
    shutil.copyfileobj(data.raw, out_file)

del data

os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/ahlus/Desktop/wallpaper.jpg")
time.sleep(1)
os.system("rm wallpaper.jpg")
print ("enjoy")