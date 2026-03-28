import sys, os
sys.stdout.reconfigure(encoding='utf-8')

img_path = r'C:\Users\Administrator\.qclaw\media\browser\5aa4a629-c8ca-408a-a791-6d43b53b6a44.png'

if not os.path.exists(img_path):
    # Try to find any PNG in the browser media folder
    media_dir = r'C:\Users\Administrator\.qclaw\media\browser'
    if os.path.exists(media_dir):
        files = sorted([os.path.join(media_dir, f) for f in os.listdir(media_dir) if f.endswith('.png')], key=os.path.getmtime, reverse=True)
        if files:
            img_path = files[0]
            print("Using latest:", img_path)
        else:
            print("NO PNG FOUND")
            sys.exit(1)
    else:
        print("MEDIA DIR NOT FOUND")
        sys.exit(1)
else:
    print("File exists:", img_path)
    print("Size:", os.path.getsize(img_path))

# Read and encode
import base64
with open(img_path, 'rb') as f:
    data = f.read()
print("Read bytes:", len(data))
b64 = base64.b64encode(data).decode()
print("BASE64:", b64[:50], "...")
