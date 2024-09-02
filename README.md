


Joke Generator App
This is a Flask web application that generates jokes based on user-provided topics. The app uses a fine-tuned GPT-2 model from the transformers library to generate contextually relevant and humorous content.

Features
User Input: Users can enter a topic or keyword, and the app will generate a joke related to that topic.
NLP Model: The app leverages a fine-tuned GPT-2 LMHeadModel for joke generation.
Responsive UI: A simple and user-friendly web interface built with Flask.
Requirements
To run this app locally, ensure you have the following installed:

Python 3.x
Flask
Transformers (Hugging Face)
PyTorch
Joblib
Pandas

You can install the required Python packages using pip:

pip install flask transformers torch joblib pandas

Run the Application:
python model.py

Set the data pre processing file path in ipynb file in jupyter notebook then pre process the file and dump the processed csv file, prepare the file for model traning here using GPT2LMHeadModel is hugging face library provided by transfoemrer library then select following files:
1. config.json
2. merges.txt
3. model.safetensors
4. tokenizer_conifg.json
5. vocab.json
and then place this all in the folder named fine-tuned-gpt2 and then open model.py file and set the path in line 10 and then same goes for index.html file also located in templates file, create a template file for index.html if there is not there and then fir up model.py app from terminal or code runner you will see like this Open your web browser and navigate to http://127.0.0.1:5000/ to use the app.
it means the app is running succesfully and welcomed by this screen
![image](https://github.com/user-attachments/assets/f1cb5ad6-3d6d-4d44-9e68-b37a7e6b86cf)
![image](https://github.com/user-attachments/assets/11ddd218-4019-4e4b-89c6-4b1488594af4)

