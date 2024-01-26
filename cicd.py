import requests
import time
import subprocess
import os
import multiprocessing
import signal

# Constants
from credgit import GITHUB_TOKEN #YOUR CRED ARE IN A DIFFERENT PYTHON FILE. INCLUDE THIS FILE INTO YOUR .GITIGNORE TO AVOID PUBLICLY SHARE YOUR GITHUB TOKEN ON A REPO.
REPO_OWNER = '' #Your github profile name
REPO_NAME = '' #Your repo name
BRANCH = ''  #Your branch name
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits/{BRANCH}"


# IF YOU'RE HAVING ISSUES RUNNING FLUTER COMMAND. CHECK YOUR PATH. IF IT DOESN'T WORK LIKE FOR ME ON W11.
# TRY THIS VARIABLE; YOU CAN ALSO COMMENT IT AMONG WITH THE TWO LINES BELOW (Line 44, 45)

FLUTTER_PATH = r'D:\Program Files\flutter\bin\flutter.bat'  # Full path to Flutter on my Windows. 


# Initialize the flutter_process variable
flutter_process = None

def get_latest_commit_sha():
    # Headers for GitHub API authentication
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            return response.json()['sha']
        else:
            print(f"Failed to fetch latest commit. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching latest commit: {e}")
        return None

def flutter_commands():
    try:
        print("Current working directory:", os.getcwd())
        subprocess.run(['git', 'pull'])
        #subprocess.run(['flutter', 'clean'])
        #subprocess.Popen(['flutter', 'run'])

        # IF FLUTTER IS NOT IN YOUR PATH OR DOESN'T WORK SOMEHOW
        subprocess.run([FLUTTER_PATH, 'clean'])
        subprocess.Popen([FLUTTER_PATH, 'run'])

    except Exception as e:
        print(f"Failed to execute Flutter commands: {e}")

def execute_flutter_commands():
    global flutter_process
    if flutter_process:
        flutter_process.terminate()
    flutter_process = multiprocessing.Process(target=flutter_commands)
    flutter_process.start()

def main():
    print("Starting commit checker...")
    last_checked_sha = get_latest_commit_sha()
    execute_flutter_commands()  # Execute on initial start

    while True:
        time.sleep(3)
        current_sha = get_latest_commit_sha()
        if current_sha != last_checked_sha:
            print(f"New commit detected (SHA: {current_sha}). Executing Flutter commands.")
            execute_flutter_commands()
            last_checked_sha = current_sha

if __name__ == '__main__':
    main()
