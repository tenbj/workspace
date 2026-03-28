import sys, os
sys.stdout.reconfigure(encoding='utf-8')

# Check workspace permissions
ws = 'C:/Users/Administrator/.qclaw/workspace'
print("WS exists:", os.path.exists(ws))
print("WS isdir:", os.path.isdir(ws))
print("WS can read:", os.access(ws, os.R_OK))
print("WS can write:", os.access(ws, os.W_OK))
print("WS can exec:", os.access(ws, os.X_OK))

# Check parent
parent = 'C:/Users/Administrator/.qclaw'
print("\nParent exists:", os.path.exists(parent))
print("Parent can write:", os.access(parent, os.W_OK))
print("Parent can read:", os.access(parent, os.R_OK))

# Check what user can write
print("\nUser can write C:/Users/Administrator:", os.access('C:/Users/Administrator', os.W_OK))

# List workspace contents
print("\nWorkspace files:")
for f in os.listdir(ws):
    fpath = os.path.join(ws, f)
    print(" ", f, "- R:", os.access(fpath, os.R_OK), "- W:", os.access(fpath, os.W_OK))
