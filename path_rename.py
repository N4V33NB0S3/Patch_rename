import os
import re


def rename_files(directory):
    video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v')

    for filename in os.listdir(directory):
        if filename.lower().endswith(video_extensions):
            name, ext = os.path.splitext(filename)
            clean_name = re.sub(r'[._]',' ', name)

            new_filename = clean_name.strip() + ext 

            if new_filename == filename:
                continue

            counter = 1
            while os.path.exists(os.path.join(directory, new_filename)):
                new_filename = f"{clean_name} ({counter}){ext}"
                counter += 1
            
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)
            print(f'Renamed {filename} --> {new_filename}')
            
if __name__ == '__main__':
    folder_path = input("directory of video files:").strip().strip("'\"")

    if os.path.isdir(folder_path):
        rename_files(folder_path)
        print("File renaming completed!")
