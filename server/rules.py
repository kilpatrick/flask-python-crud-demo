from flask import Flask, jsonify, request

from base_responses import BASE_RSP
from auth.decorators import auth_check
from services import rules


app = Flask(__name__)


# TODO: School ID should be pulled from token: jwt["organization"]["id"]
# HARDCODED_SCHOOL_ID = "dfbbf5e3-76cf-4a85-ba29-c47686d4d886"


# ————  Private Routes  ——————
@app.route('/rules', methods=["POST"])
@auth_check
def create_rule(decoded_token):
    request_body = request.get_json()
    school_id = decoded_token.get("organization", {}).get("id")
    rsp_data, metadata = rules.create_rule(school_id. request_body)
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 200

@app.route('/rules', methods=["GET"])
@auth_check
def read_all_rules(decoded_token):
    school_id = decoded_token.get("organization", {}).get("id")
    rsp_data, metadata = rules.read_all_rules(school_id)
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 200

@app.route('/rules/<rule_id>', methods=["GET"])
@auth_check
def read_rule_by_id(decoded_token, rule_id):
    school_id = decoded_token.get("organization", {}).get("id")
    rsp_data, metadata = rules.read_rule_by_id(school_id, rule_id)
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 200

@app.route('/rules/<rule_id>', methods=["PATCH"])
@auth_check
def update_rule_by_id(decoded_token, rule_id):
    school_id = decoded_token.get("organization", {}).get("id")
    request_body = request.get_json()
    rsp_data, metadata = rules.update_rule_by_id(school_id, rule_id, request_body)
    response = { **BASE_RSP, "body": rsp_data, "metadata": metadata }
    return jsonify(response), 200

@app.route('/rules/<rule_id>', methods=["DELETE"])
@auth_check
def delete_rule_by_id(decoded_token, rule_id):
    school_id = decoded_token.get("organization", {}).get("id")
    rsp_data, metadata = rules.delete_rule_by_id(school_id, rule_id)
    response = { **BASE_RSP, "status": rsp_data, "metadata": metadata }
    return jsonify(response), 200


# ————  Public Routes  ——————
# WARNING: These are public NO AUTH routes.
# Don't link these to private data!
# ———————————————————————————
@app.route('/status')
def status():
    return { **BASE_RSP, "status": "UP" }, 200
