### Script 1 : Non - Pythonic ###

# This script demonstrates how to manually join file paths using string operations.
# Not recommended for cross-platform applications.

homeFolder = r'C:\Users\Volatile'  # Base directory path (Windows-style)

subFolder = 'spam'  # Name of the subdirectory to join

# Method 1: Manual string concatenation using escaped backslash
path = homeFolder + '\\' + subFolder

# Method 2: Joining path segments using '\\' as the separator
path1 = '\\'.join([homeFolder, subFolder])

print(path)
print(path1)


### Script 2 : Pythonic from the book ###

# Import Path from the pathlib module for object-oriented file path handling
from pathlib import Path

# Define the base path as a Path object
homeFolder = Path('C:/Users/Volatile')

# Define a subfolder to be appended to the base path
subFolder = Path('spam')

# Use the / operator to join the base and subfolder paths into a new Path object
homeFolder / subFolder
# Output: WindowsPath('C:/Users/Volatile/spam')

# Convert the Path object to a string (returns a Windows-style path with backslashes)
path2 = str(homeFolder / subFolder)
# Output: 'C:\\Users\\Volatile\\spam'

print(path2)


### Script 3 : Pythonic ###

from pathlib import Path

# This script demonstrates how to join file paths using the pathlib module.
# It provides a safe, readable, and cross-platform way to construct file system paths.

homeFolder = Path(r'C:\Users\Volatile')  # Base directory as a Path object

subFolder = 'spam'  # Name of the subdirectory to append

# Joins the base path with the subfolder in a platform-independent way
fullPath = homeFolder / subFolder

# Print the full constructed path
print(fullPath)