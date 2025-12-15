import unittest

from evaluator import evaluate_rule_dangerously


test_cases = [
    {
        "rules.formula": "( (c_01 or c_02) and c_03) or c_04",
        "states": [
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
        ],
    },
    {
        "rules.formula": "( c_01 and c_02 and c_03 ) or c_04",
        "states": [
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
        ],
    },
    {
        "rules.formula": "c_01 and c_02 and c_03 and c_04",
        "states": [
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
        ],
    },
    {
        "rules.formula": "c_01 or c_02 or c_03 or c_04",
        "states": [
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
        ],
    },
    {
        "rules.formula": "( (c_01 or c_02) and c_03) and c_04",
        "states": [
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": True  }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": False, "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": True,  "c_04": False }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": True  }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": False, "c_03": False, "c_04": False }, "expected_eval": False },
        ],
    },
    {
        "rules.formula": "c_01 or c_02",
        "states": [
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": None, "c_04": None }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": None, "c_04": None }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": None, "c_04": None }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": None, "c_04": None }, "expected_eval": True  },
        ],
    },
    {
        "rules.formula": "c_01 and c_02",
        "states": [
            { "state_values": { "c_01": True,  "c_02": True,  "c_03": None, "c_04": None }, "expected_eval": True  },
            { "state_values": { "c_01": False, "c_02": False, "c_03": None, "c_04": None }, "expected_eval": False },
            { "state_values": { "c_01": True,  "c_02": False, "c_03": None, "c_04": None }, "expected_eval": False },
            { "state_values": { "c_01": False, "c_02": True,  "c_03": None, "c_04": None }, "expected_eval": False },
        ],
    },
] 

class TestEvaluateRuleDangerously(unittest.TestCase):
    """
        REPL Run with:
        >>> runner = FormulaEvaluations()
        >>> runner.run_tests()
    """
    def test_possible_states(self):
        for test_case in test_cases:
            for state in test_case["states"]:
                rule_evaluation = evaluate_rule_dangerously(rule=test_case["rules.formula"], conditions_state=state["state_values"])
                self.assertEqual(rule_evaluation, state["expected_eval"])
