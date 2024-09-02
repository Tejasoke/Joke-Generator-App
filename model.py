from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Load the fine-tuned model and tokenizer
model_directory = 'fine-tuned-gpt2'
model = GPT2LMHeadModel.from_pretrained(model_directory)
tokenizer = GPT2Tokenizer.from_pretrained(model_directory)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_joke', methods=['POST'])
def generate_joke():
    data = request.get_json()
    topic = data.get('topic', '')

    # Use your model to generate a joke based on the topic
    # Example: generate a joke using the model (modify as needed)
    input_ids = tokenizer.encode(topic, return_tensors='pt')
    output = model.generate(input_ids, max_length=50)
    joke = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({'joke': joke})

if __name__ == '__main__':
    app.run(debug=True)
