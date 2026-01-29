"""
Number Image Generator
Generates PNG images of numbers 10-100 

Requirements:
    pip install Pillow

Usage:
    python generate_numbers.py
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create output directory in current working directory
output_dir = "./numbers"
os.makedirs(output_dir, exist_ok=True)

# Settings
size = (100, 100)
bg_color = "#2d1b4e"  # Dark purple
text_color = "#00ffff"  # Cyan

# Try to use a nice font, fall back to default if not available
try:
    #  Linux systems
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
except:
    try:
        # Windows font path
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 40)
    except:
        try:
            # Mac font path
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 40)
        except:
            # Fall back to default font
            font = ImageFont.load_default()

# Generate images for numbers 10-100
for num in range(10, 101):
    # Create image with purple background
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Get text to draw
    text = str(num)
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center text
    x = (size[0] - text_width) // 2 - bbox[0]
    y = (size[1] - text_height) // 2 - bbox[1]
    
    # Draw cyan text
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save image
    img.save(f"{output_dir}/{num}.png")

print(f"Created {len(range(10, 101))} images in {output_dir}")
