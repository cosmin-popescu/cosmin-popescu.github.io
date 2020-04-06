from flask import Flask
from skribble_generator import generator``

# TODO - alternative
### SET THIS!
###
### $env:FLASK_APP = "main.py"
###

app = Flask(__name__)

@app.route('/')
def generate():
    generator.WORDS_FILE = "./skribble_generator/input/words.txt"
    generator.ADJECTIVES_FILE = "./skribble_generator/input/adjectives.txt"
    generator.CONJUNCTIONS_FILE =  "./skribble_generator/input/conjunctions.txt"
    
    output, output_hr = generator.Generate(flask=True)

    return output

if __name__ == '__main__':  
     app.run(host='0.0.0.0', debug=True)