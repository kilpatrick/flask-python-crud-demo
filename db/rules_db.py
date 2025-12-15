from uuid import UUID

from base_model import DBSharedCols


class Rules(DBSharedCols):
    name: str
    forumla: str  # ex: ( (CONDITION_01 OR CONDITION_02) AND CONDITION_03) ) OR CONDITION_04
    action: UUID

class Actions(DBSharedCols):
    rule_id: UUID  # fkey(rules.id)
    name: str      # ex: "Is Business Owner"
    action_type: str  #  enmum("request_doc", "tuition_increase_email", "tuition_increase_portal_alert")
    action_msg:str    #  ex: "Increase tuition by 10%" OR "Request TAX Doc"
    change: str       #  ex: "Increase 10%" or "2025 W2 Guardian B" 

class Conditions(DBSharedCols):
    name: str  # ex : "Is Business Owner"
