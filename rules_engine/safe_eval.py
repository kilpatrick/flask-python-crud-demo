import ast


class SafeRuleEval(ast.NodeVisitor):
    """
        Safely replicates functionality of:
        `eval(rule, {"__builtins__": None}, safe_globals)`
        where rule is something like:
        "( ( CONDITION_uuid-001 or CONDITION_uuid-002 ) and CONDITION_uuid-03 ) or CONDITION_uuid-04"
        and each UUID is 
    """

    def __init__(self, rule_str: str, rule_state_context: dict[str, bool]):
        self.rule_str = rule_str
        self.rule_state_context = rule_state_context

    def get_rule_ids(rule: str) -> dict[str, None]:
        rule_splits = rule.split(" ")
        rule_ids = {}
        for element in rule_splits:
            if element[:5] == "CONDITION_":
                rule_id = element[5:]
                rule_ids[rule_id] = None
        return rule_ids

    def parse_rule_str_to_bool_exp(self, node):
        self.rule_str


# ---
# Example Consumption/Use

def gather_rule_state_context() -> dict[str, bool]:
    """
        WIP / TODO
    """
    mocked_rule_state_context = {
        "uuid-001": None,
        "uuid-002": None,
        "uuid-003": None,
        "uuid-004": None,
    }

    rule_state_context = mocked_rule_state_context
    return rule_state_context

def safe_rule_eval(rule: str, rule_state_context: dict[str, bool]) -> bool:
    safe_eval = SafeRuleEval(rule_state_context)
    is_criteria_met: bool = safe_eval.check_rule()
    return is_criteria_met


EXAMPLE_RULE = "( ( RULE_uuid-001 or RULE_uuid-002 ) and RULE_uuid-03 ) or RULE_uuid-04"
