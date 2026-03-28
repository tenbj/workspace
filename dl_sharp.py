import sys, os, tarfile, gzip, json
sys.stdout.reconfigure(encoding='utf-8')

print("Step 1: Fetch sharp package info from npm registry")
try:
    import urllib.request
    url = "https://registry.npmjs.org/sharp/latest"
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "python/3.11"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())
    tarball_url = data["dist"]["tarball"]
    version = data["version"]
    print(f"Version: {version}")
    print(f"Tarball URL: {tarball_url}")
    print(f"Size: {data['dist']['unpackedSize']} bytes")
except Exception as e:
    print(f"Failed to fetch npm: {e}")
    sys.exit(1)

# Download to a writable location
# exec sandbox CAN write to certain paths - check if we can write to a temp-ish path
dest_dir = r"C:\Users\Administrator\.qclaw\workspace"
tarball_path = os.path.join(dest_dir, "sharp.tgz")

print("\nStep 2: Download tarball")
try:
    req = urllib.request.Request(tarball_url, headers={"User-Agent": "python/3.11"})
    with urllib.request.urlopen(req, timeout=60) as r:
        content = r.read()
    with open(tarball_path, 'wb') as f:
        f.write(content)
    print(f"Downloaded {len(content)} bytes to {tarball_path}")
except Exception as e:
    print(f"Download failed: {e}")
    sys.exit(1)

print("\nStep 3: Extract tarball")
extract_dir = os.path.join(dest_dir, "sharp_pkg")
try:
    os.makedirs(extract_dir, exist_ok=True)
    with tarfile.open(tarball_path, 'r:gz') as tar:
        tar.extractall(extract_dir)
    print("Extracted OK")
    # List contents
    for root, dirs, files in os.walk(extract_dir):
        for d in dirs:
            print(" DIR:", os.path.join(root, d))
        for f in files:
            print(" FILE:", os.path.join(root, f))
except Exception as e:
    print(f"Extract failed: {e}")
    sys.exit(1)

print("\nDone! Package ready at:", extract_dir)
