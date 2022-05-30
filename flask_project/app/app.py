#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'MegaFLASK APP FOR SKILLBOX DIPLOMA'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
