import os
from PIL import Image

INPUT_DIR = "input_photos"
OUTPUT_DIR = "output_photos"

os.makedirs(OUTPUT_DIR, exist_ok=True)

counter = 1

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        src = os.path.join(INPUT_DIR, filename)

        img = Image.open(src)

        clean = Image.new(img.mode, img.size)
        clean.putdata(list(img.getdata()))

        ext = os.path.splitext(filename)[1].lower()
        new_name = f"photo_{counter:04d}{ext}"

        clean.save(os.path.join(OUTPUT_DIR, new_name))

        print(f"Processed: {filename} -> {new_name}")
        counter += 1

print("Done!")
