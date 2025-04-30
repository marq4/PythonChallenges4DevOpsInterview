
import subprocess
import sys


cmd = sys.argv[1]

result = subprocess.run(cmd, text=True, capture_output=True)
print(result.stdout)

