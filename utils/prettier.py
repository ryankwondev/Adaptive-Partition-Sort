import os
import subprocess


def code_format(path):
    try:
        target_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".py") and root.find("venv") == -1:
                    target_files.append(os.path.join(root, file))

        for file in target_files:
            command = f"black {file}"
            print(command)
            subprocess.run(command, shell=True)

        print("code_format done")
    except Exception as e:
        print(e)
