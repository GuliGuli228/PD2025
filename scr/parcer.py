import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # без GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver


def scroll_and_collect(driver, search_url, target_count):
    driver.get(search_url)
    time.sleep(3)
    last_height = driver.execute_script("return document.body.scrollHeight")
    image_urls = set()

    while len(image_urls) < target_count:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            src = img.get_attribute("src")
            if src and "https://" in src:
                image_urls.add(src)
            if len(image_urls) >= target_count:
                break

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return list(image_urls)[:target_count]


def download_images(image_urls, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, url in enumerate(tqdm(image_urls, desc="Скачивание изображений")):
        try:
            response = requests.get(url, timeout=10)
            ext = url.split('.')[-1].split('?')[0][:4]
            filename = os.path.join(directory, f"image_{i+1}.{ext}")
            with open(filename, "wb") as f:
                f.write(response.content)
        except Exception as e:
            print(f"Ошибка при скачивании {url}: {e}")


def main():
    query = input("Введите поисковый запрос: ").strip()
    num_images = int(input("Сколько изображений нужно скачать?: "))
    directory = input("Введите путь к папке для сохранения: ").strip()

    search_url = f"https://www.pinterest.com/search/pins/?q={query.replace(' ', '%20')}"
    print(f"Поиск по URL: {search_url}")

    print("Запуск браузера...")
    driver = setup_driver()

    print("Сбор изображений...")
    image_urls = scroll_and_collect(driver, search_url, num_images)
    driver.quit()

    print(f"Найдено {len(image_urls)} изображений. Начинается скачивание...")
    download_images(image_urls, directory)

    print("Готово!")


if __name__ == "__main__":
    main()
