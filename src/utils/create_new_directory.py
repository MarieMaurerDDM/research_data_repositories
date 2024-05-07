import os


def create_new_directory(directory_path):
    # Check if the directory already exists
    if not os.path.exists(directory_path):
        # Create a directory to store records
        os.makedirs(directory_path)

    return directory_path
