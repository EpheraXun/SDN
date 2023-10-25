from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_script():
    script_name = request.json['script_name']
    
    result = run_script(script_name)
    
    return jsonify(result)

def run_script(script_name):
    # Replace this with the actual command to run script1
    result = subprocess.run(['python', script_name+'.py'], stdout=subprocess.PIPE, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)

