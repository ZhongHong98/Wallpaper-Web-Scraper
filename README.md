# Wallpaper-Web-Scraper
## 📖 Project Overview
This project is a Python-based web crawler that automatically downloads high-resolution wallpapers from a public website.

The script sends HTTP requests, parses HTML content, navigates multiple pages, extracts image download links, and saves the files locally.

This project demonstrates my ability to:

- Automate data extraction using Python

- Parse web content using BeautifulSoup

- Handle pagination and nested page navigation

- Work with file systems and HTTP requests

## 🛠️ Tools & Technologies

- Python

- Requests – for sending HTTP requests

- BeautifulSoup (bs4) – for HTML parsing

- OS module – for file handling and directory management

## 📂 Features

- Automatically crawls multiple pages

- Extracts wallpaper download links

- Downloads only 1920x1080 resolution images

- Saves files with auto-increment naming

- Skips missing resolution images gracefully

## 📥 How to Use
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/wallpaper-web-scraper.git
cd wallpaper-web-scraper
```

### 2️⃣ Install required libraries
```bash
pip install requests beautifulsoup4 lxml
```

### 3️⃣ Configure download path

Edit this line in the script:

```python
download_path = r"F:\OneDrive\Python\pythonProject\Wallpaper_Anime\Wallpaper"
```

Change it to your preferred folder.

### 4️⃣ Run the script

```bash
python wallpaper_scraper.py
```

The wallpapers will be downloaded automatically.

📁 Python file: [View Python File](Python/Wallpaper_Download.py)

## ⚠️ Disclaimer

This project is for educational purposes only.
Please respect website terms of service and robots.txt rules before scraping any website.
