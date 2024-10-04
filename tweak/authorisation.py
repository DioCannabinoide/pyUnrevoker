from exploit.restore import FileToRestore, restore_files
import json
from pathlib import Path
from pymobiledevice3.services.installation_proxy import InstallationProxyService

class UnrevokeTweak:
    def __init__(self):
        print("Initializing...")
        self.files = []

    def setup_variables(self, dev_manager):
        try:
            with open(Path.joinpath(Path.cwd(), 'tweak/files/restore.json'), 'r') as json_file:
                json_data = json.load(json_file)

            for file_info in json_data["restore_files"]:
                file_to_unrevoke = FileToRestore(
                    contents=open(Path.joinpath(Path.cwd(), f'tweak/files/{file_info["file"]}'), 'rb').read(),
                    restore_path="/private/var/db/MobileIdentityData/",
                    restore_name=file_info["file"]
                )
                self.files.append(file_to_unrevoke)

            if not self.files:
                print("No valid files to unrevoke.")

        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f"Error during setup: {e}")

    def apply(self, dev_manager):
        self.setup_variables(dev_manager)
        for file in self.files:
            print(f"Unrevoking {file.restore_name} to {file.restore_path}")
            restore_files([file], reboot=False, lockdown_client=dev_manager.device.get("ld"))
        restore_files([], reboot=True, lockdown_client=dev_manager.device.get("ld"))
