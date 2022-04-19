<div id="top"></div>

<br />
<h2 align="center">Deploying a Streamlit App with Docker</h2>
<br />
</div>

<!-- TABLE OF CONTENTS -->
1. [About the Project](#about-the-project)
2. [Build with](#build-with)
3. [Usage](#usage)
4. [Contact](#contact)

<br />


### About the Project <a id="about-the-project"></a>
This project demonstrates how to deploy a streamlit app with docker.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built with <a id="build-with"></a>
The project was built with **Python 3.9.12** and **Docker version 20.10.14**.
The python requirements are listed in **requirements.txt**.

The main requirements are the following:

* [python](https://www.python.org/)
* [docker](https://www.docker.com/)
* [streamlit](https://streamlit.io/)

<p align="right">(<a href="#top">back to top</a>)</p>


### Usage <a id="usage"></a>
The streamlit app is deployed to port `8080` and can be accessed by [http://localhost:8080](http://localhost:8080).

1. Clone the repository
   ```sh
   git clone https://github.com/SimonReitzner/deploying-a-streamlit-app-with-docker.git
   ```
2. Access folder
   ```sh
   cd deploying-a-streamlit-app-with-docker
   ```
3. Build the docker image
   ```sh
   docker build --tag streamlit:latest .
   ```
4. Start the container
   ```sh
   docker run --detach --restart always -p 8080:8501 streamlit:latest
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


### Contact <a id="contact"></a>
Project Link: [Deploying a Streamlit App with Docker](https://github.com/SimonReitzner/deploying-a-streamlit-app-with-docker)

<p align="right">(<a href="#top">back to top</a>)</p>
