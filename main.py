from flask import Flask, jsonify, abort, request
import logging
from datetime import datetime
import os

MAX_NUMBER_OF_FILES = 10
PATH = "C:/Users/krist/PycharmProjects/justServer"


def configuration_of_logger(path : str, max_number_of_files: int, level_log):
    filetype = ['log']
    list_logs = [[f for f in os.listdir(path) if f.endswith(type_)] for type_ in filetype]
    number_of_files_to_log = len(list_logs[0])

    if number_of_files_to_log >= max_number_of_files:
        old_log_file = list_logs[0][0]
        os.remove(old_log_file)

    current_datetime = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
    fn = current_datetime + ".log"

    logging.basicConfig(filename=fn, level=level_log, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S')

    """ logging.basicConfig(filename=fn, level=level_log, encoding='utf-8', filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')  python 3.9 """

app = Flask(__name__)


@app.route('/')
@app.route('/foo', methods=['GET'])
def foo():
    return "Foo!"

@app.route('/admin', methods=['GET'])
def admin_page():
    logging.warning('user request admin page')
    return "admin panel"


@app.route('/nuke', methods=['GET'])
def nuke():
    logging.error('we are f*cked')
    return "bombing target. Stand by.."


if __name__ == '__main__':
    configuration_of_logger(PATH, MAX_NUMBER_OF_FILES,logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
