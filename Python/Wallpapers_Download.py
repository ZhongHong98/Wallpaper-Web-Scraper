import requests
from bs4 import BeautifulSoup
import os
# This line hides the messy red warning messages
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- SETTINGS ---
download_path = r"F:\OneDrive\Python\pythonProject\Wallpaper_Anime\Wallpaper"
root_url = "https://wallpaperscraft.com"
start_url = "https://wallpaperscraft.com/catalog/dark"
n = 1876

if not os.path.exists(download_path):
    os.makedirs(download_path)

# Added verify=False here
resp = requests.get(start_url, verify=False)

while True:
    main_page = BeautifulSoup(resp.text, "lxml")
    container = main_page.find("div", attrs={"class": "wallpapers wallpapers_zoom wallpapers_main"})
    if not container:
        break
        
    image_list = container.find_all("a", attrs={"class": "wallpapers__link"})

    for image in image_list:
        href = root_url + image.get("href")
        # Added verify=False here
        resp1 = requests.get(href, verify=False)
        resp1.encoding = "utf-8"
        child_page = BeautifulSoup(resp1.text, "lxml")

        res_link = child_page.find("a", string="1920x1080")
        
        if res_link is not None:
            href_resolution = root_url + res_link.get("href")
            # Added verify=False here
            resp2 = requests.get(href_resolution, verify=False)
            resolution_page = BeautifulSoup(resp2.text, "lxml")

            download_btn = resolution_page.find("a", attrs={"class": "gui-button gui-button_full-height"})
            if download_btn:
                href_image = download_btn.get("href")
                file_name = f"Wallpaper_Anime_{n}.jpg"
                full_file_path = os.path.join(download_path, file_name)

                print(f"Downloading: {file_name}")

                # Added verify=False here
                image_data = requests.get(href_image, verify=False).content
                with open(full_file_path, mode="wb") as f:
                    f.write(image_data)
                n += 1 
        else:
            print("Skipping: No 1080p version")

    next_button = main_page.find("a", attrs={"class": "pager__link"}, string="→")
    if next_button is None:
        break

    href_next = root_url + next_button.get("href")
    # Added verify=False here
    resp = requests.get(href_next, verify=False)
    print(f"Next page: {href_next}")

