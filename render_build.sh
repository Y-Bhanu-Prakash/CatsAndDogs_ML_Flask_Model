#!/usr/bin/env bash

# Step 1: Install Python dependencies
pip install -r requirments.txt

# Step 2: Download and extract model/dataset
# (Only if needed during app runtime)

# echo "Downloading model archive..."
# wget -O model.zip https://your-storage-url.com/path/to/model.zip

echo "Extracting model..."
unzip -o model.zip -d PetImages

# Download the dataset (optional – if your app needs it at build time)
# wget -O dataset.zip https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
# unzip dataset.zip -d ./data
# Clean up the downloaded zip file
# rm dataset.zip
