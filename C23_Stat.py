import os
from datetime import *
statistics = os.stat('text.txt')
print(statistics)
print()
print("file size",statistics.st_size)
print("Last modified time",datetime.fromtimestamp(statistics.st_mtime))