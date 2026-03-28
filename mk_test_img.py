from PIL import Image, ImageDraw, ImageFont
import os

# Create a test image with text
img = Image.new('RGB', (400, 200), color=(44, 62, 80))
draw = ImageDraw.Draw(img)

text = "Hello World\nOpenClaw Test\nMarch 23, 2026"
draw.text((20, 40), text, fill=(255, 255, 255))

out = "C:\\Users\\Administrator\\.qclaw\\workspace\\test_img.png"
img.save(out)
print("Saved:", out)
