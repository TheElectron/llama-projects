from flask import Flask
import ollama

response = ollama.chat(model='llama3',
                        messages=[
                            {
                                'role': 'user',
                                'content': 'Me explique sobre o ciclo de vida das plantas?',
                            },
                        ])

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(response['message']['content'])
    return f"<h3> {response['message']['content']} <\h3> "