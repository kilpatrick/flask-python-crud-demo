import re

from conditions import business, school, taxes


def get_rule_conditions(rule_formula: str, family_details: dict[str, any]) -> dict[str, bool]:
    """
        Should take a collection of `conditions.condtion_types`, such as:
          "family_status_new and business_owner_true and file_taxes_2025_true"
        And generate a lookup truth table such as:
          {
            "family_status_new": boolean,
            "business_owner_true": boolean,
            "file_taxes_2025_true": boolean,
          }
    """

    condtion_checks = {
        "business_owner_false": lambda: not business.is_business_owner(family_details),
        "business_owner_true": lambda: business.is_business_owner(family_details),
        "family_status_new": lambda: school.check_family_status("new", family_details),
        "family_status_returning": lambda: school.check_family_status("returning", family_details),
        "file_taxes_2025_false": lambda: not taxes.check_tax_filing_status(2025, family_details),
        "file_taxes_2025_true": lambda: taxes.check_tax_filing_status(2025, family_details),
    }

    # I had Claude Sonnet 4.5 write this regex. I verified in regex101.com
    # against all test cases currently in the repo, but this is potentially
    # brittle and should have its own tests if used in a prod app.
    pattern = r'\b(?!and\b|or\b|not\b)[a-zA-Z_][a-zA-Z0-9_]*\b'
    conditions = set(re.findall(pattern, rule_formula))

    truth_table = {}
    for condition in conditions:
        if condition not in conditions:
            # This should be unreachable. If you're debugging this. Fix
            # whatever is allowing this to be reachable (such as an 
            # whatever process allowed an enum to hit the db that is not
            # represented here.)
            raise ValueError(f"Unknown Condition: '{condition}' in rule.")
        truth_table[condition] = condtion_checks[condition]()

    return truth_table
