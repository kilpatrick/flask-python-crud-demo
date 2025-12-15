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


def create_action(school_id: str, request_body: dict) -> [dict, dict]:
  import uuid
  new_id = str(uuid.uuid4())
  now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
  new_action = {
    "id": new_id,
    "school_id": school_id,
    "created_at": now,
    "updated_at": now,
    "deleted_at": None,
    **request_body
  }
  db_seed["actions"][new_id] = new_action
  return new_action, TODO_METADATA

def read_all_actions(school_id: str) -> [dict, dict]:
  actions_filtered_by_school = []
  for action_id in db_seed["actions"]:
    record = db_seed["actions"][action_id]
    row_school_id = record.get("school_id")
    if school_id  and record.get("deleted_at") == None and row_school_id and row_school_id == school_id:
      actions_filtered_by_school.append(record)
  return actions_filtered_by_school, TODO_METADATA

def read_action_by_id(school_id: str, action_id: str) -> [dict, dict]:
  record = db_seed["actions"].get(action_id)
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    return record, TODO_METADATA
  return None, TODO_METADATA

def update_action_by_id(school_id: str, action_id: str, update_body: dict) -> [dict, dict]:
  record = db_seed["actions"].get(action_id)
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    # WARNING: Remember there's lots of handwaving going on here. This is going to allow for
    # things like the user changing the UUID of records which is a terrible, horrible thing.
    # Don't actually do that.
    updated_record = {**db_seed["actions"][action_id], **update_body}
    updated_record["updated_at"] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    db_seed["actions"][action_id] = updated_record
    return db_seed["actions"][action_id], TODO_METADATA
  return None, TODO_METADATA

def delete_action_by_id(school_id: str, action_id: str) -> [dict, dict]:
  record = db_seed["actions"].get(action_id)
  if record and record.get("deleted_at") == None and record.get("school_id") == school_id:
    mocked_cur_date_getter_setter = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    updated_record = {**db_seed["actions"][action_id], "deleted_at": mocked_cur_date_getter_setter}
    db_seed["actions"][action_id] = updated_record
    return "Record Deleted", TODO_METADATA
  return None, TODO_METADATA
