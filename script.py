import random, requests, shutil, os, time
from bs4 import BeautifulSoup

start_time = time.time()

page_number = random.randint(1, 9)

if page_number == 1:
	index = random.randint(1, 30)
elif page_number == 9:
	index = random.randint(0, 16)
else:
	index = random.randint(0, 30)

# Request the page
if page_number == 1:
	req = requests.get("https://workhardanywhere.com/wallpapers")
else:
	req = requests.get("https://workhardanywhere.com/wallpapers/{}/".format(page_number))

content = req.content

# Create an instance of BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Get the images on the page. approx 30
images = soup.findAll("div", {"class": "image_holder"})

# capture a randomn image's url
wallpaper = images[index].find("img")['src'].replace("-550x550", "")

data = requests.get(wallpaper, stream=True)
with open('//home/ahlus/Wallpapers/wallpaper.jpg', 'wb') as out_file:
    shutil.copyfileobj(data.raw, out_file)

del data

os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/ahlus/Wallpapers/wallpaper.jpg")
print("--- %s seconds ---" % (time.time() - start_time))
