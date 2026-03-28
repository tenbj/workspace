import sys, io
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw

img = Image.new('RGB', (480, 240), (44, 62, 80))
d = ImageDraw.Draw(img)
d.text((20, 40), 'Hello World!\nOpenClaw Image Test\nMarch 23, 2026\nChinese: \u4e2d\u6587\u6d4b\u8bd5', fill=(255, 255, 255))

buf = io.BytesIO()
img.save(buf, format='PNG')
b64 = buf.getvalue().hex()
# Write hex to stdout (stderr is piped, stdout too but captured differently)
# Use a file
with open('C:/Users/Administrator/.qclaw/workspace/test_img_b64.txt', 'w') as f:
    f.write(b64)
print("WROTE_B64_FILE")
