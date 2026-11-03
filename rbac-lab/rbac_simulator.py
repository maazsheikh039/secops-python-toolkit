#!/usr/bin/env python3
"""
Role-Based Access Control (RBAC) Simulator
Models users, roles, permissions, and evaluates access control decisions.
"""

class Permission:
    """
    Represents a single permission in the RBAC system.
    A permission defines an action that can be performed on a resource.
    """
    
    def __init__(self, action, resource):
        """
        Initialize a permission.
        
        Args:
            action (str): The action (e.g., 'read', 'write', 'delete')
            resource (str): The resource (e.g., 'document', 'database')
        """
        self.action = action
        self.resource = resource
    
    def __str__(self):
        return f"{self.action}:{self.resource}"
    
    def __eq__(self, other):
        """Check if two permissions are equal."""
        if not isinstance(other, Permission):
            return False
        return self.action == other.action and self.resource == other.resource
    
    def __hash__(self):
        """Make Permission hashable for use in sets."""
        return hash((self.action, self.resource))


class Role:
    """
    Represents a role in the RBAC system.
    A role is a collection of permissions.
    """
    
    def __init__(self, name):
        """
        Initialize a role.
        
        Args:
            name (str): The role name (e.g., 'admin', 'editor')
        """
        self.name = name
        self.permissions = set()
    
    def add_permission(self, permission):
        """
        Add a permission to this role.
        
        Args:
            permission (Permission): The permission to add
        """
        self.permissions.add(permission)
    
    def has_permission(self, permission):
        """
        Check if this role has a specific permission.
        
        Args:
            permission (Permission): The permission to check
            
        Returns:
            bool: True if role has permission, False otherwise
        """
        return permission in self.permissions
    
    def __str__(self):
        return f"Role: {self.name} ({len(self.permissions)} permissions)"


class User:
    """
    Represents a user in the RBAC system.
    A user can have multiple roles.
    """
    
    def __init__(self, username):
        """
        Initialize a user.
        
        Args:
            username (str): The username
        """
        self.username = username
        self.roles = set()
    
    def assign_role(self, role):
        """
        Assign a role to this user.
        
        Args:
            role (Role): The role to assign
        """
        self.roles.add(role)
    
    def has_permission(self, permission):
        """
        Check if user has a permission through any of their roles.
        
        Args:
            permission (Permission): The permission to check
            
        Returns:
            bool: True if user has permission, False otherwise
        """
        for role in self.roles:
            if role.has_permission(permission):
                return True
        return False
    
    def __str__(self):
        return f"User: {self.username} (Roles: {[r.name for r in self.roles]})"


class RBACSystem:
    """
    Main RBAC system that manages users, roles, and access decisions.
    """
    
    def __init__(self):
        """Initialize the RBAC system."""
        self.users = {}
        self.roles = {}
    
    def create_role(self, role_name):
        """
        Create a new role.
        
        Args:
            role_name (str): Name of the role
            
        Returns:
            Role: The created role
        """
        role = Role(role_name)
        self.roles[role_name] = role
        return role
    
    def create_user(self, username):
        """
        Create a new user.
        
        Args:
            username (str): Username
            
        Returns:
            User: The created user
        """
        user = User(username)
        self.users[username] = user
        return user
    
    def check_access(self, username, action, resource):
        """
        Check if a user has permission to perform an action on a resource.
        
        Args:
            username (str): The username
            action (str): The action to perform
            resource (str): The resource to access
            
        Returns:
            bool: True if access granted, False otherwise
        """
        user = self.users.get(username)
        if not user:
            return False
        
        permission = Permission(action, resource)
        return user.has_permission(permission)
    
    def display_system_state(self):
        """Display current state of the RBAC system."""
        print("\n=== RBAC System State ===")
        print(f"\nRoles ({len(self.roles)}):")
        for role in self.roles.values():
            print(f"  - {role}")
            for perm in role.permissions:
                print(f"    * {perm}")
        
        print(f"\nUsers ({len(self.users)}):")
        for user in self.users.values():
            print(f"  - {user}")
