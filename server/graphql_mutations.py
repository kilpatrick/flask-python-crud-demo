import graphene

from server.graphql_types import Rule, Condition, Action
from services import rules
from services import graphql_conditions
from services import graphql_actions


# Rule Mutations
class CreateRule(graphene.Mutation):
    """Mutation to create a new rule"""
    class Arguments:
        name = graphene.String(required=True)
        formula = graphene.String()
        action = graphene.String()
    
    rule = graphene.Field(Rule)
    
    def mutate(self, info, name, formula=None, action=None):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        request_body = {
            "name": name,
            "formula": formula,
            "action": action
        }
        rsp_data, _ = rules.create_rule(school_id, request_body)
        if not rsp_data:
            raise Exception("Failed to create rule")
        return CreateRule(rule=rsp_data)


class UpdateRule(graphene.Mutation):
    """Mutation to update an existing rule"""
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        formula = graphene.String()
        action = graphene.String()
    
    rule = graphene.Field(Rule)
    
    def mutate(self, info, id, name=None, formula=None, action=None):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        update_body = {}
        if name is not None:
            update_body["name"] = name
        if formula is not None:
            update_body["formula"] = formula
        if action is not None:
            update_body["action"] = action
        
        rsp_data, _ = rules.update_rule_by_id(school_id, id, update_body)
        if not rsp_data:
            raise Exception("Failed to update rule or rule not found")
        return UpdateRule(rule=rsp_data)


class DeleteRule(graphene.Mutation):
    """Mutation to delete a rule (soft delete)"""
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()
    
    def mutate(self, info, id):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        rsp_data, _ = rules.delete_rule_by_id(school_id, id)
        if not rsp_data:
            raise Exception("Failed to delete rule or rule not found")
        return DeleteRule(success=True, message=rsp_data)


# Condition Mutations
class CreateCondition(graphene.Mutation):
    """Mutation to create a new condition"""
    class Arguments:
        name = graphene.String(required=True)
    
    condition = graphene.Field(Condition)
    
    def mutate(self, info, name):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        request_body = {"name": name}
        rsp_data, _ = graphql_conditions.create_condition(school_id, request_body)
        if not rsp_data:
            raise Exception("Failed to create condition")
        return CreateCondition(condition=rsp_data)


class UpdateCondition(graphene.Mutation):
    """Mutation to update an existing condition"""
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
    
    condition = graphene.Field(Condition)
    
    def mutate(self, info, id, name=None):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        update_body = {}
        if name is not None:
            update_body["name"] = name
        
        rsp_data, _ = graphql_conditions.update_condition_by_id(school_id, id, update_body)
        if not rsp_data:
            raise Exception("Failed to update condition or condition not found")
        return UpdateCondition(condition=rsp_data)


class DeleteCondition(graphene.Mutation):
    """Mutation to delete a condition (soft delete)"""
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()
    
    def mutate(self, info, id):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        rsp_data, _ = graphql_conditions.delete_condition_by_id(school_id, id)
        if not rsp_data:
            raise Exception("Failed to delete condition or condition not found")
        return DeleteCondition(success=True, message=rsp_data)


# Action Mutations
class CreateAction(graphene.Mutation):
    """Mutation to create a new action"""
    class Arguments:
        name = graphene.String(required=True)
        action_type = graphene.String()
        action_msg = graphene.String()
        change = graphene.String()
        formula = graphene.String()
    
    action = graphene.Field(Action)
    
    def mutate(self, info, name, action_type=None, action_msg=None, change=None, formula=None):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        request_body = {
            "name": name,
            "action_type": action_type,
            "action_msg": action_msg,
            "change": change,
            "formula": formula
        }
        rsp_data, _ = graphql_actions.create_action(school_id, request_body)
        if not rsp_data:
            raise Exception("Failed to create action")
        return CreateAction(action=rsp_data)


class UpdateAction(graphene.Mutation):
    """Mutation to update an existing action"""
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        action_type = graphene.String()
        action_msg = graphene.String()
        change = graphene.String()
        formula = graphene.String()
    
    action = graphene.Field(Action)
    
    def mutate(self, info, id, name=None, action_type=None, action_msg=None, change=None, formula=None):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        update_body = {}
        if name is not None:
            update_body["name"] = name
        if action_type is not None:
            update_body["action_type"] = action_type
        if action_msg is not None:
            update_body["action_msg"] = action_msg
        if change is not None:
            update_body["change"] = change
        if formula is not None:
            update_body["formula"] = formula
        
        rsp_data, _ = graphql_actions.update_action_by_id(school_id, id, update_body)
        if not rsp_data:
            raise Exception("Failed to update action or action not found")
        return UpdateAction(action=rsp_data)


class DeleteAction(graphene.Mutation):
    """Mutation to delete an action (soft delete)"""
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()
    
    def mutate(self, info, id):
        school_id = info.context.get('school_id')
        if not school_id:
            raise Exception("Unauthorized: school_id required")
        
        rsp_data, _ = graphql_actions.delete_action_by_id(school_id, id)
        if not rsp_data:
            raise Exception("Failed to delete action or action not found")
        return DeleteAction(success=True, message=rsp_data)


class Mutation(graphene.ObjectType):
    """GraphQL mutations for creating, updating, and deleting data"""
    
    # Rule mutations
    create_rule = CreateRule.Field()
    update_rule = UpdateRule.Field()
    delete_rule = DeleteRule.Field()
    
    # Condition mutations
    create_condition = CreateCondition.Field()
    update_condition = UpdateCondition.Field()
    delete_condition = DeleteCondition.Field()
    
    # Action mutations
    create_action = CreateAction.Field()
    update_action = UpdateAction.Field()
    delete_action = DeleteAction.Field()
