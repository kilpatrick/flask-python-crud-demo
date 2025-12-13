# Auth

This is a placeholder. It's assumed in a productionized app, a valid hardened authentication layer would be here. This serves to show the basic structure of what is expected.

## Keys

**WARNING:** The NOT FOR PRODUCTION USE keys used in the JWTs are included in this repo. No keys used in any publicly exposed environment (including dev and staging) should have their keys in version control. This is just a demo. These can be used for local generation and validation of JWTs.

### Keys

**private.key**: Private key generated with `openssl genrsa -out ./private.key 4096`. In Prod, you may want to consider alternative signing options such as a 2048 numbit or switching the algorithm to ES256 to provide faster signing/validation.
**public.key**: Public key generated with `openssl rsa -in private.key -pubout -out public.key`


### Not Implemented

**Token Generation**
It is assumed that another service is generating (and refreshing) signed JWTs on login and that all requests to this service will include the JWT. Example shape:

```json
{
  "email": "c.ronaldo@example.com",
  "exp": 1767254460,
  "iat": 1765627200,
  "name": "Cristiano Ronaldo",
  "organization": {
    "id": "dfbbf5e3-76cf-4a85-ba29-c47686d4d886"
  },
  "permissions": [
    "orgs:read-self",
    "users:read-full-org",
    "users:read-self",
    "users:update-self",
    "rules:create",
    "rules:read",
    "rules:update",
    "rules:delete"
  ],
  "role": {
    "id": "5d0909b9-9339-4177-b3e3-8e45e4a620c7"
  },
  "id": "e47c7f3b-31f8-479d-91f5-a898f67a5337"
}
```

**Robust Token Validation**
The rudimentary, partially implemented `@auth_check` decorator in this repo serves as a placeholder. It is assumed a production ready, shared internal package or middleware exits and would be imported to handle token and permission validation across all services.
