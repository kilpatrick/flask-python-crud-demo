# GraphQL API Guide

## Overview

This project now supports both REST and GraphQL APIs. The GraphQL endpoint is available at `/graphql` and requires the same authentication as REST endpoints.

## Key Differences from REST

1. **Single Endpoint**: All GraphQL requests go to `POST /graphql`
2. **Query Language**: Requests use GraphQL query syntax in the request body
3. **Client-Controlled Fields**: You request only the fields you need
4. **Operations**: 
   - **Queries** (read operations): `{ rules { id name } }`
   - **Mutations** (write operations): `mutation { createRule(...) { id } }`

## Field Name Convention

GraphQL field names use **camelCase** in queries, even though the Python code uses snake_case. Graphene automatically converts:
- `school_id` → `schoolId`
- `created_at` → `createdAt`
- `updated_at` → `updatedAt`
- `deleted_at` → `deletedAt`
- `action_type` → `actionType`
- `action_msg` → `actionMsg`

## Authentication

Same as REST - include `Authorization` header with JWT token:
```
Authorization: {{AUTH_TOKEN}}
```

## Request Format

All GraphQL requests are POST to `/graphql` with JSON body:

```json
{
  "query": "{ rules { id name } }"
}
```

For mutations with variables:
```json
{
  "query": "mutation($name: String!) { createRule(name: $name) { id name } }",
  "variables": {
    "name": "New Rule"
  }
}
```

## Available Operations

### Rules

**Queries:**
- `rules` - Get all rules
- `rule(id: ID!)` - Get single rule

**Mutations:**
- `createRule(name: String!, formula: String, action: String)` - Create rule
- `updateRule(id: ID!, name: String, formula: String, action: String)` - Update rule
- `deleteRule(id: ID!)` - Soft delete rule

### Conditions

**Queries:**
- `conditions` - Get all conditions
- `condition(id: ID!)` - Get single condition

**Mutations:**
- `createCondition(name: String!)` - Create condition
- `updateCondition(id: ID!, name: String)` - Update condition
- `deleteCondition(id: ID!)` - Soft delete condition

### Actions

**Queries:**
- `actions` - Get all actions
- `action(id: ID!)` - Get single action

**Mutations:**
- `createAction(name: String!, actionType: String, actionMsg: String, change: String, formula: String)` - Create action
- `updateAction(id: ID!, name: String, actionType: String, actionMsg: String, change: String, formula: String)` - Update action
- `deleteAction(id: ID!)` - Soft delete action

## Example Queries

### Get all rules (minimal fields)
```graphql
{
  rules {
    id
    name
  }
}
```

### Get all rules (all fields)
```graphql
{
  rules {
    id
    name
    formula
    action
    schoolId
    createdAt
    updatedAt
    deletedAt
  }
}
```

### Get single rule
```graphql
{
  rule(id: "30c12b0e-18fb-4b7d-b3bf-954336607e7b") {
    id
    name
    formula
  }
}
```

### Create a rule
```graphql
mutation {
  createRule(
    name: "New Rule"
    formula: "(CONDITION_01 OR CONDITION_02)"
    action: "action-id-here"
  ) {
    id
    name
    formula
    createdAt
  }
}
```

### Update a rule
```graphql
mutation {
  updateRule(
    id: "30c12b0e-18fb-4b7d-b3bf-954336607e7b"
    name: "Updated Name"
  ) {
    id
    name
    updatedAt
  }
}
```

### Delete a rule
```graphql
mutation {
  deleteRule(id: "30c12b0e-18fb-4b7d-b3bf-954336607e7b") {
    success
    message
  }
}
```

## Testing with Postman

1. Import the collection: `postman/collections/New Collection 1.postman_collection.json`
2. Set the environment: `postman/environments/New_Environment.postman_environment.json`
3. All requests use the same `{{BASE_URL}}/graphql` endpoint
4. Modify the `query` field in the request body to request different fields

## Next Steps

1. **Test the GraphQL endpoint**: Use the Postman collection to test all operations
2. **Compare with REST**: Notice how GraphQL lets you request only needed fields
3. **Explore GraphQL features**: 
   - Try requesting nested data (when relationships are added)
   - Use variables for dynamic queries
   - Combine multiple queries in one request

## Troubleshooting

- **401 Unauthorized**: Check your `AUTH_TOKEN` is valid
- **Field not found**: Remember to use camelCase (e.g., `schoolId` not `school_id`)
- **Invalid query**: Check GraphQL syntax - queries use `{ }`, mutations use `mutation { }`
- **No data returned**: Check that records exist and aren't soft-deleted (`deletedAt` is null)
