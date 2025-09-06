# ==============================================================================
# UTILITY SCRIPT (FINAL VERSION)
# Author: Abhishek raj
# ==============================================================================
# Contains the ProjectOrchestrator for the Jupyter App and the GitManager for deployment.
# ==============================================================================

import os, sys, subprocess, ipywidgets as widgets, io
from IPython.display import display, clear_output
from PIL import Image
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path: sys.path.append(project_root)
from src import config, predict

class ProjectOrchestrator:
    """Manages the setup and execution of the Jupyter-based app."""
    def __init__(self, project_path):
        self.project_path = project_path
        if not os.path.exists(self.project_path): raise FileNotFoundError(f"Project path not found: {self.project_path}")
        os.chdir(self.project_path)
    def setup_environment(self):
        print("⏳ Installing libraries..."); self._run_command("pip install -r requirements.txt -q && pip install ipywidgets -q"); print("✅ Environment ready.")
        return self
    def verify_project_files(self):
        print("\nVerifying files..."); model_path = os.path.join(config.MODELS_PATH, config.FINE_TUNED_MODEL_NAME)
        if not os.path.exists(model_path): raise FileNotFoundError(f"Model not found: {model_path}")
        print("✅ Trained model present."); return self
    def run_prediction_app(self):
        print("\n🚀 Launching Jupyter App..."); header = widgets.Label('Select an image and click "Classify":'); uploader = widgets.FileUpload(accept='image/*', description='Upload Image', button_style='info'); button = widgets.Button(description='Classify Image', button_style='success', icon='search'); out = widgets.Output()
        def on_button_clicked(b):
            if not uploader.value:
                with out: clear_output(); print("Please upload an image.")
                return
            file_info = next(iter(uploader.value.values())); image_data = file_info['content']
            with out:
                clear_output(); print("Analyzing..."); display(Image.open(io.BytesIO(image_data)))
                model_path = os.path.join(config.MODELS_PATH, config.FINE_TUNED_MODEL_NAME); result = predict.predict_from_image(model_path, image_data)
                clear_output(); display(Image.open(io.BytesIO(image_data)))
                if result["success"]:
                    p, c = result['prediction'].capitalize(), result['confidence']
                    if p == 'Spoon': print(f"Prediction: Spoon 🥄 (Confidence: {c:.2%})")
                    elif p == 'Fork': print(f"Prediction: Fork 🍴 (Confidence: {c:.2%})")
                    else: print(f"Prediction: Other 🤔 (Confidence: {c:.2%})")
                else: print(f"Error: {result['error']}")
        button.on_click(on_button_clicked); display(widgets.VBox([header, uploader, button, out]))
    def _run_command(self, command, check=True): subprocess.run(command, shell=True, check=check)

class GitManager:
    """Manages all Git and GitHub operations."""
    def __init__(self, project_path, repo_url, username, email):
        self.project_path, self.repo_url, self.username, self.email = project_path, repo_url, username, email
        os.chdir(self.project_path)
    def push_to_github(self, commit_message="Final project update"):
        print("🚀 Starting GitHub push process..."); orchestrator = ProjectOrchestrator(self.project_path)
        try:
            print("INFO: Setting up Git LFS..."); orchestrator._run_command("apt-get install git-lfs > /dev/null && git lfs install && git lfs track '*.h5'")
            print("INFO: Initializing repository..."); orchestrator._run_command("git init -b main")
            print("INFO: Configuring Git user..."); orchestrator._run_command(f'git config --global user.name "{self.username}" && git config --global user.email "{self.email}"')
            print("INFO: Adding remote GitHub URL..."); orchestrator._run_command("git remote remove origin", check=False); orchestrator._run_command(f"git remote add origin {self.repo_url}")
            print("INFO: Adding all files..."); orchestrator._run_command("git add .")
            print(f"INFO: Committing files..."); orchestrator._run_command(f'git commit -m "{commit_message}"')
            print("INFO: Pushing files to GitHub..."); orchestrator._run_command("git push -u origin main")
            print("\n✅✅✅ SUCCESS! Your project has been pushed to GitHub.")
        except Exception as e: print(f"\n❌ Error during push: {e}")
