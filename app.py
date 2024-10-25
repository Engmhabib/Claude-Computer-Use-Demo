import os
import uuid
import json
import requests
import threading
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Retrieve the Anthropic API key from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Ensure the API key is set
if not ANTHROPIC_API_KEY:
    raise ValueError("The ANTHROPIC_API_KEY environment variable is not set.")

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-3-5-sonnet-20241022"

HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": ANTHROPIC_API_KEY,
    "Anthropic-Version": "2023-06-01",
    "Anthropic-Beta": "computer-use-2024-10-22"
}

TOOLS = [
    {
        "type": "computer_20241022",
        "name": "computer",
        "display_width_px": 1024,
        "display_height_px": 768,
        "display_number": 1
    },
    {
        "type": "text_editor_20241022",
        "name": "str_replace_editor"
    },
    {
        "type": "bash_20241022",
        "name": "bash"
    }
]

conversation_history = {}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_prompt = request.form['prompt']
    conversation_id = request.form.get('conversation_id', str(uuid.uuid4()))
    messages = conversation_history.get(conversation_id, [])
    messages.append({"role": "user", "content": user_prompt})
    response = converse_with_claude(messages)
    conversation_history[conversation_id] = messages
    return jsonify({"response": response, "conversation_id": conversation_id})

def converse_with_claude(messages):
    while True:
        payload = {
            "model": MODEL,
            "max_tokens": 1024,
            "tools": TOOLS,
            "messages": messages
        }

        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            data = response.json()

            if 'completion' in data:
                assistant_message = data['completion']
                stop_reason = data.get('stop_reason', '')

                if stop_reason == 'tool_use':
                    # Extract tool request
                    tool_request = assistant_message.strip()
                    # Execute the tool and get the result
                    tool_result = execute_tool(tool_request)
                    # Append the assistant's message and the tool result to the messages
                    messages.append({"role": "assistant", "content": assistant_message})
                    messages.append({"role": "user", "content": f"<tool_result>{tool_result}</tool_result>"})
                else:
                    # Append the assistant's message to the messages and return it
                    messages.append({"role": "assistant", "content": assistant_message})
                    return assistant_message
            else:
                error_message = data.get('error', {}).get('message', 'Unknown error.')
                return f"Error in API response: {error_message}"
        except Exception as e:
            return f"Exception occurred during API call: {str(e)}"

def execute_tool(tool_request):
    """
    Parses the tool request and executes the appropriate tool.
    """
    try:
        # Remove <tool> tags if present
        tool_request = tool_request.replace('<tool>', '').replace('</tool>', '')
        # Parse the tool request
        tool_data = json.loads(tool_request)
        tool_name = tool_data.get('name')
        tool_input = tool_data.get('input', '')

        if tool_name == 'bash':
            return execute_bash(tool_input)
        elif tool_name == 'str_replace_editor':
            return execute_text_editor(tool_input)
        elif tool_name == 'computer':
            return execute_computer_tool(tool_input)
        else:
            return "Unknown tool requested."
    except Exception as e:
        return f"Error executing tool: {str(e)}"

def execute_bash(command):
    """
    Executes a bash command in a restricted shell.
    """
    try:
        # Security measure: Restrict dangerous commands
        restricted_commands = ['rm', 'shutdown', 'reboot', 'sudo', 'wget', 'curl', 'dd', 'mkfs', '>:']
        if any(cmd in command for cmd in restricted_commands):
            return "Command contains restricted operations."

        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=5, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Command error: {e.output}"
    except subprocess.TimeoutExpired:
        return "Command timed out."

def execute_text_editor(input_data):
    """
    Simulates text editing by performing string replacements.
    """
    try:
        if isinstance(input_data, str):
            input_data = json.loads(input_data)
        text = input_data.get('text', '')
        find = input_data.get('find', '')
        replace = input_data.get('replace', '')
        if not all([text, find, replace]):
            return "Text editor input is incomplete."
        updated_text = text.replace(find, replace)
        return updated_text
    except Exception as e:
        return f"Error in text editor: {str(e)}"

def execute_computer_tool(input_data):
    """
    Simulates computer interactions.
    """
    # For demonstration, we'll return a placeholder message.
    return "Executed computer tool (GUI interactions are not implemented in this demo)."

if __name__ == '__main__':
    app.run(debug=True)
