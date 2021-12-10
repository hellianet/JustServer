from flask import Flask, jsonify, abort, request
import logging
from datetime import datetime
import os
import re

MAX_NUMBER_OF_FILES = 10
PATH = "X:/!/1"
# PATH = "C:/Users/krist/PycharmProjects/justServer/hmclog"
CHECK_PATTERN = r'20[0-9][0-9]-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12][0-9]|3[01])T(?:00|1?[1-9]|2[0-4])-[0-5][0-9]-[0-5][0-9]'


def create_log_file_name(date_time):
    date = date_time.strftime('%Y-%m-%dT%H-%M-%S')
    name_file = date + ".log"
    return name_file


def configuration_of_logger(path: str, max_number_of_files: int, level_log):
    fn = create_log_file_name(datetime.now())

    logging.basicConfig(filename=os.path.join(path, fn), level=level_log, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S')

    """ logging.basicConfig(filename=fn, level=level_log, encoding='utf-8', filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')  python 3.9 """


app = Flask(__name__)


@app.route('/')
@app.route('/foo', methods=['GET'])
def foo():
    logging.debug('just some regular stuff')
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
    configuration_of_logger(PATH, MAX_NUMBER_OF_FILES, logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
