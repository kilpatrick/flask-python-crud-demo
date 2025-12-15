# import uuid
# uuid.uuid4()

rules = {
    # About Rules:
    # These are example expected cases that could exist and be represented by different actions.
    #   -------------------------------------------------------------------------------------------
    #   condition_type          and business_owner_false and file_taxes_2025_false
    #   condition_type          and business_owner_true  and file_taxes_2025_false
    #   family_status_returning and business_owner_false and file_taxes_2025_false
    #   family_status_returning and business_owner_true  and file_taxes_2025_false
    #   condition_type          and business_owner_false and file_taxes_2025_true
    #   condition_type          and business_owner_true  and file_taxes_2025_true
    #   family_status_returning and business_owner_false and file_taxes_2025_true
    #   family_status_returning and business_owner_true  and file_taxes_2025_true
    #   -------------------------------------------------------------------------------------------
    # Each condition (i.e. "family_status_returning") corresponds to a conditions.condition_type enum.
    # Conditions require enums so the code know how to handle converting a condition into a boolean.
    # The combined True or False outcome determines if the linked actions.id happens or not.

    "30c12b0e-18fb-4b7d-b3bf-954336607e7b": {
        "action_id": "f221f039-98fb-4e8a-8ec8-8fc0f0bf411b",
        "name": "New Family + Business Owner + Filed taxes in 2025",
        "formula": "family_status_new and business_owner_true and file_taxes_2025_true",
        # BASE_COLS
        "id": "30c12b0e-18fb-4b7d-b3bf-954336607e7b",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "d15feafe-071b-4cc8-b776-22c027db4d84": {
        "action_id": "FK_TO_ACTIONS",
        "name": "New Family + Business Owner + No 2025 Taxes",
        "formula": "family_status_new and business_owner_true and file_taxes_2025_false",
        # BASE_COLS
        "id": "d15feafe-071b-4cc8-b776-22c027db4d84",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "f3492e06-e29e-4569-851b-7002cc230c30": {
        "action_id": "FK_TO_ACTIONS",
        "name": "Returning Family + Doesn't Own a Business + No 2025 Taxes Files",
        "formula": "family_status_returning and business_owner_false and file_taxes_2025_false",
        # BASE_COLS
        "id": "f3492e06-e29e-4569-851b-7002cc230c30",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    # Blank Rule to Use as Starter Rule:
    # "FILL_THIS_OUT": {
    #     "action_id": "FK_TO_ACTIONS",
    #     "name": "FILL_THIS_OUT",
    #     "formula": "FILL_THIS_OUT",
    #     # BASE_COLS
    #     "id": "FILL_THIS_OUT",
    #     "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
    #     "created_at": None,
    #     "updated_at": None,
    #     "deleted_at": None,
    # },
    "edc3610a-8d76-40a4-9828-12783ae2034d": {
        "action_id": "FK_TO_ACTIONS",
        "name": "Deleted Rule",
        "formula": "Boolean Combination of conditions.id fk values",
        # BASE_COLS
        "id": "edc3610a-8d76-40a4-9828-12783ae2034d",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": "2024-12-14T12:23:47Z", 
        "updated_at": "2025-06-14T09:42:09Z",
        "deleted_at": "2025-12-13T11:10:33Z"
    },
}

conditions = {
    "42e1d754-47e8-4f15-a7b3-8e5b2367aae2": {
        "name": "Owns a Business",
        "condition_type": "business_owner_false",
        # BASE_COLS
        "id": "42e1d754-47e8-4f15-a7b3-8e5b2367aae2",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "cf7d1218-5434-42e1-b29f-b15f830e4720": {
        "name": "Does Not Own a Business",
        "condition_type": "business_owner_true",
        # BASE_COLS
        "id": "cf7d1218-5434-42e1-b29f-b15f830e4720",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "64a1c01f-ddc7-4810-b1f8-1d48487a2f9f": {
        "name": "Family is New to School",
        "condition_type": "family_status_new",
        # BASE_COLS
        "id": "64a1c01f-ddc7-4810-b1f8-1d48487a2f9f",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "ab2fd8ba-6a10-4b4e-a378-13a3a2812ce4": {
        "name": "Family Returning from Previous Year",
        "condition_type": "family_status_returning",
        # BASE_COLS
        "id": "ab2fd8ba-6a10-4b4e-a378-13a3a2812ce4",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "b503df9e-1982-49b9-98bb-5b887d668f0d": {
        "name": "Did Not file 2025 Taxes",
        "condition_type": "file_taxes_2025_false",
        # BASE_COLS
        "id": "b503df9e-1982-49b9-98bb-5b887d668f0d",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "f20d62f5-1e01-4e62-9f5e-e3c24a2aad51": {
        "name": "Filed Their 2025 Taxes",
        "condition_type": "file_taxes_2025_true",
        # BASE_COLS
        "id": "f20d62f5-1e01-4e62-9f5e-e3c24a2aad51",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}

actions = {
    "f221f039-98fb-4e8a-8ec8-8fc0f0bf411b": {
        "action_type": "request_doc",
        "document_id": "ff88b66c-30c0-49bf-91d9-ff81f6442dc0",
        "name": "Request 2026 Business Taxes",
        # BASE_COLS
        "id": "f221f039-98fb-4e8a-8ec8-8fc0f0bf411b",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "8beab254-5350-4257-b2e9-b37b908aef3b": {
        "action_type": "request_doc",
        "document_id": "38cea5b2-e756-4d52-81e1-d99c55e535d0",
        "name": "Untitled Action",
        # BASE_COLS
        "id": "8beab254-5350-4257-b2e9-b37b908aef3b",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "b0be1f7e-6565-4b15-ab60-4d57c540d3e4": {
        "action_type": "request_doc",
        "document_id": "fa8cba48-51cb-42dc-bf87-88def390961c",
        "name": "Untitled Action 2",
        # BASE_COLS
        "id": "b0be1f7e-6565-4b15-ab60-4d57c540d3e4",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}

document_types = {
    "38c2a6de-c25c-4fec-9582-7089d6e1fe69": {
        # BASE_COLS
        "id": "38c2a6de-c25c-4fec-9582-7089d6e1fe69",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "c1e96f2e-676e-4650-8e7c-9d98c1581c88": {
        # BASE_COLS
        "id": "c1e96f2e-676e-4650-8e7c-9d98c1581c88",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "77d5ab66-839c-4b48-be8c-348cfe2609a0": {
        # BASE_COLS
        "id": "77d5ab66-839c-4b48-be8c-348cfe2609a0",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}

document_uploads = {
    "a2fd5806-4e2d-498b-a43a-ea47cde9946a": {
        # BASE_COLS
        "id": "a2fd5806-4e2d-498b-a43a-ea47cde9946a",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "712d05ab-d70f-47d9-9396-0888eb05bfba": {
        # BASE_COLS
        "id": "712d05ab-d70f-47d9-9396-0888eb05bfba",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "3df682b3-0af8-4cc9-934b-f39498789ed4": {
        # BASE_COLS
        "id": "3df682b3-0af8-4cc9-934b-f39498789ed4",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}

families = {
    # Notes:
    # - `tax_filing_years`: Would instead lookup from tax_filings table if that exists
    "8b6df376-0690-4b59-9208-00a8209904db": {  # <-- Testing family for Ronaldo (JWT Test User)
        "status": "returning",
        "is_business_owner": False,
        "tax_filing_years": [2025, 2024, 2023],
        # BASE_COLS
        "id": "8b6df376-0690-4b59-9208-00a8209904db",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "b3cecb02-8857-43ea-a120-7969d9f2a7f7": {
        "status": "new",
        "is_business_owner": False,
        "tax_filing_years": [2024],
        # BASE_COLS
        "id": "b3cecb02-8857-43ea-a120-7969d9f2a7f7",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "34dd6862-b8f9-4f08-8067-cfb7a15b188f": {
        "status": "new",
        "is_business_owner": False,
        "tax_filing_years": [],
        # BASE_COLS
        "id": "34dd6862-b8f9-4f08-8067-cfb7a15b188f",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}

guardians = {
    "e47c7f3b-31f8-479d-91f5-a898f67a5337": {  # <-- Testing user used in JWT
        "email": "c.ronaldo@example.com",
        "first_name": "Cristiano",
        "last_name": "Ronaldo",
        "family_id": "8b6df376-0690-4b59-9208-00a8209904db",
        # BASE_COLS
        "id": "e47c7f3b-31f8-479d-91f5-a898f67a5337",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "58bd2c46-7aad-4b91-af13-78ba44327868": {
        # BASE_COLS
        "id": "58bd2c46-7aad-4b91-af13-78ba44327868",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "676c848b-e8ac-45aa-8a8a-fbb86ce047ab": {
        # BASE_COLS
        "id": "676c848b-e8ac-45aa-8a8a-fbb86ce047ab",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}

schools = {
    "782a3d9b-a88f-4436-a4bb-2bb00ff00f99": {
        # BASE_COLS
        "id": "782a3d9b-a88f-4436-a4bb-2bb00ff00f99",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "b7812fa3-b477-4272-b213-4e6013223c27": {
        # BASE_COLS
        "id": "b7812fa3-b477-4272-b213-4e6013223c27",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "d2ad86cb-5405-4996-9cdf-bfb48a13e570": {
        # BASE_COLS
        "id": "d2ad86cb-5405-4996-9cdf-bfb48a13e570",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}

applications = {
    "ff704790-519e-4621-a9a9-caabf3f814a8": {
        "family_id": "8b6df376-0690-4b59-9208-00a8209904db",
        # BASE_COLS
        "id": "ff704790-519e-4621-a9a9-caabf3f814a8",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "23b4c160-463a-489d-af2f-99bcaff7d9a9": {
        "family_id": "b3cecb02-8857-43ea-a120-7969d9f2a7f7",
        # BASE_COLS
        "id": "23b4c160-463a-489d-af2f-99bcaff7d9a9",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
    "644c3043-942c-40e6-99e0-f8e187f12f25": {
        "family_id": "34dd6862-b8f9-4f08-8067-cfb7a15b188f",
        # BASE_COLS
        "id": "644c3043-942c-40e6-99e0-f8e187f12f25",
        "school_id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    },
}



db_seed = {
    "rules": rules,
    "conditions": conditions,
    "actions": actions,
    "document_types": document_types,
    "document_uploads": document_uploads,
    "families": families,
    "guardians": guardians,
    "schools": schools,
    "applications": applications,
}
