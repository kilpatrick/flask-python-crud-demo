from flask import request, jsonify

from server.graphql_schema import schema


def graphql_view(decoded_token):
    """GraphQL endpoint handler with authentication"""
    # Extract school_id from token
    school_id = decoded_token.get("organization", {}).get("id")
    
    # Get the GraphQL query from request
    data = request.get_json()
    query = data.get('query')
    variables = data.get('variables')
    operation_name = data.get('operationName')
    
    if not query:
        return jsonify({
            "errors": [{"message": "No query provided"}]
        }), 400
    
    # Execute GraphQL query with school_id in context
    # Graphene uses its own execution method, not graphql-core's graphql_sync
    context = {
        'school_id': school_id,
        'decoded_token': decoded_token
    }
    
    result = schema.execute(
        query,
        variables=variables,
        operation_name=operation_name,
        context=context
    )
    
    # Format response
    response_data = {'data': result.data}
    
    if result.errors:
        # Format errors for GraphQL response
        response_data['errors'] = [
            {
                "message": str(error),
                "locations": getattr(error, 'locations', None),
                "path": getattr(error, 'path', None)
            }
            for error in result.errors
        ]
    
    status_code = 200
    if result.errors:
        # Check if any errors are authentication/authorization related
        has_auth_error = any(
            'Unauthorized' in str(error) or 'school_id' in str(error).lower()
            for error in result.errors
        )
        if has_auth_error:
            status_code = 401
    
    return jsonify(response_data), status_code
