import streamlit as st
import zipfile
import os
from io import BytesIO
import shutil


# Function to create a simple Python project
def create_simple_python_project(project_path):
    os.makedirs(os.path.join(project_path, "src"), exist_ok=True)
    with open(os.path.join(project_path, "src/main.py"), "w") as f:
        f.write("# Simple Python Project\n\nif __name__ == '__main__':\n    print('Hello, World!')\n")
    with open(os.path.join(project_path, "requirements.txt"), "w") as f:
        f.write("# Add your project dependencies here\n")


# Function to create a Flask project
def create_flask_project(project_path):
    os.makedirs(os.path.join(project_path, "src"), exist_ok=True)
    with open(os.path.join(project_path, "src/app.py"), "w") as f:
        f.write(
            "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef hello_world():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run()\n")
    with open(os.path.join(project_path, "requirements.txt"), "w") as f:
        f.write("flask\n")


# Function to create a FastAPI project
def create_fastapi_project(project_path):
    os.makedirs(os.path.join(project_path, "src"), exist_ok=True)
    with open(os.path.join(project_path, "src/main.py"), "w") as f:
        f.write(
            "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {'Hello': 'World'}\n")
    with open(os.path.join(project_path, "requirements.txt"), "w") as f:
        f.write("fastapi\nuvicorn\n")


# Function to zip the generated project
def zip_project(project_path):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(project_path):
            for file in files:
                z.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), project_path))
    buffer.seek(0)
    return buffer


# Function to clean up the temporary project directory
def clean_up(project_path):
    shutil.rmtree(project_path, ignore_errors=True)


# Streamlit UI
def main():
    st.set_page_config(page_title="Python Project Generator", page_icon=":snake:")

    st.title(":hammer_and_wrench: Python Project Generator")

    st.markdown("""
    This tool generates Python project boilerplate code based on your selection. Choose one of the options below:
    """)

    project_type = st.selectbox("Select Project Type", ["Simple Python Project", "Flask App", "FastAPI App"])

    if st.button("Generate Project"):
        project_path = "generated_project"
        clean_up(project_path)

        if project_type == "Simple Python Project":
            create_simple_python_project(project_path)
        elif project_type == "Flask App":
            create_flask_project(project_path)
        elif project_type == "FastAPI App":
            create_fastapi_project(project_path)

        zip_buffer = zip_project(project_path)
        clean_up(project_path)

        st.markdown("""
        ### Project Generated Successfully! :rocket:

        Click the button below to download your project as a zip file.
        """)

        st.download_button(
            label="Download Project",
            data=zip_buffer,
            file_name="project.zip",
            mime="application/zip"
        )


# Run the Streamlit app
if __name__ == "__main__":
    main()
