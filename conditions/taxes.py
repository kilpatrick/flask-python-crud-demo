def check_tax_filing_status(year: int, family_details: dict[str, any]) -> bool:
    filed_in_requested_year = year in family_details.get("tax_filing_years")
    return filed_in_requested_year