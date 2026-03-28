import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw

img = Image.new('RGB', (400, 200), (44, 62, 80))
d = ImageDraw.Draw(img)
d.text((20, 40), 'Hello World\nOpenClaw Test\nMarch 23 2026', fill=(255, 255, 255))

# Try different locations
import os
paths = [
    'D:/temp/openclaw_test.png',
    'C:/Users/Administrator/Desktop/test_img.png',
    'D:/test_img.png',
]
for p in paths:
    try:
        d = os.path.dirname(p)
        os.makedirs(d, exist_ok=True)
        img.save(p)
        print("SUCCESS:", p)
        break
    except Exception as e:
        print("FAIL:", p, "-", e)
