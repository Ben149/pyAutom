# This script calculates and prints the total size (in bytes) of all files 
# located in the 'C:\Windows\System32' directory.
# It does not include the sizes of files in subdirectories.

import os

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(f'Total size: {totalSize} B')



# This script calculates and prints the total size of all files (in gigabytes)
# located in the 'C:\Windows\System32' directory.
# It only counts files in that directory (not subdirectories).

import os

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

# Convert bytes to gigabytes (1 GB = 1024^3 bytes)
totalSizeGB = totalSize / (1024 ** 3)

# Print total size in GB, rounded to 2 decimal places
print(f'Total size: {totalSizeGB:.2f} GB')
