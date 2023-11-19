#!/usr/bin/env python3
# app.py

from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)
client = openai.OpenAI()

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    data = request.form

    # Assemble parameters, ensuring defaults where needed
    params = {
      'prompt': data['prompt'],
      'n': int(data.get('n', 1)),
      'size': data.get('size', '1024x1024')
    }

    if 'model' in data:
      params['model'] = data['model']
    if 'quality' in data and data['model'] == 'dall-e-3':
      params['quality'] = data['quality']
    if 'response_format' in data:
      params['response_format'] = data['response_format']
    if 'style' in data and data['model'] == 'dall-e-3':
      params['style'] = data['style']
    if 'user' in data:
      params['user'] = data['user']

    response = client.images.generate(**params)
    image_url = response.data[0].url
    return jsonify({'image_url': image_url})

  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)

