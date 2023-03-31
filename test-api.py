import json
import requests
import io
import base64
import time
from PIL import Image, PngImagePlugin

url = "http://127.0.0.1:7861"

payload = {
    "prompt": "1boy",
    "steps": 25,
    "sampler_index":'DPM++ 2M Karras',
}

while True:
    try:
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
        response.raise_for_status()
        break
    except requests.exceptions.RequestException as e:
        print(f"Service not available yet: {e}")
        time.sleep(5)  # Wait for 5 seconds before retrying

r = response.json()

for i in r['images']:
    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

    png_payload = {
        "image": "data:image/png;base64," + i
    }
    response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("parameters", response2.json().get("info"))
    image.save('test/output.png', pnginfo=pnginfo)
