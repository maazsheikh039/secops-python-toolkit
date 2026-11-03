# Role-Based Access Control (RBAC) Simulator

A clean, object-oriented Python simulation of a Role-Based Access Control (RBAC) authorization engine designed to model users, roles, permissions, and resources while enforcing least-privilege access decisions.

## Objectives
- Implement core IAM (Identity and Access Management) entities: `User`, `Role`, `Permission`, and `Resource`.
- Enable set-based permission hashing and equality checks for high-performance role association.
- Evaluate authorization requests dynamically across multi-role user memberships.
- Validate security decision matrices through automated test scenarios.

## Tools Used
- **Python 3** (`classes`, `sets`, `dictionaries`)
- **Linux CLI / SSH**

## Key Skills Demonstrated
- **Authorization Modeling:** Designing scalable access control structures mimicking enterprise IAM systems (AWS IAM, Linux groups).
- **Object-Oriented Programming (OOP):** Encapsulating state and behavior within cohesive security classes.
- **Defensive Access Design:** Preventing unauthorized privilege escalation by evaluating explicit permission mappings.

## Troubleshooting Log
- *Permission Hash Equality:* Implemented custom `__eq__` and `__hash__` methods in the `Permission` class to guarantee proper set lookups.
- *Role Scope Verification:* Ensured users can hold multiple roles simultaneously and accumulate combined permission privileges.
