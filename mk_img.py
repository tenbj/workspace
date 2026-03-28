from PIL import Image, ImageDraw
img = Image.new('RGB', (400, 200), (44, 62, 80))
d = ImageDraw.Draw(img)
d.text((20, 40), 'Hello World\nOpenClaw Test\nMarch 23 2026', fill=(255, 255, 255))
img.save('C:/Users/Administrator/test_img.png')
print('OK')
