#!/usr/bin/env python3
"""
Test script for RBAC simulator.
This demonstrates a simple document management system.
"""

from rbac_simulator import RBACSystem, Permission

def main():
    # Initialize RBAC system
    rbac = RBACSystem()
    
    print("=== Setting up RBAC System ===\n")
    
    # Create roles: 'admin', 'editor', 'viewer'
    admin_role = rbac.create_role('admin')
    editor_role = rbac.create_role('editor')
    viewer_role = rbac.create_role('viewer')
    
    # Configure admin permissions
    admin_role.add_permission(Permission('read', 'document'))
    admin_role.add_permission(Permission('write', 'document'))
    admin_role.add_permission(Permission('delete', 'document'))
    
    # Configure editor permissions
    editor_role.add_permission(Permission('read', 'document'))
    editor_role.add_permission(Permission('write', 'document'))
    
    # Configure viewer permissions
    viewer_role.add_permission(Permission('read', 'document'))
    
    # Create users: 'alice', 'bob', 'charlie'
    alice = rbac.create_user('alice')
    bob = rbac.create_user('bob')
    charlie = rbac.create_user('charlie')
    
    # Assign roles to users
    alice.assign_role(admin_role)
    bob.assign_role(editor_role)
    charlie.assign_role(viewer_role)
    
    # Display system state
    rbac.display_system_state()
    
    # Test access control
    print("\n=== Testing Access Control ===\n")
    
    test_cases = [
        ('alice', 'delete', 'document', True),
        ('bob', 'write', 'document', True),
        ('bob', 'delete', 'document', False),
        ('charlie', 'read', 'document', True),
        ('charlie', 'write', 'document', False),
    ]
    
    for username, action, resource, expected in test_cases:
        result = rbac.check_access(username, action, resource)
        status = "GRANTED" if result else "DENIED"
        check = "✓" if result == expected else "✗"
        print(f"{check} {username} -> {action}:{resource} = {status}")

if __name__ == "__main__":
    main()
