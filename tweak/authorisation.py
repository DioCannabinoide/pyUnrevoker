from exploit.restore import FileToRestore, restore_files
import json
from pathlib import Path

class AuthorizationTweak:
    def __init__(self, method="2"):
        print("Initializing Unrevoker authorization...")
        self.rejection_files = []
        self.set_method(method)

    def set_method(self, method):
        self.method = method

    def setup_variables(self, device_manager):
        try:
            with open(Path.joinpath(Path.cwd(), 'tweak/files/restore.json'), 'r') as json_file:
                json_data = json.load(json_file)

            for file_info in json_data["authorization_files"]:
                empty_file = FileToRestore(
                    contents=b'',
                    restore_path=f"/private/var/db/MobileIdentityData/{file_info['filename']}",
                    restore_name=file_info["filename"]
                )
                actual_file = FileToRestore(
                    contents=open(Path.joinpath(Path.cwd(), f'tweak/files/{file_info["filename"]}'), 'rb').read(),
                    restore_path=f"/private/var/db/MobileIdentityData/{file_info['filename']}",
                    restore_name=file_info["filename"]
                )
                self.rejection_files.append({
                    "actual_file": actual_file,
                    "empty_file": empty_file,
                    "file_info": file_info
                })

            if not self.rejection_files:
                print("No valid files to restore.")

        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f"Error during setup: {e}")

    def apply(self, device_manager):
        self.setup_variables(device_manager)
        for file_entry in self.rejection_files:
            actual_file = file_entry["actual_file"]
            file_info = file_entry["file_info"]
            print(f"Restoring {file_info.get('filename')} to /private/var/db/MobileIdentityData/")
            restore_files([actual_file], reboot=False, lockdown_client=device_manager.device.get("ld"))
        restore_files([], reboot=True, lockdown_client=device_manager.device.get("ld"))
