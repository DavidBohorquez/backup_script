from pathlib import Path
import platform
import shutil
import datetime
import os

def detect_os():
    return platform.system()

def get_backup_directory():
    home_dir = Path.home()
    buckup_dir = home_dir / "backup"
    backup_dir.mkdir(parents=True, exist_ok=True)
    return backup_dir

def create_backup():
    os_name = detect_os()
    home_dir = Path.home()
    backup_dir = get_backup_directory()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = backup_dir / f"backup_{os_name}_{date_str}"
    
    shutil.make_archive(str(archive_name), 'zip', str(home_dir))
    return str(archive_name) + ".zip"

if __name__ == "__main__":
    archive_path = create_backup()
    print(f"Sauvegarde créée : {archive_path}")
    