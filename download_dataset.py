"""Script to automatically download and extract the Indonesia Hourly Weather dataset
from Kagglehub into the local ./dataset folder.
"""
import os
import shutil
import kagglehub

DATASET_NAME = "karanroyka/indonesia-hourly-weather-for-rain-prediction"
TARGET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")

def download_and_setup_dataset():
    print(f"Downloading dataset '{DATASET_NAME}' via kagglehub...")
    download_path = kagglehub.dataset_download(DATASET_NAME)
    print("Downloaded to cache:", download_path)
    
    source_data_dir = os.path.join(download_path, "data")
    if not os.path.exists(source_data_dir):
        source_data_dir = download_path
        
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    print(f"Copying dataset files to {TARGET_DIR}...")
    copied_files = 0
    for file_name in os.listdir(source_data_dir):
        src_file = os.path.join(source_data_dir, file_name)
        dst_file = os.path.join(TARGET_DIR, file_name)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)
            print(f"  -> {file_name}")
            copied_files += 1
            
    print(f"Done! {copied_files} files ready in {TARGET_DIR}")

if __name__ == "__main__":
    download_and_setup_dataset()
