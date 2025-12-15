from datetime import datetime, timezone

from rules_engine.parse_rule import get_rule_conditions
from rules_engine.evaluator import evaluate_rule_dangerously
from db.seed_data import db_seed


# ------------------------------------------------------
# Setting up a database that can be easily distributed, seeded, and
# run on all devices of the consumers of this demo is outside scope.
# DB interactions are handwaved. This of course isn't how a prod DB
# interaction occurs. Assume proper relational db like postgresql w/
# all the typical defaults and safeguards.
MOCKED_DB = db_seed
TODO_METADATA = {
  "current_page": None,
  "page_size": None,
  "total_pages": None,
  "total_records": None,
}
# ------------------------------------------------------


def create_rule(school_id: str, request_body: dict) -> [dict, dict]:
  import uuid
  new_id = str(uuid.uuid4())
  now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
  new_rule = {
    "id": new_id,
    "school_id": school_id,
    "created_at": now,
    "updated_at": now,
    "deleted_at": None,
    **request_body
  }
  MOCKED_DB["rules"][new_id] = new_rule
  return new_rule, TODO_METADATA

def read_all_rules(school_id: str) -> [dict, dict]:
  rules_filtered_by_school = []
  for rule_id in MOCKED_DB["rules"]:
    record = MOCKED_DB["rules"][rule_id]
    row_school_id = record.get("school_id")
    if school_id  and record.get("deleted_at") == None and row_school_id and row_school_id == school_id:
      rules_filtered_by_school.append(record)
  return rules_filtered_by_school, TODO_METADATA

def read_rule_by_id(school_id: str, rule_id: str) -> [dict, dict]:
  record = MOCKED_DB["rules"][rule_id]
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    return record, TODO_METADATA
  return None, TODO_METADATA

def update_rule_by_id(school_id: str, rule_id: str, update_body: dict) -> [dict, dict]:
  record = MOCKED_DB["rules"].get(rule_id)
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    # WARNING: Remember there's lots of handwaving going on here. This is going to allow for
    # things like the user changing the UUID of records which is a terrible, horrible thing.
    # Don't actually do that.
    updated_record = {**MOCKED_DB["rules"][rule_id], **update_body}
    updated_record["updated_at"] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    MOCKED_DB["rules"][rule_id] = updated_record
    return MOCKED_DB["rules"][rule_id], TODO_METADATA
  return None, TODO_METADATA

def delete_rule_by_id(school_id: str, rule_id: str) -> [dict, dict]:
  record = MOCKED_DB["rules"][rule_id]
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    mocked_cur_date_getter_setter = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    updated_record = {**MOCKED_DB["rules"][rule_id], "deleted_at": mocked_cur_date_getter_setter}
    MOCKED_DB["rules"][rule_id] = updated_record
    return "Record Deleted", TODO_METADATA
  return None, TODO_METADATA

# Special Case: This is for easy testing, but would happen on App submission in a real use case.
# This is the equivalent of a `--dry-run` flag to show the details about what the rules engine
# would have decided had it really been triggered.
def trigger_rule_dry_run(school_id: str, rule_id: str) -> [dict, dict]:
  record = MOCKED_DB["rules"][rule_id]
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:

    # MOCKED Family info
    TODO_family_details_MOCKED = MOCKED_DB["families"]["8b6df376-0690-4b59-9208-00a8209904db"]

    # Rules
    record = MOCKED_DB["rules"][rule_id]
    formula = record.get("formula")
    truth_table = get_rule_conditions(formula, TODO_family_details_MOCKED)
    final_eval = evaluate_rule_dangerously(formula, truth_table)

    # Actions
    action_id = record.get("action_id")
    action_name = MOCKED_DB["actions"][action_id].get("name")
    doc_id_tied_to_action = MOCKED_DB["actions"][action_id].get("document_id")

    # --dry-run vals
    dry_run_body = {
      "action_id": action_id,
      "action_name": None,
      "doc_id_tied_to_action": doc_id_tied_to_action,
      "family_info_used": TODO_family_details_MOCKED,
      "final_eval": final_eval,
      "formula ": formula,
      "rule_id": rule_id,
      "truth_table": truth_table,
    }
    return dry_run_body, TODO_METADATA
  return None, TODO_METADATA
