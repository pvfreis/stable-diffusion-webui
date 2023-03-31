import json
import requests
import io
import base64
import time
import os
from PIL import Image, PngImagePlugin

url = "http://127.0.0.1:7861"

prompts = ["1boy", "1girl", "1dog", "1cat", "1boy", "1girl", "1dog", "1cat", "1boy", "1girl", "1dog", "1cat", "1boy", "1girl", "1dog", "1cat", ]  # Add more prompts as needed

# Create a timestamped folder
timestamp = time.strftime("%H-%M-%S")
os.makedirs(timestamp, exist_ok=True)

for prompt in prompts:
    payload = {
        "prompt": prompt,
        "steps": 25,
        "sampler_index": 'DPM++ 2M Karras',
    }

    while True:
        try:
            response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
            response.raise_for_status()
            break
        except requests.exceptions.RequestException as e:
            print(f"Service not available yet: Trying again in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying

    r = response.json()

    for i, img_data in enumerate(r['images']):
        image = Image.open(io.BytesIO(base64.b64decode(img_data.split(",", 1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + img_data
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))

        # Save the images with different filenames in the timestamped folder
        image_filename = f"out/{timestamp}/{prompt}_{i}.png"
        image.save(image_filename, pnginfo=pnginfo)
