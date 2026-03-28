import sys, os
sys.stdout.reconfigure(encoding='utf-8')
img_path = r'C:\Users\Administrator\.qclaw\media\browser\7e770a92-f9a1-4295-8177-21a192e34ace.png'
print("Exists:", os.path.exists(img_path))
print("Size:", os.path.getsize(img_path) if os.path.exists(img_path) else "N/A")

if os.path.exists(img_path):
    from PIL import Image
    img = Image.open(img_path)
    print("Format:", img.format)
    print("Size:", img.size)
    print("Mode:", img.mode)
    print("OK - image has content")
