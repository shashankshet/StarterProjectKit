# StarterProjectKit

StarterProjectKit is a simple web application built with Streamlit that allows users to generate boilerplate code for different types of Python projects. It provides options to create a simple Python project, a Flask web application, or a FastAPI API project. Each generated project includes necessary files such as `main.py`, `app.py` (for Flask), and `requirements.txt`.

## Features

- **Simple Python Project**: Generates a basic Python project with a `main.py` file and an empty `requirements.txt`.
- **Flask App**: Generates a Flask web application with a basic `app.py` file that includes a simple "Hello, World!" route and installs `flask` in `requirements.txt`.
- **FastAPI App**: Generates a FastAPI API project with a `main.py` file that includes a simple root endpoint and installs `fastapi` and `uvicorn` in `requirements.txt`.

## Usage

1. **Select Project Type**: Choose the type of project you want to generate from the dropdown menu.
2. **Generate Project**: Click on the "Generate Project" button to create the selected project type.
3. **Download Project**: Once generated, click the "Download Project" button to download the project as a zip file.

## Installation

To run the Python Project Generator locally, ensure you have Python installed. Then, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd python-project-generator
   ```
   
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    Run the Streamlit app
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Access the application in your web browser at http://localhost:8501

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.