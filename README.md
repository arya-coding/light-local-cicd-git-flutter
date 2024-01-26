
# Light Local CI/CD for Flutter with Git


Automate the Flutter development workflow by checking for new commits in a specific Git branch and executing Flutter commands accordingly. It uses a Python script to periodically check for new commits and, upon detecting a change, runs a series of Flutter commands to ensure the local environment is up-to-date with the latest codebase. It runs smoothly on W11 with Flutter 3.x, and a Samsung Android 13 connected in USB C for real debug device tests. All Flutter logs are shown in the terminal. 

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- Git installed and configured.
- Flutter SDK installed and properly set up.
- A GitHub Personal Access Token with appropriate permissions set in `credgit.py` as `GITHUB_TOKEN`.

## Installation
To install `light-local-cicd-git-flutter`, follow these steps:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/arya-coding/light-local-cicd-git-flutter.git
   ```
2. Navigate to the cloned repository:
   ```bash
   cd light-local-cicd-git-flutter
   ```
3. (Optional) Adjust `FLUTTER_PATH` in the script if Flutter is not added to your system's PATH or doesn't work like me on W11.

## Usage
To use `light-local-cicd-git-flutter`, run the main Python script:
```bash
python cicd.py
```
The script will start monitoring the specified Git branch for new commits every 3 seconds. Upon detecting a new commit, it will automatically run `flutter clean` and `flutter run` to reflect the latest changes in your local Flutter environment.

## Contributing
Contributions to the `light-local-cicd-git-flutter` project are welcome. Before contributing, please ensure you have discussed your intended changes via issue.

