import tempfile, os, sys
tmp = tempfile.gettempdir()
print("Tmp dir:", tmp)
print("Writable:", os.access(tmp, os.W_OK))
print("Python exe:", sys.executable)

# Try writing to tmp
test_file = os.path.join(tmp, 'openclaw_write_test.txt')
try:
    with open(test_file, 'w') as f:
        f.write('test')
    print("Write to tmp: OK")
    os.remove(test_file)
except Exception as e:
    print("Write to tmp FAILED:", e)
