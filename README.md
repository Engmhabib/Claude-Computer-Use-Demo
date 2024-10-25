# Claude Computer Use Demo

This Flask application demonstrates how to integrate the Anthropic API with the **"Computer Use"** feature using **Claude 3.5 Sonnet**. The application allows users to input prompts, which Claude processes and responds to by executing specified tools.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create a New Conda Environment](#2-create-a-new-conda-environment)
  - [3. Activate the Environment](#3-activate-the-environment)
  - [4. Install Dependencies](#4-install-dependencies)
  - [5. Set Up Environment Variables](#5-set-up-environment-variables)
  - [6. Run the Application](#6-run-the-application)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
  - [Insufficient Credits Error](#insufficient-credits-error)
- [Security Considerations](#security-considerations)
- [Notes](#notes)
- [License](#license)

---

## Features

- **Real Tool Execution**: Executes bash commands and text editing tasks as instructed by Claude.
- **Enhanced User Interface**: A user-friendly chat interface with conversation history.
- **Security Measures**: Restricts dangerous commands and runs commands in a controlled environment.
- **Troubleshooting Steps**: Guidance on resolving common issues, including API authentication and billing errors.

---

## Prerequisites

- **Python 3.7** or higher
- **Anaconda** installed on your system
- **Anthropic API Key**: With access to the "Computer Use" beta feature and sufficient credits

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/claude-computer-use-demo.git
cd claude-computer-use-demo
```

**Note**: Replace `yourusername` with your GitHub username if you have forked the repository.

---

### 2. Create a New Conda Environment

Create a new environment named `claude_env` with Python 3.9:

```bash
conda create -n claude_env python=3.9
```

---

### 3. Activate the Environment

```bash
conda activate claude_env
```

---

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### 5. Set Up Environment Variables

#### For Windows (Command Prompt or Anaconda Prompt):

```bash
set ANTHROPIC_API_KEY=your_anthropic_api_key
```

#### For Unix/Linux/MacOS:

```bash
export ANTHROPIC_API_KEY='your_anthropic_api_key'
```

**Important**:

- Replace `your_anthropic_api_key` with your actual Anthropic API key.
- Ensure you set the environment variable in the same terminal session where you will run the application.
- Do **not** include quotes around the API key on Windows.

---

### 6. Run the Application

```bash
python app.py
```

You should see output indicating the server is running:

```
* Serving Flask app 'app'
* Debug mode: on
...
* Running on http://127.0.0.1:5000
```

---

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.

2. You will see a chat interface where you can interact with Claude.

3. **Enter Prompts**: Type your prompt into the input box and press "Send".

   **Example Prompts**:

   - `"Run the command 'echo Hello World' in bash."`
   - `"Replace 'world' with 'Earth' in the text 'Hello world!'"`

4. **View Responses**: Claude will process your request and display the output.

---

## Troubleshooting

### Common Issues

#### 1. `ANTHROPIC_API_KEY` is `None`

- **Cause**: The environment variable is not set or not accessible.

- **Solution**:

  - Ensure you set the `ANTHROPIC_API_KEY` environment variable in the same terminal session.
  - Do not include extra spaces or quotes when setting the variable on Windows.
  - Restart the Flask app after setting the variable.

#### 2. Authentication Error: `'x-api-key header is required'`

- **Cause**: The API key is missing or not being sent in the request headers.

- **Solution**:

  - Verify that `ANTHROPIC_API_KEY` is set and not `None`.
  - Ensure the headers in `app.py` are correctly set with proper capitalization.

#### 3. Invalid API Key or Permissions Error

- **Cause**: The API key is incorrect or lacks necessary permissions.

- **Solution**:

  - Double-check your API key for typos.
  - Ensure your API key has access to the "Computer Use" beta feature.

#### 4. Module Not Found Errors

- **Cause**: Required packages are not installed in the environment.

- **Solution**:

  - Activate the correct Conda environment.
  - Install dependencies using `pip install -r requirements.txt`.

---

### Insufficient Credits Error

If you receive an error message like:

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits."
  }
}
```

#### **Solution**:

1. **Check Your Anthropic Account Balance**:

   - Log in to your Anthropic account.
   - Navigate to the **Plans & Billing** section.
   - Verify your current credit balance.

2. **Purchase Credits or Upgrade Your Plan**:

   - If your balance is low, purchase additional credits.
   - Consider upgrading your plan if necessary.

3. **Ensure Beta Feature Access**:

   - Confirm you have access to the "Computer Use" beta feature.
   - Request access from Anthropic if needed.

4. **Retry the Application**:

   - After resolving billing issues, restart the Flask app.
   - Test the application to ensure it's working correctly.

---

## Security Considerations

- **API Key Confidentiality**:

  - Do not expose your Anthropic API key in code repositories, logs, or console outputs.
  - Remove or comment out any `print` statements that display the API key in `app.py`.

- **Command Execution Safety**:

  - The application restricts dangerous commands to prevent harmful operations.
  - Commands are executed with limited privileges and timeouts.

- **Sandboxed Environment**:

  - For added security, consider running the application inside a Docker container or virtual machine.

---

## Notes

- **Environment Activation**:

  - Always activate your Conda environment before running the application.

- **Dependencies**:

  - Ensure all dependencies in `requirements.txt` are installed.

- **Anthropic API Access**:

  - Confirm that your API key is valid and has the necessary permissions.

- **Error Handling**:

  - The application includes basic error handling. For production use, enhance exception handling and logging as needed.

---

## License

This project is licensed under the MIT License.

---

## Additional Resources

- **Anthropic API Documentation**: [Anthropic API Docs](https://docs.anthropic.com/)
- **Flask Documentation**: [Flask Docs](https://flask.palletsprojects.com/)
- **Anaconda Documentation**: [Anaconda Docs](https://docs.anaconda.com/)

---

## Acknowledgments

This project is based on integrating Anthropic's Claude 3.5 Sonnet with a Flask application to demonstrate the "Computer Use" feature.

---

**Disclaimer**: Always exercise caution when executing code or commands received from any external source, including AI models. Ensure that appropriate security measures are in place to protect your system.

---

**Contact**: For any questions or issues regarding this project, please open an issue on GitHub or reach out to the project maintainer.

---
