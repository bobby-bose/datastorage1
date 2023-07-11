import os
import requests


def get_files_and_subdirectories_in_directory():
    files_and_subdirectories = os.listdir()
    return files_and_subdirectories


def search_file(file_name):
    files_list = get_files_and_subdirectories_in_directory()
    if file_name in files_list:
        return True
    return False


def print_subdirectories(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print("Subdirectory:", item_path)
            print_subdirectories(item_path)


def save_memory_addresses_to_file(file_path, memory_addresses):
    with open(file_path, 'w') as file:
        for address in memory_addresses:
            file.write(address + '\n')


def upload_file_to_github(file_path, github_repo_url):
    with open(file_path, 'rb') as file:
        response = requests.put(github_repo_url, file)
        if response.status_code == 200:
            print("File uploaded successfully.")
        else:
            print("Failed to upload file.")


if __name__ == "__main__":
    files_and_subdirectories_list = get_files_and_subdirectories_in_directory()
    memory_addresses = []

    print("List of files and subdirectories in the working directory:")
    for item in files_and_subdirectories_list:
        item_path = os.path.abspath(item)
        if os.path.isfile(item_path):
            print("File:", item_path)
            file_stats = os.stat(item_path)
            print("Size:", file_stats.st_size, "bytes")
            memory_addresses.append(str(id(file_stats)))
        elif os.path.isdir(item_path):
            print("Subdirectory:", item_path)
            print_subdirectories(item_path)

    search_file_name = "main.py"
    print("\nSearching for file:", search_file_name)
    if search_file(search_file_name):
        print("File found!")
    else:
        print("File not found.")

    # Save memory addresses to a text file
    addresses_file_path = 'memory_addresses.txt'
    save_memory_addresses_to_file(addresses_file_path, memory_addresses)

    # Upload file to GitHub storage
    github_repo_url = 'https://github.com/bobby-bose/datastorage1/contents/memory_addresses.txt'
    upload_file_to_github(addresses_file_path, github_repo_url)
