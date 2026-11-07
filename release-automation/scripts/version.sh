#!/bin/bash
VERSION_FILE="src/app.py"
CURRENT_VERSION=$(grep __version__ "$VERSION_FILE" | cut -d'"' -f2)

function get_version() {
    echo "$CURRENT_VERSION"
}

function bump_version() {
    local bump_type=$1
    IFS='.' read -r major minor patch <<< "$CURRENT_VERSION"
    
    case $bump_type in
        major)
            major=$((major + 1))
            minor=0
            patch=0
            ;;
        minor)
            minor=$((minor + 1))
            patch=0
            ;;
        patch)
            patch=$((patch + 1))
            ;;
        *)
            echo "Usage: $0 {major|minor|patch}"
            exit 1
            ;;
    esac
    
    NEW_VERSION="$major.$minor.$patch"
    sed -i "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" "$VERSION_FILE"
    
    echo "Version bumped: $CURRENT_VERSION -> $NEW_VERSION"
    echo "$NEW_VERSION"
}

case "${1:-get}" in
    get)
        get_version
        ;;
    major|minor|patch)
        bump_version "$1"
        ;;
    *)
        echo "Usage: $0 {get|major|minor|patch}"
        exit 1
        ;;
esac
