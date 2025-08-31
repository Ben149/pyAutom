import os
import csv
import time
from pathlib import Path
from datetime import datetime

def human_readable_size(size_bytes):
    """Convert bytes to a human-readable string (e.g., KB, MB, GB)."""
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def get_files_data(folder_path):
    """Return list of files with their size and last changed time in the folder recursively."""
    files_data = []
    try:
        for dirpath, _, filenames in os.walk(folder_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    try:
                        size = os.path.getsize(fp)
                        last_changed_ts = os.path.getmtime(fp)
                        last_changed = datetime.fromtimestamp(last_changed_ts)
                        files_data.append({
                            'Folder Path': dirpath,
                            'Filename': f,
                            'Size (Bytes)': size,
                            'Size (Readable)': human_readable_size(size),
                            'Last Changed': last_changed
                        })
                    except (PermissionError, FileNotFoundError):
                        # Skip files we can't access
                        pass
    except (PermissionError, FileNotFoundError):
        # Skip folders we can't access
        pass
    return files_data

def main():
    root_folder = Path(r'C:\Users\benson.lewis\OneDrive - MIC\Desktop\Learning\udemy')
    start_time = time.time()

    all_files = []

    # Instead of just immediate subfolders, we gather all files recursively
    all_files = get_files_data(root_folder)

    # Sort files by Last Changed descending (most recent first)
    all_files.sort(key=lambda x: x['Last Changed'], reverse=True)

    duration = time.time() - start_time

    # Prepare output directory and file path
    output_dir = r'C:\Users\Public\Reports'
    os.makedirs(output_dir, exist_ok=True)

    csv_file = os.path.join(output_dir, 'udemy_files_report.csv')

    # Write to CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Folder Path', 'Filename', 'Size (Bytes)', 'Size (Readable)', 'Last Changed']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_files:
            # Format the Last Changed datetime nicely as string
            row['Last Changed'] = row['Last Changed'].strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(row)

        # Optional summary rows
        writer.writerow({})
        writer.writerow({'Folder Path': 'Total scanned files', 'Filename': len(all_files)})
        writer.writerow({'Folder Path': 'Scan duration (seconds)', 'Filename': f"{duration:.2f}"})

    print(f"Report saved to {csv_file}")

if __name__ == "__main__":
    main()