#!/bin/bash
set -e

VERSION=${1:-$(./scripts/version.sh get)}
PREVIOUS_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
OUTPUT_FILE="RELEASE_NOTES_${VERSION}.md"

echo "Generating release notes for version $VERSION..."

cat > "$OUTPUT_FILE" << HEADER
# Release Notes - Version $VERSION

**Release Date:** $(date '+%Y-%m-%d')

## Changes

HEADER

if [ -n "$PREVIOUS_TAG" ]; then
    echo "Changes since $PREVIOUS_TAG:" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    echo "### Features" >> "$OUTPUT_FILE"
    git log "$PREVIOUS_TAG"..HEAD --pretty=format:"- %s (%h)" --grep="^feat" >> "$OUTPUT_FILE" 2>/dev/null || echo "- No new features" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    echo "### Bug Fixes" >> "$OUTPUT_FILE"
    git log "$PREVIOUS_TAG"..HEAD --pretty=format:"- %s (%h)" --grep="^fix" >> "$OUTPUT_FILE" 2>/dev/null || echo "- No bug fixes" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
else
    echo "Initial release - all commits:" >> "$OUTPUT_FILE"
    git log --pretty=format:"- %s (%h)" >> "$OUTPUT_FILE"
fi

echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "Release notes generated: $OUTPUT_FILE"
cat "$OUTPUT_FILE"
