import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw
import io, os

img = Image.new('RGB', (400, 200), (44, 62, 80))
d = ImageDraw.Draw(img)
d.text((20, 40), 'Hello World\nOpenClaw Test\nMarch 23 2026', fill=(255, 255, 255))

# Save to bytes
buf = io.BytesIO()
img.save(buf, format='PNG')
png_bytes = buf.getvalue()
print("PNG size:", len(png_bytes), "bytes")

# Try writing raw bytes to workspace
out_path = 'C:/Users/Administrator/.qclaw/workspace/test_img.bin'
try:
    with open(out_path, 'wb') as f:
        f.write(png_bytes)
    print("BIN write OK:", out_path, "- size:", os.path.getsize(out_path))
except Exception as e:
    print("BIN write FAIL:", e)

# Try workspace path directly
out_path2 = 'C:/Users/Administrator/.qclaw/workspace/test_img.png'
try:
    with open(out_path2, 'wb') as f:
        f.write(png_bytes)
    print("PNG write OK:", out_path2)
except Exception as e:
    print("PNG write FAIL:", e)
