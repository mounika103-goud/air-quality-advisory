"""Top-level Streamlit entrypoint.

Some hosting platforms (including Streamlit Community Cloud) expect the Streamlit script
to be at the repository root or allow you to point to a single file. This small wrapper
ensures the app can be launched from the repo root as `streamlit run streamlit_app.py`.
"""
from src import app


if __name__ == "__main__":
    # Call the Streamlit app's main() function
    app.main()
