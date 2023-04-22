import os.path
import subprocess


def make_requirements_txt(path):
    try:
        command = f"pip freeze > {os.path.join(path, 'requirements.txt')}"
        subprocess.run(command, shell=True)

        print("requirements.txt done")
    except Exception as e:
        print(e)
