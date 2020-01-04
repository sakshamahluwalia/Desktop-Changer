import random, requests, shutil, os, time
from bs4 import BeautifulSoup

start_time = time.time()

page_number = random.randint(1, 2) 

if page_number == 1:
	index = random.randint(1, 48)
else:
	index = random.randint(0, 26)

# Request the page
if page_number == 1:
	req = requests.get("https://workhardanywhere.com/collections/wallpapers")
else:
	req = requests.get("https://workhardanywhere.com/wallpapers?page={}".format(page_number))

content = req.content

# Create an instance of BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Get the link to the image page 
tags = soup.findAll("a", {"class": "ProductItem__ImageWrapper"})

# extract the link from the anchor tag 
link = "https://shop.workhardanywhere.com/" + tags[index]["href"]

req2 = requests.get(link)

content_req2 = req2.content

# Create an instance of BeautifulSoup
soup_req2 = BeautifulSoup(content_req2, "html.parser")

images = soup_req2.findAll("a", {"class": "wallpaper_download"})

# capture a randomn image's url
wallpaper = images[0]["href"]

data = requests.get(wallpaper, stream=True)
with open('//home/ahlus/Wallpapers/wallpaper.jpg', 'wb') as out_file:
    shutil.copyfileobj(data.raw, out_file)

del data

os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/ahlus/Wallpapers/wallpaper.jpg")
print("--- %s seconds ---" % (time.time() - start_time))
