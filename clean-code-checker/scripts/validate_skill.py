#!/usr/bin/env python3
"""
Skill Validator
Validates a skill meets all requirements before packaging
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import yaml
except ImportError:
    yaml = None


def validate_skill(skill_path: str) -> Tuple[bool, str]:
    """Validate a skill meets all requirements"""
    skill_dir = Path(skill_path)

    # Check if directory exists
    if not skill_dir.exists():
        return False, f"Skill directory does not exist: {skill_path}"

    # Check for required SKILL.md file
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return False, "Required SKILL.md file not found"

    # Validate SKILL.md content
    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for YAML frontmatter
        if not content.startswith('---'):
            return False, "SKILL.md must start with YAML frontmatter"

        # Extract frontmatter
        frontmatter_end = content.find('---', 3)
        if frontmatter_end == -1:
            return False, "SKILL.md has invalid YAML frontmatter"

        frontmatter = content[3:frontmatter_end]

        # Parse YAML
        if yaml:
            try:
                metadata = yaml.safe_load(frontmatter)
            except yaml.YAMLError as e:
                return False, f"SKILL.md has invalid YAML: {e}"
        else:
            # Simple manual parsing if yaml module not available
            metadata = {}
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip().strip('"\'')

        # Check required fields
        required_fields = ['name', 'description']
        for field in required_fields:
            if field not in metadata:
                return False, f"SKILL.md missing required field: {field}"

        # Validate content
        errors = []
        if not metadata['name'].replace('-', '').replace('_', '').replace(' ', '').isalnum():
            errors.append("Skill name should contain only alphanumeric characters, hyphens, underscores, and spaces")

        if len(metadata['description']) < 10:
            errors.append("Description should be at least 10 characters long")

        if not metadata['description'].endswith('.'):
            errors.append("Description should end with a period")

        if errors:
            return False, "; ".join(errors)

    except Exception as e:
        return False, f"Error reading SKILL.md: {e}"

    # Check optional directories
    optional_dirs = ['scripts', 'references', 'assets']
    for dir_name in optional_dirs:
        dir_path = skill_dir / dir_name
        if dir_path.exists():
            if not dir_path.is_dir():
                return False, f"{dir_name} should be a directory"

            # Validate file extensions in directories
            if dir_name == 'scripts':
                script_extensions = ['.py', '.js', '.ts', '.sh']
                for file_path in dir_path.rglob('*'):
                    if file_path.is_file():
                        if not any(file_path.suffix.endswith(ext) for ext in script_extensions):
                            return False, f"Invalid file extension in scripts directory: {file_path}"

    return True, "Skill validation passed"


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <skill-path>")
        sys.exit(1)

    skill_path = sys.argv[1]
    valid, message = validate_skill(skill_path)

    if valid:
        print(f"PASS: {message}")
        sys.exit(0)
    else:
        print(f"FAIL: {message}")
        sys.exit(1)


if __name__ == "__main__":
    main()