import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_dir(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

def main():
    project_type = '{{cookiecutter.project_type}}'
    
    subfolders = ["python_ai_agent"]

    for folder in subfolders:
        if folder != project_type:
            remove_dir(os.path.join(PROJECT_DIRECTORY, folder))

    chosen_path = os.path.join(PROJECT_DIRECTORY, project_type)
    if os.path.exists(chosen_path):
        for item in os.listdir(chosen_path):
            shutil.move(os.path.join(chosen_path, item), PROJECT_DIRECTORY)
        remove_dir(chosen_path)

if __name__ == '__main__':
    main()
