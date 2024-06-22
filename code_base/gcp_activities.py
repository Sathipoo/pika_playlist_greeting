
from google.cloud import storage
import os

credentials_file_path="/Users/sathishkumar/Downloads/compact-haiku-414007-7c19f02fa07b.json"
def upload_file_to_gcs(bucket_name, source_file_path, destination_subfolder="", credentials_file_path=credentials_file_path):
    # Create a GCS client object using service account key file authentication
    try:
        client = storage.Client.from_service_account_json(credentials_file_path)
    except FileNotFoundError:
        print(f"Error: Service account key file not found at {credentials_file_path}")
        return

    # Reference the bucket
    bucket = client.bucket(bucket_name)

    # Determine the destination path in GCS
    destination_path = os.path.join(destination_subfolder, os.path.basename(source_file_path))

    # Upload the file
    try:
        blob = bucket.blob(destination_path)
        blob.upload_from_filename(source_file_path)
        print(f"File '{source_file_path}' uploaded to bucket '{bucket_name}' as '{blob.name}'")
    except Exception as e:
        print(f"Upload failed: {e}")
