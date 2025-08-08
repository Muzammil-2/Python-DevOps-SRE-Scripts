import shutil    # copying,moves and deleting files, directories.
import datetime  # timestamp
import os        # perform activity on os platform to create files and directories.

def backup_files(source, destination):
    today = datetime.date.today() # 2025-01-15
    backup_file_name = os.path.join(destination,f"backup_{today}.gz")# backup_2025-01-15.tar.gz.tar.gz
    shutil.make_archive(backup_file_name,'gztar',source)
    print("backup_file_name")


source = "/f/Dec"
destination = "/f/Python/jan"
backup_files(source,destination)