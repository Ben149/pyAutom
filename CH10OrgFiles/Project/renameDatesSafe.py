#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY safely.

import shutil, os, re

# Toggle dry-run mode (True = simulate, False = actually rename)
dry_run = True

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)        # all text before the date
    ((0|1)?\d)-                            # one or two digits for the month
    ((0|1|2|3)?\d)-                        # one or two digits for the day
    ((19|20)\d\d)                          # four digits for the year
    (.*?)$                                 # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilePath = os.path.join(absWorkingDir, amerFilename)
    euroFilePath = os.path.join(absWorkingDir, euroFilename)

    # Prevent overwriting existing files.
    if os.path.exists(euroFilePath):
        print(f'[SKIP] "{euroFilePath}" already exists. Not renaming "{amerFilePath}".')
        continue

    # Perform or simulate renaming.
    if dry_run:
        print(f'[DRY RUN] Would rename "{amerFilePath}" → "{euroFilePath}"')
    else:
        print(f'[RENAME] "{amerFilePath}" → "{euroFilePath}"')
        shutil.move(amerFilePath, euroFilePath)