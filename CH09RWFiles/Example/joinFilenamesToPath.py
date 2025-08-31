# This script joins names from a list of filenames to the end of a folder's name.

from pathlib import Path

myFiles = ['petrol.csv', 'petrol.xlsx', 'kerosene.csv', 'kerosene.xlsx']

for filename in myFiles:
    print(Path(r'C:\Volatile', filename))