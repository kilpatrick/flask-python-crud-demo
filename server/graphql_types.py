import graphene

from services import rules
from services import graphql_conditions
from services import graphql_actions


class Rule(graphene.ObjectType):
    """GraphQL type for Rule"""
    id = graphene.ID()
    name = graphene.String()
    formula = graphene.String()
    action = graphene.String()
    school_id = graphene.ID(name='schoolId')
    created_at = graphene.String(name='createdAt')
    updated_at = graphene.String(name='updatedAt')
    deleted_at = graphene.String(name='deletedAt')
    
    def resolve_schoolId(self, info):
        return self.get('school_id') if isinstance(self, dict) else getattr(self, 'school_id', None)
    
    def resolve_createdAt(self, info):
        return self.get('created_at') if isinstance(self, dict) else getattr(self, 'created_at', None)
    
    def resolve_updatedAt(self, info):
        return self.get('updated_at') if isinstance(self, dict) else getattr(self, 'updated_at', None)
    
    def resolve_deletedAt(self, info):
        return self.get('deleted_at') if isinstance(self, dict) else getattr(self, 'deleted_at', None)


class Condition(graphene.ObjectType):
    """GraphQL type for Condition"""
    id = graphene.ID()
    name = graphene.String()
    school_id = graphene.ID(name='schoolId')
    created_at = graphene.String(name='createdAt')
    updated_at = graphene.String(name='updatedAt')
    deleted_at = graphene.String(name='deletedAt')
    
    def resolve_schoolId(self, info):
        return self.get('school_id') if isinstance(self, dict) else getattr(self, 'school_id', None)
    
    def resolve_createdAt(self, info):
        return self.get('created_at') if isinstance(self, dict) else getattr(self, 'created_at', None)
    
    def resolve_updatedAt(self, info):
        return self.get('updated_at') if isinstance(self, dict) else getattr(self, 'updated_at', None)
    
    def resolve_deletedAt(self, info):
        return self.get('deleted_at') if isinstance(self, dict) else getattr(self, 'deleted_at', None)


class Action(graphene.ObjectType):
    """GraphQL type for Action"""
    id = graphene.ID()
    name = graphene.String()
    action_type = graphene.String(name='actionType')
    action_msg = graphene.String(name='actionMsg')
    change = graphene.String()
    formula = graphene.String()
    school_id = graphene.ID(name='schoolId')
    created_at = graphene.String(name='createdAt')
    updated_at = graphene.String(name='updatedAt')
    deleted_at = graphene.String(name='deletedAt')
    
    def resolve_actionType(self, info):
        return self.get('action_type') if isinstance(self, dict) else getattr(self, 'action_type', None)
    
    def resolve_actionMsg(self, info):
        return self.get('action_msg') if isinstance(self, dict) else getattr(self, 'action_msg', None)
    
    def resolve_schoolId(self, info):
        return self.get('school_id') if isinstance(self, dict) else getattr(self, 'school_id', None)
    
    def resolve_createdAt(self, info):
        return self.get('created_at') if isinstance(self, dict) else getattr(self, 'created_at', None)
    
    def resolve_updatedAt(self, info):
        return self.get('updated_at') if isinstance(self, dict) else getattr(self, 'updated_at', None)
    
    def resolve_deletedAt(self, info):
        return self.get('deleted_at') if isinstance(self, dict) else getattr(self, 'deleted_at', None)
