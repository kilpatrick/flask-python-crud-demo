def evaluate_rule_dangerously(formula: str, truth_table: dict[str, bool]):
    """
        Certainly NEVER run `eval()` on untrusted inputs, and there's probably no
        reasonably way to get to 100% certainty your inputs are trusted, so just
        don't run eval in prod at all.

        ex acceptable values:
        - two conditions no parenthesis:
            - `formula`: c_01 or c_02
            - `truth_table`: {'c_01': False, 'c_02': True}
        - four conditions with parenthesis honored:
            - `formula`: ( (c_01 or c_02) and c_03) or c_04
            - `truth_table`: {'c_01': True, 'c_02': True, 'c_03': True, 'c_04': True}
    """

    # I asked AI for some "safe" globals to make this safer, but don't use this as-is.
    safe_globals = {
            'True': True,
            'False': False,
            'and': lambda x, y: x and y,
            'or': lambda x, y: x or y,
            'not': lambda x: not x,
    }

    safe_globals.update(truth_table)
    result = eval(formula, {"__builtins__": None}, safe_globals)
    return result
