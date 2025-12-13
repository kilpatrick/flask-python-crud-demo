# Python Flask Web App Demo

## Local Development

### Prerequisites

It is assumed that you have:

**a virtual environment:** 
- created a python virtual environment (`python3 -m venv .venv`)
- are always working from within that environment (`source .venv/bin/activate`)

**installed requirements:** `make requirements`

**python version:** This was built in python 3.13, and has only been tested with that version. You can almost certainly get by with using an older version, but at minimum you'll need python >= 3.9.

### Running / Using the Server

- From the root directory, run `make start-server` to start the flask server.
- A Postman collection has been included (in `./postman` dir) to provide prebuilt calls you can use/test/modify as needed. 
  - If you want to test outside of Postman, you can manually find the `BASE_URL` and `AUTH_TOKEN` values required for a successful call in the `./postman/environments/` file.
  - The APIs are also partially documented in OpenAPI 3.x yaml format in the `./api/rules.yaml` file.

---
Copyright © 2025. All rights reserved.
