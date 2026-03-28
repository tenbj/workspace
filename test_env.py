import sys
print("Python version:", sys.version)
try:
    from PIL import Image
    print("PIL: YES")
except ImportError:
    print("PIL: NO")
try:
    import pytesseract
    print("pytesseract: YES")
except ImportError:
    print("pytesseract: NO")
try:
    import requests
    print("requests: YES")
except ImportError:
    print("requests: NO")
try:
    import cv2
    print("opencv: YES")
except ImportError:
    print("opencv: NO")
try:
    import torch
    print("torch: YES")
except ImportError:
    print("torch: NO")
try:
    import transformers
    print("transformers: YES")
except ImportError:
    print("transformers: NO")
