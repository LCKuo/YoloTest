import zipfile
import os
import shutil

extract_dir = "./dataset"

if os.path.exists(extract_dir):
    try:
        shutil.rmtree(extract_dir)
        print(f"Directory '{extract_dir}' and its contents deleted successfully.")
    except OSError as e:
        print(f"Error: {e}")  # Handle potential errors during deletion
else:
    print(f"The directory '{extract_dir}' does not exist.")

zip_file = "./1017.zip"
extract_dir = "dataset"

with zipfile.ZipFile(zip_file, "r") as zip_ref:
    zip_ref.extractall(extract_dir)
