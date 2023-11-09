import json
import os
import requests

import os
import requests

def download_images(image_dict, path=''):
    for folder_path, image_urls in image_dict.items():
        folder_path = os.path.join(path, folder_path)

        os.makedirs(folder_path, exist_ok=True)

        for index, image_url in enumerate(image_urls, start=1):
            try:
                response = requests.get(image_url)
                response.raise_for_status()

                _, ext = os.path.splitext(image_url)
                file_name = f"image_{index}{ext}"

                file_path = os.path.join(folder_path, file_name)

                with open(file_path, 'wb') as file:
                    file.write(response.content)

                print(f"Downloaded: {file_name} to {folder_path}")

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {image_url}: {e}")

def load_file(file_name='data.json'):
    with open(file_name, encoding = "utf-8") as f:
        data = json.load(f)
    return data
data = load_file()
print(type(data))
print(data)
download_images(data, 'h2h')
