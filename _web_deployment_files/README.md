# Web Deployment Files (Archived)

## Purpose
This folder contains all the necessary scripts to run and deploy the Utensil Classifier project as a **standalone Streamlit web application**.

These files are kept separate from the primary Jupyter-based application but are ready to be used for future web deployment.

## Key Files
* `app.py`: The main Streamlit user interface script.
* `main.py`: A command-line entry point to run the app using `python main.py run`.
* `src/utils.py` (in the main `src` folder): Contains the `WorkflowManager` class which is used by `main.py` to launch the Streamlit app.

## How to Use for Future Deployment

When you are ready to deploy this as a web app, follow these steps:

1.  **Review `app.py`:** Ensure it is up-to-date with your latest model.
2.  **Test Locally:** Move `app.py` and `main.py` back to the project's root directory. Run the app using the command:
    ```bash
    streamlit run app.py
    ```
3.  **Deploy:** Push the entire project (with `app.py` in the root) to GitHub and connect it to a service like Streamlit Community Cloud.
