# Automated Release Engineering System

## Objectives
- Automate build verification, unit testing, and artifact packaging workflows.
- Implement Semantic Versioning (SemVer) automation scripts (`major`, `minor`, `patch`).
- Parse Git commit streams to extract `feat:` and `fix:` conventional commits into markdown release notes.
- Orchestrate end-to-end releases with Git tagging, metadata insertion, and archived release bundling.

## Tools Used
- **Shell Scripting (`bash`, `sed`, `grep`)**: Automation routines and string parsing.
- **Git**: Version control, tag management, and history extraction.
- **Python 3**: Execution environment and unit testing framework.

## Key Skills Demonstrated
- Continuous Delivery (CD) pipeline automation.
- Release engineering and packaging strategy.
- Automated changelog generation and SemVer adherence.

## Troubleshooting Log
- **Version Substring Extraction**: Standardized `sed` pattern matching to prevent syntax mismatches across environment distributions.
- **Commit Categorization**: Configured `git log` pattern filters to capture conventional commits while falling back cleanly for initial builds.
