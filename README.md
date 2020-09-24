# Exercise 3 - Assignment 1

## Introduction
Some utility functions provided by GOOGLE are introduced in this assignment to help us interact with 
[google cloud storage](https://cloud.google.com/storage). They are:
1. storage_copy_file.py: Copies a blob from one bucket to another with a new name.
2. storage_create_bucket.py: Creates a new bucket.
3. storage_delete_bucket.py: Deletes a bucket.
4. storage_delete_file.py: Deletes a blob from the bucket.
5. storage_download_file.py: Downloads a blob from the bucket.
6. storage_list_buckets.py: Lists all buckets.
7. storage_list_files.py: Returns a list of all the blobs in the bucket.
8. storage_list_files_with_prefix.py: Lists all the blobs in the bucket that begin with the prefix.
9. storage_make_public.py: Makes a blob publicly accessible.
10. storage_move_file.py: Renames a blob.
11. storage_upload_file.py: Uploads a file to the bucket.

## Problem statement
### Upload a list of files to the bucket
Given [a uploaded data folder](./images/upload/) consisting of all files needed to store on gcp storage, we plan to write a python 
script named [**_storage_upload_files.py_**](storage_upload_files.py) to:
- Create a bucket called *comp4312_studentid* on gcp, which *studentid* is your student ID.
- Upload data into the bucket:
    - List all files in [the data folder](./images/upload/) and assign to *source_file_names*
    - Extract basename of each path in *source_file_names* to form *destination_blob_names*
    - Upload files in *source_file_names* on the *comp4312_studentid* bucket with filenames listed in *destination_blob_names*

### Download a list of blobs from the bucket
Suppose we have a bucket named *comp4312_studentid* on gcp storage containing data files wanted to save locally in 
[a downloaded data folder](./images/download/), we are going to write a python 
script named [**_storage_download_files.py_**](storage_download_files.py) to:
- Download all files on the bucket:
    - List all files in the *comp4312_studentid* bucket on gcp storage and assign to *source_blob_names*
    - Create paths to save all files in *source_blob_names* and store in *destination_file_names*
    - Download all files on the *comp4312_studentid* bucket with names listed in source_blob_names and save to paths in destination_file_names
- Delete the bucket *comp4312_studentID* on gcp
    
## Code Skeletons and Requirements
You are expected to work on the two files below which are provided general skeletons:
1. [**storage_upload_files.py**](storage_upload_files.py): Uploads a list of files to the bucket.
2. [**storage_download_files.py**](storage_download_files.py): Downloads a list of blobs from the bucket.

**Please complete all preserved parts inside these two python files under the blocks:**
```python
    #####################
    # Your code is here #
    ####################
```
**to form executable scripts.**

## Install venv to run codes

```commandline
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
