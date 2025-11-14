import os
from PIL import Image
import pillow_heif

# Register HEIC support
pillow_heif.register_heif_opener()

def convert_to_JPG(folder_path):
    print(f"Scanning folder: {folder_path}")
    output_folder = os.path.join(folder_path, "converted_jpgs")
    os.makedirs(output_folder, exist_ok=True)

    converted_count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(output_folder, jpg_filename)

            try:
                image = Image.open(heic_path)
                image.save(jpg_path, "JPEG")
                print(f"Converted: {filename} → {jpg_filename}")
                converted_count += 1
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

    if converted_count == 0:
        print("No HEIC files found or converted.")
    else:
        print(f"Finished converting {converted_count} file(s).")

# Run the conversion
convert_to_JPG("./G2")