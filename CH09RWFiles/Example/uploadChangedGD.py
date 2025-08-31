import os
import io
import time
from pathlib import Path
from datetime import datetime, timezone
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If no valid credentials, do OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def get_drive_folder_id(service, folder_name, parent_id=None):
    """Get folder ID by name. Creates folder if not exists."""
    query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    if parent_id:
        query += f" and '{parent_id}' in parents"

    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get('files', [])
    if items:
        return items[0]['id']
    else:
        # Create folder
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]
        folder = service.files().create(body=file_metadata, fields='id').execute()
        print(f"Created folder '{folder_name}' with ID: {folder['id']}")
        return folder['id']

def list_files_in_folder(service, folder_id):
    """Returns a dict of {filename: file metadata} for files in the folder."""
    query = f"'{folder_id}' in parents and trashed = false"
    results = service.files().list(q=query, fields="files(id, name, modifiedTime)").execute()
    items = results.get('files', [])
    files_dict = {file['name']: file for file in items}
    return files_dict

def upload_file(service, local_file_path, drive_folder_id, existing_file_id=None):
    file_metadata = {
        'name': os.path.basename(local_file_path),
        'parents': [drive_folder_id]
    }
    media = MediaFileUpload(local_file_path, resumable=True)
    if existing_file_id:
        # Update existing file
        updated_file = service.files().update(
            fileId=existing_file_id,
            media_body=media
        ).execute()
        print(f"Updated file: {local_file_path}")
        return updated_file
    else:
        # Upload new file
        uploaded_file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        print(f"Uploaded new file: {local_file_path}")
        return uploaded_file

def iso_to_timestamp(iso_str):
    dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    return dt.replace(tzinfo=timezone.utc).timestamp()

def sync_folder(service, local_folder, drive_folder_id):
    local_folder = Path(local_folder)
    drive_files = list_files_in_folder(service, drive_folder_id)

    for root, _, files in os.walk(local_folder):
        for filename in files:
            local_file = Path(root) / filename
            rel_path = local_file.relative_to(local_folder)

            # Check if file exists on Drive folder
            drive_file = drive_files.get(str(rel_path))

            local_mtime = local_file.stat().st_mtime

            if drive_file:
                remote_mtime = iso_to_timestamp(drive_file['modifiedTime'])
                if local_mtime > remote_mtime + 1:  # allow 1 second tolerance
                    # Update file
                    upload_file(service, local_file, drive_folder_id, drive_file['id'])
                else:
                    print(f"Skipped (up-to-date): {local_file}")
            else:
                # New file - upload
                upload_file(service, local_file, drive_folder_id)

def main():
    service = authenticate()

    # Set the local folder to sync and the Drive folder name
    local_folder = r'C:\Users'
    drive_folder_name = 'udemy_backup'

    # Get (or create) Drive folder
    drive_folder_id = get_drive_folder_id(service, drive_folder_name)

    # Start syncing files
    sync_folder(service, local_folder, drive_folder_id)

if __name__ == '__main__':
    main()