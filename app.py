import streamlit as st
from streamlit import cli as stcli
import sys

# Load the content of the streamlit app (for the sake of simplicity let us take the README.md file)
with open("README.md", mode="r") as f:
    content = f.read()

# Create app
def main():
    """Function to create the streamlit app"""
    st.markdown(content, unsafe_allow_html=True)


if __name__ == "__main__":
    # Start the app for development
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())