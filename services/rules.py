from datetime import datetime, timezone

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


def create_rule() -> [dict, dict]:
  return None, TODO_METADATA

def read_all_rules(school_id: str) -> [dict, dict]:
  rules_filtered_by_school = []
  for rule_id in db_seed["rules"]:
    record = db_seed["rules"][rule_id]
    row_school_id = record.get("school_id")
    if school_id  and record.get("deleted_at") == None and row_school_id and row_school_id == school_id:
      rules_filtered_by_school.append(record)
  return rules_filtered_by_school, TODO_METADATA

def read_rule_by_id(school_id: str, rule_id: str) -> [dict, dict]:
  record = db_seed["rules"][rule_id]
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    return record, TODO_METADATA
  return None, TODO_METADATA

def update_rule_by_id(school_id: str, rule_id: str, update_body: dict) -> [dict, dict]:
  record = db_seed["rules"][rule_id]
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    # WARNING: Remember there's lots of handwaving going on here. This is going to allow for
    # things like the user changing the UUID of records which is a terrible, horrible thing.
    # Don't actually do that.
    updated_record = {**db_seed["rules"][rule_id], **update_body}
    db_seed["rules"][rule_id] = updated_record
    return db_seed["rules"][rule_id], TODO_METADATA
  return None, TODO_METADATA

def delete_rule_by_id(school_id: str, rule_id: str) -> [dict, dict]:
  record = db_seed["rules"][rule_id]
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    mocked_cur_date_getter_setter = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    updated_record = {**db_seed["rules"][rule_id], "deleted_at": mocked_cur_date_getter_setter}
    db_seed["rules"][rule_id] = updated_record
    return "Record Deleted", TODO_METADATA
  return None, TODO_METADATA

