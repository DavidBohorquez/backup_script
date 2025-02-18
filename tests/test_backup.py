import pytest
import backup
import shutil
from pathlib import Path

def test_detect_os():
    assert backup.detect_os() in ["Windows", "Linux", "Darwin"]
    
def test_get_backup_directory(mocker):
    mock_home = Path("/tmp/fake/home")
    mocker.patch("pathlib.Path.home", return_value=mock_home)

    backup_dir = backup.get_backup_directory()
    assert backup_dir == Path("/fake/home/backup")

def test_create_backup(mocker):
    mocker.patch("backup.detect_os", return_value="Linux")
    mocker.patch("backup.get_backup_directory", return_value=Path("/fake/backup"))
    mocker.patch("pathlib.Path.home", return_value=Path("/fake/backup"))

    mock_make_archive = mocker.patch("shutil.make_archive", return_value="/fake/backup/backup.zip")

    archive_path = backup.create_backup()
    assert archive_path == Path("/fake/backup/backup_Linux.zip")

    mock_make_archive.assert_called_once_with("/fake/backup/backup_Linux.zip", 'zip', "/fake/backup") 