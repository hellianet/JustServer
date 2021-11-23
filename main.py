from flask import Flask, jsonify, abort, request
import logging
from datetime import datetime
import os

MAX_NUMBER_OF_FILES = 10
PATH = "C:/Users/krist/PycharmProjects/justServer"

filetype = ['log']
list_logs = [[f for f in os.listdir(PATH) if f.endswith(type_)] for type_ in filetype]
number_of_files_to_log = len(list_logs[0])

if number_of_files_to_log >= MAX_NUMBER_OF_FILES:
    old_log_file = list_logs[0][0]
    os.remove(old_log_file)

current_datetime = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
fn = current_datetime + ".log"

logging.basicConfig(filename=fn, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S')

app = Flask(__name__)

@app.route('/')
@app.route('/foo', methods=['GET'])
def foo():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
