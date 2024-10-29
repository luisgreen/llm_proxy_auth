# LLM Proxy with Bearer Authentication

This is a simple Flask application designed to serve as a proxy for Large Language Models (LLMs) like Ollama, while enforcing Bearer authentication. The proxy forwards requests to the underlying LLM API and streams the response back to the client.

**Table of Contents**

- [LLM Proxy with Bearer Authentication](#llm-proxy-with-bearer-authentication)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Running Locally](#running-locally)
    - [Creating a Docker Image](#creating-a-docker-image)
  - [Docker Compose](#docker-compose)

## Prerequisites

To run this proxy, you'll need:

* Python 3.9+
* Flask
* requests library
* A LLM API (e.g., Ollama)
* A random Bearer token 

## Installation

### Running Locally

1. Clone the repository using `git clone git@github.com:luisgreen/llm_proxy_auth.git`
2. Install the required dependencies by running `pip install -r requirements.txt` in the project directory
3. Set environment variables for your LLM API URL and Bearer token:
   
```bash
export LLM_API_URL='https://your-llm-api-url.com/api'
export REQUIRED_BEARER_TOKEN='your-bearer-token'
```
1. Run the proxy using `python proxy.py` in the project directory

### Creating a Docker Image

1. There is an included `Dockerfile`, which you can use to create a Docker image for this proxy. To build and run it, first make sure that you have Docker installed on your machine. 
2. Navigate to the project root folder and run: Run `docker build -t ollama-proxy` in the project directory to create a Docker image

## Docker Compose

To run the proxy with Docker Compose, create a new file named `docker-compose.yml` with the following contents:
```yml
version: '3'
services:
  ollama-proxy:
    build: .
    environment:
      LLM_API_URL: ${LLM_API_URL}
      REQUIRED_BEARER_TOKEN: ${REQUIRED_BEARER_TOKEN}
    ports:
      - "5000:5000"
    depends_on:
      - llm-api
```
In this example, we're assuming you have a separate service for the LLM API. If that's not the case, simply remove the `llm-api` reference.

To run the proxy with Docker Compose:

1. Set environment variables for your LLM API URL and Bearer token:
```bash
export LLM_API_URL='https://your-llm-api-url.com/api'
export REQUIRED_BEARER_TOKEN='your-bearer-token'
```
2. Run `docker-compose up` in the project directory to start the proxy

Now you can access the proxy at `http://localhost:5000`. The proxy will forward requests to your LLM API, enforcing Bearer authentication along the way.

Note that this is just a basic example, and you may want to modify the Docker Compose file to fit your specific use case.
