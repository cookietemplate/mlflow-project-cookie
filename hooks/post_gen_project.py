import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def initialize_git_repository():
    try:
        subprocess.check_call(["git", "init"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.check_call(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.check_call(["git", "commit", "-m", "Initial commit"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as error:
        print(error.output)

def check_poetry():
    try:
        subprocess.check_call(["poetry", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.check_call(["poetry", "install"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as error:
        print("Poetry is not installed. Please install Poetry and run 'poetry install' to initialize the project.")
        shutil.rmtree(PROJECT_DIRECTORY)

initialize_git_repository()
check_poetry()
