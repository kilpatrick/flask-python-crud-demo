def check_family_status(status: str, family_details: dict[str, any]) -> bool:
    status_check_matches = family_details.get("status") == status
    return status_check_matches
