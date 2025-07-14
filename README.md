<div align="center">
  <img width="70" height="70" alt="image" src="https://github.com/user-attachments/assets/66648b34-8e6e-4324-906c-c48b76f94cad" />
  <h1>Simple RAG (Retrieval Augemented Generation)</h1>

![RAG Logo](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-blueviolet) ![License](https://img.shields.io/github/license/arthurtran04/ibm-2) ![Built with](https://img.shields.io/badge/Built%20With-Python-blue?logo=python)
</div>



## Table of Contents

- [Prerequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Model](#model)
- [Architecture](#architecture)
- [Features](#features)
- [Installation](#installation)
- [How to get API Access Token](#how-to-get-api-access-token)
- [Usage](#usage)
- [License](#license)

## Prerequirements

- ![Python 3.9](https://img.shields.io/badge/Python-3.9-blue) or above: [Download here](https://python.org/downloads)
- Hugging Face account: [Sign up here](https://huggingface.co)

## Project Structure

```
simple-RAG/
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── .gitignore
├── server.py
├── worker.py
├── .env.example
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

## Model

- [HuggingFaceTB/SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) (You can use different models)

## Architecture



## Features

- **Plug-and-Play RAG Pipeline**: Simple to set up and extend for your own datasets.
- **Customizable Retriever**: Easily swap or enhance the retrieval back-end (vector DBs, Elasticsearch, etc.).
- **Modular Generation**: Integrates with your choice of LLM (OpenAI, HuggingFace, etc.).
- **Fast and Lightweight**: Minimal external dependencies, ready for rapid prototyping.
- **Clear Example Usage**: See how to query your own data with just a few lines of code.

## Installation

To install this project, open your Terminal and follow these steps:

1. Clone the repository:

    ```sh
    $ git clone https://github.com/arthurtran04/simple-RAG.git
    ```

2. Change the directory to `simple-RAG`:

    ```sh
    $ cd "$(find . -type d -name "simple-RAG")"
    ```

3. Create a Python virtual environment `.venv` and install the required dependencies:

    ```sh
    $ python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

4. Set up environment variables:

   ```sh
   $ cp .env.example .env
   ```

5. Configure your `.env` file:

   ```env
   # Hugging Face API Token
   HF_TOKEN=
   ```

## How to get API Access Token

<div align="center">
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <p>1. Go to <a href="https://huggingface.co">Hugging Face website</a>, click your avatar and click "Access Tokens"</p>
    <img src="https://github.com/user-attachments/assets/55e6e178-55dd-4b6b-b738-e3c6a9c51206" width="300rem" style="vertical-align: top;" />
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <p>2. Click "Create new token"</p>
    <img src="https://github.com/user-attachments/assets/b4d09f00-da1d-4f4f-b57d-b55293cb7161" width="600rem" style="vertical-align: top;" />
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <p>3. Name your token and tick the two checkboxes in the "Inference" section</p>
    <img src="https://github.com/user-attachments/assets/862828cb-1a02-4d12-8727-26aa5460f006" width="600rem" style="vertical-align: top;" />
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <p>4. Scroll down and click "Create token"</p>
    <img src="https://github.com/user-attachments/assets/14be640c-2c0f-467d-85d9-db3b31b43174" width="600rem" style="vertical-align: top;" />
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <p>5. Copy your Access Token before closing and paste it into the <code>HF_TOKEN</code> variable inside the <code>.env</code> file</p>
    <img src="https://github.com/user-attachments/assets/8a087c0b-51dd-40c2-9576-c9529ed915ed" width="600rem" style="vertical-align: top;" />
  </div>
</div>

## Usage

To start the application, run the `server.py` file:

   ```sh
   $ python server.py
   ```
This application will run locally at `http://127.0.0.1:5000`:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/bb2e62cd-aa9d-4303-ad74-f72e70eaa9c0"/>

Upload your PDF file and enter your prompt in the textbox below, and the chatbot will respond:

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/07cf32c0-3d37-454c-913d-425fd0461319"/>

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
