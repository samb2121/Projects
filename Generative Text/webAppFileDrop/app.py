from flask import Flask, render_template, request, Response, jsonify
import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def index():
    logging.debug("Rendering the index page.")
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'xmlFile' not in request.files:
        return jsonify(error="No file part"), 400

    file = request.files['xmlFile']
    if file.filename == '':
        return jsonify(error="No selected file"), 400

    if file:
        xml_content = file.read().decode('utf-8')

    #print(xml_content)
    
    prompt = f'''From this point forward you are an unbiased and objective police officer. Analyze the XML data and generate a police report narrative from the perspective of the officer involved in the incident. Identify Who, Where, When, What, and infer Why, before crafting the narrative. Provide only the narrative as the result. 
    
Here is the XML Data:

{xml_content}

'''
           
    logging.debug(f"Generated prompt: {prompt}")

    data = {
        "mode": "instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://127.0.0.1:5000/v1/chat/completions', headers=headers, json=data, verify=False)

    complete_text = ""
    response_data = response.json()
    for choice in response_data.get('choices', []):
        complete_text += choice.get('message', {}).get('content', '')

    return jsonify(text=complete_text)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
