#!/bin/bash

# Read JSON input from stdin (Claude Code passes hook context as JSON)
INPUT=$(cat)

# Extract the user's prompt text
PROMPT_TEXT=$(echo "$INPUT" | jq -r '.prompt')

# Skip if prompt is empty or null
if [ -z "$PROMPT_TEXT" ] || [ "$PROMPT_TEXT" = "null" ]; then
    exit 0
fi

# Translate using pre_hook.py (use venv Python where google-genai is installed)
TRANSLATED=$("$CLAUDE_PROJECT_DIR/.venv/bin/python3" "$CLAUDE_PROJECT_DIR/pre_hook.py" "$PROMPT_TEXT" 2>/dev/null)

# If translation succeeded, return it as additional context
if [ -n "$TRANSLATED" ] && [ "$TRANSLATED" != "$PROMPT_TEXT" ]; then
    echo "[翻译 Translation]"
    echo "原文: $PROMPT_TEXT"
    echo "译文: $TRANSLATED"
fi

exit 0
