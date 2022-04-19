# Use/extend python3.9-slim-buster image
FROM python:3.9-slim-buster

# Copy app.py, README.md, requirements.txt and config.toml
COPY ["app.py", "README.md", "requirements.txt", "./"]
COPY config.toml /root/.streamlit/

# Install python dependencies
RUN pip install -r requirements.txt

# Expose the streamlit port
EXPOSE 8501

# Set entrypoint and cmd
ENTRYPOINT ["streamlit", "run"]
CMD [ "app.py" ]