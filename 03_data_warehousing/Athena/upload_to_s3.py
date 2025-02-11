# This script uses the boto3 library to interact with AWS S3 and uploads files similarly to how your original script uploads files to GCS.
# Make sure to replace placeholder values for BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION with your actual AWS credentials
# and bucket information. Also, ensure that the boto3 library is installed in your environment using pip install boto3.

import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import time

# Change this to your bucket name
BUCKET_NAME = "your_s3_bucket_name"

# AWS credentials (if not using environment variables or IAM roles)
AWS_ACCESS_KEY_ID = "your_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
AWS_REGION = "your_aws_region"

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-"
MONTHS = [f"{i:02d}" for i in range(1, 7)]
DOWNLOAD_DIR = "."

CHUNK_SIZE = 8 * 1024 * 1024  # 8 MB

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

s3_client = boto3.client('s3', 
                         aws_access_key_id=AWS_ACCESS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=AWS_REGION)


def download_file(month):
    url = f"{BASE_URL}{month}.parquet"
    file_path = os.path.join(DOWNLOAD_DIR, f"yellow_tripdata_2024-{month}.parquet")

    try:
        print(f"Downloading {url}...")
        urllib.request.urlretrieve(url, file_path)
        print(f"Downloaded: {file_path}")
        return file_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None


def verify_s3_upload(bucket_name, object_name):
    try:
        s3_client.head_object(Bucket=bucket_name, Key=object_name)
        return True
    except Exception as e:
        print(f"Verification failed for {object_name}: {e}")
        return False


def upload_to_s3(file_path, max_retries=3):
    object_name = os.path.basename(file_path)

    for attempt in range(max_retries):
        try:
            print(f"Uploading {file_path} to {BUCKET_NAME} (Attempt {attempt + 1})...")
            s3_client.upload_file(file_path, BUCKET_NAME, object_name)
            print(f"Uploaded: s3://{BUCKET_NAME}/{object_name}")
            
            if verify_s3_upload(BUCKET_NAME, object_name):
                print(f"Verification successful for {object_name}")
                return
            else:
                print(f"Verification failed for {object_name}, retrying...")
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Credentials error: {e}")
            return
        except Exception as e:
            print(f"Failed to upload {file_path} to S3: {e}")
        
        time.sleep(5)  # Wait before retrying
    
    print(f"Giving up on {file_path} after {max_retries} attempts.")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        file_paths = list(executor.map(download_file, MONTHS))

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(upload_to_s3, filter(None, file_paths))  # Remove None values

    print("All files processed and verified.")