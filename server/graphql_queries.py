import graphene

from server.graphql_types import Rule, Condition, Action, RuleDryRun
from services import rules
from services import graphql_conditions
from services import graphql_actions


class Query(graphene.ObjectType):
    """GraphQL queries for reading data"""
    
    # Rules queries
    rules = graphene.List(Rule, description="Get all rules for the authenticated school")
    rule = graphene.Field(Rule, id=graphene.ID(required=True), description="Get a rule by ID")
    rule_dry_run = graphene.Field(
        RuleDryRun,
        rule_id=graphene.ID(required=True),
        application_id=graphene.ID(required=True),
        description="Preview rule evaluation with application data without executing actions"
    )
    
    # Conditions queries
    conditions = graphene.List(Condition, description="Get all conditions for the authenticated school")
    condition = graphene.Field(Condition, id=graphene.ID(required=True), description="Get a condition by ID")
    
    # Actions queries
    actions = graphene.List(Action, description="Get all actions for the authenticated school")
    action = graphene.Field(Action, id=graphene.ID(required=True), description="Get an action by ID")
    
    def resolve_rules(self, info):
        """Resolve all rules query"""
        school_id = info.context.get('school_id')
        if not school_id:
            return []
        rsp_data, _ = rules.read_all_rules(school_id)
        return rsp_data if rsp_data else []
    
    def resolve_rule(self, info, id):
        """Resolve single rule query"""
        school_id = info.context.get('school_id')
        if not school_id:
            return None
        rsp_data, _ = rules.read_rule_by_id(school_id, id)
        return rsp_data

    def resolve_rule_dry_run(self, info, rule_id, application_id):
        """Resolve rule dry-run query"""
        school_id = info.context.get('school_id')
        if not school_id:
            return None
        rsp_data, _ = rules.trigger_rule_dry_run(school_id, rule_id, application_id)
        return rsp_data
    
    def resolve_conditions(self, info):
        """Resolve all conditions query"""
        school_id = info.context.get('school_id')
        if not school_id:
            return []
        rsp_data, _ = graphql_conditions.read_all_conditions(school_id)
        return rsp_data if rsp_data else []
    
    def resolve_condition(self, info, id):
        """Resolve single condition query"""
        school_id = info.context.get('school_id')
        if not school_id:
            return None
        rsp_data, _ = graphql_conditions.read_condition_by_id(school_id, id)
        return rsp_data
    
    def resolve_actions(self, info):
        """Resolve all actions query"""
        school_id = info.context.get('school_id')
        if not school_id:
            return []
        rsp_data, _ = graphql_actions.read_all_actions(school_id)
        return rsp_data if rsp_data else []
    
    def resolve_action(self, info, id):
        """Resolve single action query"""
        school_id = info.context.get('school_id')
        if not school_id:
            return None
        rsp_data, _ = graphql_actions.read_action_by_id(school_id, id)
        return rsp_data
