import json
import requests
import io
import base64
import time
import os
from PIL import Image, PngImagePlugin

url = "http://127.0.0.1:7861"


prompts = ["a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",
            "a portrait face closeup of a man as fantasy character, Concept art, fine art, highly detailed, extremely detailed, beautiful composition, trending on deviantart by Greg Rutkowski and artgerm",]  # Add more prompts as needed

# Create a timestamped folder
timestamp = time.strftime("%H-%M-%S")
folder_name = os.path.join("out", timestamp)
folder_path = os.path.join(os.getcwd(), folder_name)
os.makedirs(folder_path, exist_ok=True)

print(f"Current working directory: {os.getcwd()}")  # Print the current working directory
print(f"Saving images in folder: {folder_path}")    # Print the folder path

for prompt in prompts:
    payload = {
        "prompt": prompt,
        "steps": 25,
        "sampler_index": 'DPM++ 2M Karras',
        "seed": -1,
    }

    highres_payload = {
                    "enable_hr": True,
                    "hr_upscaler": "Latent",
                    "hr_scale": 1,
                    "hr_second_pass_steps": 12,
                    "denoising_strength": 0.5,
    }
    payload.update(highres_payload)

    while True:
        try:
            response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
            response.raise_for_status()
            break
        except requests.exceptions.RequestException as e:
            print(f"Service not available yet: Trying again in 10 seconds.")
            time.sleep(10)  # Wait for 5 seconds before retrying

    r = response.json()
    start_time = time.time()

    for i, img_data in enumerate(r['images']):
        image = Image.open(io.BytesIO(base64.b64decode(img_data.split(",", 1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + img_data
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))

        # Save the images with different filenames in the timestamped folder
        image_filename = os.path.join(folder_path, f"{prompt}_{i}.png")
        image.save(image_filename, pnginfo=pnginfo)
    
end_time = time.time()  # End time
elapsed_time = end_time - start_time  # Calculate elapsed time
print(f"Time taken for inference of all images: {elapsed_time:.2f} seconds")  # Print the elapsed time
