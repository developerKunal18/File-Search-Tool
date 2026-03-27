import os

folder_path = input("Enter folder path: ")
target_file = input("Enter file name to search: ")

found = False

for root, dirs, files in os.walk(folder_path):
    if target_file in files:
        print("\nFile found at:")
        print(os.path.join(root, target_file))
        found = True

if not found:
    print("File not found.")
