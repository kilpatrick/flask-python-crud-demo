import graphene

from server.graphql_queries import Query
from server.graphql_mutations import Mutation


# Create the GraphQL schema combining queries and mutations
schema = graphene.Schema(query=Query, mutation=Mutation)
