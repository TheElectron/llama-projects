from flask import Flask, request, jsonify, render_template
from utils import get_llama_response

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('chat.html')
#    return render_template('index.html')

@app.route('/handle_message', methods=['POST'])
def handle_message():
    message = request.json['message']
    response = get_llama_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
