# ==============================================================================
# GITHUB PUSH SCRIPT
# Author: Abhishek raj
# ==============================================================================
# This script automates all commands to push the project to GitHub.
# ==============================================================================

import sys
import os

# --- Add the project's 'src' directory to the Python path ---
PROJECT_PATH = "/content/drive/MyDrive/PHD Project/Utensil_Classifier_Project"
SRC_PATH = os.path.join(PROJECT_PATH, "src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from utils import GitManager

def main():
    """Main function to configure and run the GitHub push process."""
    print("--- Preparing to Push Project to GitHub ---")
    
    # ========================= YOUR GITHUB DETAILS GO HERE =========================
    # 1. Create a new, empty repository on GitHub.com and paste the URL here.
    REPO_URL = "https://github.com/TheAbhishekraj/Utensil-Classifier-Jupyter.git"
    
    # 2. Enter your GitHub username and email.
    USERNAME = "TheAbhishekraj"
    EMAIL = "rajabhi2602@gmail.com"
    
    # 3. Write a commit message for this version.
    COMMIT_MESSAGE = "Final version of Jupyter-based application with archived deployment files"
    # ===============================================================================
    
    if "YourUsername" in REPO_URL or "YourGitHubUsername" in USERNAME:
        print("\n⚠️ ATTENTION: Please open 'push_to_github.py' and replace the placeholder GitHub details.")
        return
        
    git_manager = GitManager(project_path=PROJECT_PATH, repo_url=REPO_URL, username=USERNAME, email=EMAIL)
    git_manager.push_to_github(commit_message=COMMIT_MESSAGE)

if __name__ == "__main__":
    main()
