#!/usr/bin/env python

import sys

# [START storage_download_file]
from google.cloud import storage
from storage_list_files import return_blobs


def download_blobs(bucket_name: str, source_blob_names: list, destination_file_names: list) -> None:
    """Downloads a list of blobs from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_names = ["storage-object-name-1", ..., "storage-object-name-n"]
    # destination_file_names = ["local/path/to/file-1", ..., "local/path/to/file-n"]

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)


    for i in range(len(source_blob_names)):
        blob = bucket.blob(source_blob_names[i])
        blob.download_to_filename(destination_file_names[i])
        print(
            "File {} downloaded as {}.".format(
                source_blob_names[i], destination_file_names[i]
            )
        )
# [END storage_download_file]

if __name__ == "__main__":
    from storage_list_files import return_blobs
    # 1. List all files in the bucket "comp4312_studentid" on gcp and assign to source_blob_names
    bucket_name = "comp4312_0870121"
    source_blob_names = []

    source_blob_names = return_blobs(bucket_name)


    # An example of returned values in source_blob_names
    # source_blob_names = ['dandelion1.jpg', 'dandelion2.jpg', 'dandelion3.jpg',
    #                      'grass1.jpeg', 'grass2.jpeg', 'grass3.jpeg']

    # 2. Create paths to save all files in source_blob_names and store in destination_file_names
    import os
    download_path = "images/download/"
    destination_file_names = []

    for file in source_blob_names:
        destination_file_names.append(download_path + file)


    # An example of returned values in destination_file_names
    # destination_file_names = ['images/download/dandelion1.jpg', 'images/download/dandelion2.jpg',
    #                           'images/download/dandelion3.jpg', 'images/download/grass1.jpeg',
    #                           'images/download/grass2.jpeg', 'images/download/grass3.jpeg']

    # 3. Download files on the bucket_name bucket with names listed in source_blob_names
    #    and save to paths in destination_file_names
    download_blobs(bucket_name=bucket_name,
                   source_blob_names=source_blob_names,
                   destination_file_names=destination_file_names)

    # 4. Delete the bucket "comp4312_studentid" on gcp
    from storage_delete_bucket import delete_bucket

    delete_bucket(bucket_name, True)



