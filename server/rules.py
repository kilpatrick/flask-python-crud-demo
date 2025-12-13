from flask import Flask, jsonify

from base_responses import BASE_RSP
from auth.decorators import auth_check
from services import rules


app = Flask(__name__)

MOCKED_FOR_DEMO = {
    "jwt": "Not used in demo",
    "permissions": ["Not used in demo"]
}

# ————  Private Routes  ——————
@app.route('/rules', methods=["POST"])
@auth_check
def create_rule():
    rsp_data, metadata = rules.create_rule()
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 501

@app.route('/rules', methods=["GET"])
@auth_check
def read_all_rules():
    rsp_data, metadata = rules.read_all_rules()
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 501

@app.route('/rules/<rule_id>', methods=["GET"])
@auth_check
def read_rule_by_id(rule_id):
    rsp_data, metadata = rules.read_rule_by_id(rule_id)
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 501

@app.route('/rules/<rule_id>', methods=["GET"])
@auth_check
def update_rule_by_id(rule_id):
    rsp_data, metadata = rules.update_rule_by_id(rule_id)
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 501

@app.route('/rules/<rule_id>', methods=["GET"])
@auth_check
def delete_rule_by_id(rule_id):
    rsp_data, metadata = rules.delete_rule_by_id(rule_id)
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 501


# ————  Public Routes  ——————
# WARNING: These are public NO AUTH routes.
# Don't link these to private data!
# ———————————————————————————
@app.route('/status')
def status():
    return { **BASE_RSP, "status": "UP" }, 200
