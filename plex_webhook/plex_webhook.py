from flask import Flask, request
import json
from utils import get_logger, processEvent

app = Flask("Webhook")
logger = get_logger()

@app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH'])
def index():
    payload = request.form.get('payload')
    output = processEvent(payload)
    req_data = request.get_json()
    str_obj = json.dumps(req_data)
    if request.method == 'GET':
        return '<h1>PLEX WEBHOOK</h1>'
    if request.method == 'POST':
            return {'POST': str_obj}
    if request.method == 'PUT':
            return {'PUT': str_obj}
    if request.method == 'PATCH':
            return {'PATCH': str_obj}

app.run(host='0.0.0.0', port=4200, threaded=True, debug=True)