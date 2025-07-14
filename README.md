# Chatbot Application using DeepSeek-V3 model

## Introduction

This repository presents a **Chatbot Application** powered by the **DeepSeek-V3 model**. Designed with a mix of **CSS**, **JavaScript**, **Python**, and **HTML**, it combines visually appealing design with intelligent conversational capabilities. The project exemplifies the seamless integration of AI-driven dialogue systems with a polished user experience.

## Table of Contents

- [Introduction](#introduction)
- [Prerequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Model](#model)
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
chatbot/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── script.js
│   └── icons...
├── templates/
│   └── index.html
├── .gitignore
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Model

- [deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3)

## Features

- Chatbot Application using DeepSeek-V3 model from Hugging Face
- Using Flask for back-end development
- Using Pylint for code analysis

## Installation

To install this project, open your Terminal and follow these steps:

1. Clone the repository:

    ```sh
    $ git clone https://github.com/arthurtran04/chatbot.git
    ```

2. Change the directory to `chatbot`:

    ```sh
    $ cd "$(find . -type d -name "chatbot")"
    ```

3. Create a Python virtual environment `venv` and install the required dependencies:

    ```sh
    $ python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. Create a `.env` file to save your API token:

   ```sh
   $ touch .env
   echo "API_TOKEN=" > .env
   ```

## How to get API Access Token

<p align="center">
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
    <p>5. Copy your Access Token before closing and paste it into the <code>API_TOKEN</code> variable inside the <code>.env</code> file</p>
    <img src="https://github.com/user-attachments/assets/8a087c0b-51dd-40c2-9576-c9529ed915ed" width="600rem" style="vertical-align: top;" />
    <img src="https://github.com/user-attachments/assets/b3c16ac9-f538-44fe-a14f-55800e30d53d" width="600rem" style="vertical-align: top;" />
  </div>
</p>

## Usage

To start the application, run the `app.py` file:

   ```sh
   $ python app.py
   ```
This application will run locally at `http://127.0.0.1:5000`:

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/924a34a2-712d-44a6-8a8d-6f47b35c6b5b"/>

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/bb2e62cd-aa9d-4303-ad74-f72e70eaa9c0"/>

Enter your prompt in the textbox below, and the chatbot will respond:

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/07cf32c0-3d37-454c-913d-425fd0461319"/>

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
