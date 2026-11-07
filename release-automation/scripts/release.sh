#!/bin/bash
# Complete release automation script

set -e

RELEASE_TYPE=${1:-patch}

echo "=== Starting Release Process ==="
echo "Release Type: $RELEASE_TYPE"

# Step 1: Bump version
echo "Step 1: Bumping version..."
NEW_VERSION=$(./scripts/version.sh "$RELEASE_TYPE" | tail -n 1)

# Step 2: Run build
echo "Step 2: Running build..."
./scripts/build.sh

# Step 3: Commit version change
echo "Step 3: Committing version change..."
git add src/app.py
git commit -m "chore: bump version to $NEW_VERSION"

# Step 4: Create git tag
echo "Step 4: Creating git tag..."
git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION"

# Step 5: Generate release notes
echo "Step 5: Generating release notes..."
./scripts/generate-release-notes.sh "$NEW_VERSION"

# Step 6: Create release package
echo "Step 6: Creating release package..."
RELEASE_DIR="releases/v$NEW_VERSION"
mkdir -p "$RELEASE_DIR"
cp -r build/release-*/* "$RELEASE_DIR/"
cp "RELEASE_NOTES_${NEW_VERSION}.md" "$RELEASE_DIR/"

echo ""
echo "=== Release Complete ==="
echo "Version: $NEW_VERSION"
echo "Tag: v$NEW_VERSION"
echo "Release Package: $RELEASE_DIR"
echo ""
echo "Next steps:"
echo "  - Review release notes: cat RELEASE_NOTES_${NEW_VERSION}.md"
echo "  - Push to remote: git push origin main --tags"
