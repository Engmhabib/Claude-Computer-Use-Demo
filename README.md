Claude Computer Use Demo
This Flask application demonstrates how to integrate the Anthropic API with the "Computer Use" feature using Claude 3.5 Sonnet. The application allows users to input prompts, which Claude processes and responds to by executing specified tools.

Features
Real Tool Execution: Executes bash commands and text editing tasks as instructed by Claude.

Enhanced User Interface: A user-friendly chat interface with conversation history.

Security Measures: Restricts dangerous commands and runs commands in a controlled environment.

Prerequisites
Python 3.7 or higher
Anthropic API Key: With access to the "Computer Use" beta feature.
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/claude-computer-use-demo.git
cd claude-computer-use-demo
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up Environment Variables
Set the ANTHROPIC_API_KEY environment variable in your system.

For Unix/Linux:

bash
Copy code
export ANTHROPIC_API_KEY='your_anthropic_api_key'
For Windows (Command Prompt):

cmd
Copy code
set ANTHROPIC_API_KEY=your_anthropic_api_key
5. Run the Application
bash
Copy code
python app.py
Visit http://127.0.0.1:5000 in your web browser.

Usage
Enter Prompts: Type your prompt into the input box and press "Send".

Example Prompts:

"Run the command echo Hello World in bash."

"Replace 'world' with 'Earth' in the text 'Hello world!'"

View Responses: Claude will process your request and display the output.

Security Considerations
Restricted Commands: The application restricts potentially harmful commands.

Execution Timeout: Commands are limited to a 5-second execution time.

Input Validation: Inputs are validated to prevent code injection.

Notes
Sandboxed Environment: For additional security, consider running the application inside a Docker container or virtual machine.

Anthropic API Access: Ensure your API key has the necessary permissions.

Error Handling: The application includes basic error handling. For production use, enhance exception handling and logging.

License
This project is licensed under the MIT License.