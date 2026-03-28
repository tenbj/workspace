import sys
sys.stdout.reconfigure(encoding='utf-8')
print("Python works:", sys.version)

from PIL import Image, ImageDraw
img = Image.new('RGB', (400, 200), (44, 62, 80))
d = ImageDraw.Draw(img)
d.text((20, 40), 'Hello World\nOpenClaw Test\nMarch 23 2026', fill=(255, 255, 255))

out = 'C:/Users/Administrator/.qclaw/workspace/test_img.png'
img.save(out)
print("Saved:", out)
