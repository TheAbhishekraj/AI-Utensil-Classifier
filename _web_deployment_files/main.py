# ==============================================================================
# MAIN EXECUTION SCRIPT (FINAL VERSION)
# Author: Abhishek raj
# ==============================================================================
# This is the single entry point to check, run, or deploy the entire project.
#
# How to use from the command line:
#   - To check the setup:  python main.py check
#   - To run the Jupyter app: python main.py run
#   - To deploy to GitHub:    python main.py deploy --repo-url <URL> --username <USER> --email <EMAIL>
# ==============================================================================

import argparse
import sys
import os

# --- Add the project's 'src' directory to the Python path ---
PROJECT_PATH = "/content/drive/MyDrive/PHD Project/Utensil_Classifier_Project"
SRC_PATH = os.path.join(PROJECT_PATH, "src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from utils import WorkflowManager

def main():
    # Create the main parser
    parser = argparse.ArgumentParser(description="Main controller for the Utensil Classifier project.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Create the parser for the "check" command
    parser_check = subparsers.add_parser("check", help="Verify the project setup and file integrity.")

    # Create the parser for the "run" command
    parser_run = subparsers.add_parser("run", help="Set up the environment and run the interactive Jupyter app.")

    # Create the parser for the "deploy" command
    parser_deploy = subparsers.add_parser("deploy", help="Push the entire project to a GitHub repository.")
    parser_deploy.add_argument("--repo-url", required=True, help="The HTTPS URL of the new, empty GitHub repository.")
    parser_deploy.add_argument("--username", required=True, help="Your GitHub username.")
    parser_deploy.add_argument("--email", required=True, help="Your GitHub email.")
    parser_deploy.add_argument("--commit-message", default="Deploy final project version", help="The message for the git commit.")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Create an instance of our master workflow manager
    workflow = WorkflowManager(project_path=PROJECT_PATH)

    # Execute the appropriate command
    if args.command == "check":
        # We access the orchestrator within the workflow to run the verification
        workflow.orchestrator.verify_project_files()
        print("\nVerification complete.")
    elif args.command == "run":
        workflow.run_app()
    elif args.command == "deploy":
        workflow.deploy(
            repo_url=args.repo_url,
            username=args.username,
            email=args.email,
            commit_message=args.commit_message
        )

if __name__ == "__main__":
    main()
