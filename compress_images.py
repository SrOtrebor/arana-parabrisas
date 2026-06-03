import os
from PIL import Image

folder = 'fotos'

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        try:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                with Image.open(filepath) as img:
                    # Convert to RGB if it's not (e.g. RGBA for some PNGs)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Resize if too large (e.g. width > 1200)
                    if img.width > 1200:
                        ratio = 1200 / float(img.width)
                        new_height = int(float(img.height) * float(ratio))
                        img = img.resize((1200, new_height), Image.Resampling.LANCZOS)
                        
                    # Save with lower quality to compress
                    img.save(filepath, "JPEG", optimize=True, quality=75)
                    print(f"Compressed {filename}")
        except Exception as e:
            print(f"Failed to compress {filename}: {e}")
