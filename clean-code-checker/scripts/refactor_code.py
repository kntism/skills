#!/usr/bin/env python3
"""
Clean Code Refactorer
Applies Clean Code optimizations to code files
"""

import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class RefactoringRule:
    """Represents a refactoring rule that can be applied"""
    name: str
    category: str
    description: str
    apply_function: callable


class CleanCodeRefactorer:
    """Main refactoring class for Clean Code principles"""

    def __init__(self, language: str):
        self.language = language.lower()
        self.refactored_lines: List[str] = []
        self.rules_applied: Set[str] = set()

    def refactor(self, file_path: str, rules: List[str] = None) -> Dict[str, Any]:
        """Refactor a file according to Clean Code principles"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            self.refactored_lines = lines.copy()
            self.rules_applied = set()

            # Apply refactoring rules
            all_rules = self._get_all_rules()

            if rules:
                # Apply only specified rules
                for rule_name in rules:
                    if rule_name in all_rules:
                        all_rules[rule_name].apply_function(self)
                        self.rules_applied.add(rule_name)
            else:
                # Apply all rules
                for rule in all_rules.values():
                    try:
                        rule.apply_function(self)
                        self.rules_applied.add(rule.name)
                    except Exception as e:
                        print(f"Warning: Rule {rule.name} failed: {e}")

            # Save refactored code
            if self.rules_applied:
                backup_path = f"{file_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                with open(backup_path, 'w', encoding='utf-8') as backup_file:
                    backup_file.writelines(lines)

                with open(file_path, 'w', encoding='utf-8') as output_file:
                    output_file.writelines(self.refactored_lines)

                return {
                    'success': True,
                    'rules_applied': list(self.rules_applied),
                    'backup_file': backup_path,
                    'changes_count': len(self.refactored_lines) - len(lines)
                }
            else:
                return {
                    'success': True,
                    'rules_applied': [],
                    'backup_file': None,
                    'changes_count': 0
                }

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'rules_applied': list(self.rules_applied)
            }

    def _get_all_rules(self) -> Dict[str, RefactoringRule]:
        """Get all available refactoring rules"""
        return {
            'fix_naming': RefactoringRule(
                'fix_naming', 'naming',
                'Fix naming conventions',
                self._fix_naming_conventions
            ),
            'shorten_functions': RefactoringRule(
                'shorten_functions', 'functions',
                'Break down long functions',
                self._shorten_functions
            ),
            'remove_trailing_whitespace': RefactoringRule(
                'remove_trailing_whitespace', 'formatting',
                'Remove trailing whitespace',
                self._remove_trailing_whitespace
            ),
            'break_long_lines': RefactoringRule(
                'break_long_lines', 'formatting',
                'Break long lines',
                self._break_long_lines
            ),
            'extract_constants': RefactoringRule(
                'extract_constants', 'magic_numbers',
                'Extract magic numbers to constants',
                self._extract_constants
            ),
            'improve_error_handling': RefactoringRule(
                'improve_error_handling', 'error_handling',
                'Improve error handling',
                self._improve_error_handling
            ),
            'remove_useless_comments': RefactoringRule(
                'remove_useless_comments', 'comments',
                'Remove useless comments',
                self._remove_useless_comments
            )
        }

    def _fix_naming_conventions(self):
        """Fix naming convention violations"""

        if self.language in ['js', 'ts']:
            # Convert snake_case to camelCase
            for i, line in enumerate(self.refactored_lines):
                # Fix variable declarations
                line = re.sub(r'\b(let|const|var)\s+([a-z][a-zA-Z0-9_]*)',
                             lambda m: f"{m.group(1)} {self._to_camel_case(m.group(2))}", line)
                # Fix function names
                line = re.sub(r'\bfunction\s+([a-z][a-zA-Z0-9_]*)',
                             lambda m: f"function {self._to_camel_case(m.group(1))}", line)
                self.refactored_lines[i] = line

        elif self.language == 'python':
            # Convert camelCase to snake_case
            for i, line in enumerate(self.refactored_lines):
                # Fix function names
                line = re.sub(r'\bdef\s+([a-z][a-zA-Z0-9_]*)',
                             lambda m: f"def {self._to_snake_case(m.group(1))}", line)
                # Fix class names
                line = re.sub(r'\bclass\s+([A-Z][a-zA-Z0-9_]*)',
                             lambda m: f"class {self._to_snake_case(m.group(1))}", line)
                self.refactored_lines[i] = line

    def _shorten_functions(self):
        """Attempt to break down long functions"""
        # This is a simplified version - in practice, you'd need more sophisticated AST parsing
        if self.language in ['js', 'ts']:
            self.refactored_lines = [
                line if len(line) <= 80 else self._break_js_line(line)
                for line in self.refactored_lines
            ]
        else:
            self.refactored_lines = [
                line if len(line) <= 80 else self._break_python_line(line)
                for line in self.refactored_lines
            ]

    def _remove_trailing_whitespace(self):
        """Remove trailing whitespace from all lines"""
        for i, line in enumerate(self.refactored_lines):
            self.refactored_lines[i] = line.rstrip() + '\n'

    def _break_long_lines(self):
        """Break long lines into multiple lines"""
        for i, line in enumerate(self.refactored_lines):
            if len(line) > 100:
                if self.language in ['js', 'ts']:
                    self.refactored_lines[i] = self._break_js_line(line)
                else:
                    self.refactored_lines[i] = self._break_python_line(line)

    def _extract_constants(self):
        """Extract magic numbers to constants"""
        # Find common magic numbers and replace them
        magic_numbers = {
            '1000': 'MAX_ITEMS',
            '100': 'DEFAULT_TIMEOUT',
            '50': 'MAX_RESULTS',
            '10': 'DEFAULT_LIMIT',
            '5': 'RETRY_COUNT'
        }

        for i, line in enumerate(self.refactored_lines):
            for num, const_name in magic_numbers.items():
                if num in line:
                    # Add constant declaration at top if not exists
                    if i > 0 and not any(const_name in l for l in self.refactored_lines[:i]):
                        if self.language == 'python':
                            self.refactored_lines.insert(i, f"{const_name} = {num}\n")
                        else:
                            self.refactored_lines.insert(i, f"const {const_name} = {num};\n")
                        i += 1

                    # Replace number with constant
                    line = line.replace(num, const_name)
            self.refactored_lines[i] = line

    def _improve_error_handling(self):
        """Improve error handling patterns"""
        if self.language in ['js', 'ts']:
            for i, line in enumerate(self.refactored_lines):
                # Improve empty catch blocks
                if 'catch () {' in line:
                    self.refactored_lines[i] = line.replace('catch () {', 'catch (error) {')
                    if i + 1 < len(self.refactored_lines):
                        self.refactored_lines[i + 1] = f"    console.error('Error:', error);\n" + self.refactored_lines[i + 1]

        elif self.language == 'python':
            for i, line in enumerate(self.refactored_lines):
                # Improve bare except blocks
                if line.strip() == 'except:' and i + 1 < len(self.refactored_lines):
                    if self.refactored_lines[i + 1].strip() == 'pass':
                        self.refactored_lines[i] = line.replace('except:', 'except Exception as e:')
                        self.refactored_lines[i + 1] = "    logger.error(f'Error: {e}')\n"

    def _remove_useless_comments(self):
        """Remove obviously useless comments"""
        for i, line in enumerate(self.refactored_lines):
            stripped = line.strip()
            if (stripped.startswith('//') and (
                stripped.lower().startswith('// todo') or
                stripped.lower().startswith('// fixme') or
                stripped.lower().startswith('// hack') or
                stripped.lower().startswith('// this function')
            )):
                self.refactored_lines[i] = line.replace(stripped, '', 1)

    def _to_camel_case(self, snake_str: str) -> str:
        """Convert snake_case to camelCase"""
        components = snake_str.split('_')
        return components[0] + ''.join(word.capitalize() for word in components[1:])

    def _to_snake_case(self, camel_str: str) -> str:
        """Convert camelCase to snake_case"""
        result = []
        for i, char in enumerate(camel_str):
            if char.isupper() and i > 0:
                result.append('_')
            result.append(char.lower())
        return ''.join(result)

    def _break_js_line(self, line: str) -> str:
        """Break a long JavaScript line"""
        if '+' in line and 'template' not in line:
            parts = line.split('+')
            if len(parts) > 1:
                indent = len(line) - len(line.lstrip())
                spaces = ' ' * indent
                return parts[0] + ' +\n' + spaces + ' + '.join(parts[1:])
        return line

    def _break_python_line(self, line: str) -> str:
        """Break a long Python line"""
        if '(' in line and ')' in line:
            parts = line.split('(')
            if len(parts) > 1:
                indent = len(line) - len(line.lstrip())
                spaces = ' ' * indent
                return parts[0] + '(\n' + ' ' * (indent + 4) + ', '.join(parts[1].split(',')) + '\n' + spaces + ')'
        return line


def main():
    parser = argparse.ArgumentParser(description='Refactor code according to Clean Code principles')
    parser.add_argument('--file', required=True, help='Path to the code file to refactor')
    parser.add_argument('--language', required=True, choices=['js', 'ts', 'python'],
                       help='Programming language of the file')
    parser.add_argument('--rules', nargs='+',
                       help='Specific rules to apply (default: apply all rules)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be changed without actually modifying the file')

    args = parser.parse_args()

    try:
        refactorer = CleanCodeRefactorer(args.language)

        if args.dry_run:
            # Simulate refactoring without actually changing the file
            print(f"🔧 Dry run mode - What would be applied to {args.file}:")
            rules = refactorer._get_all_rules()
            if args.rules:
                for rule_name in args.rules:
                    if rule_name in rules:
                        print(f"  ✓ {rules[rule_name].description}")
                    else:
                        print(f"  ✗ Unknown rule: {rule_name}")
            else:
                for rule in rules.values():
                    print(f"  ✓ {rule.description}")
        else:
            result = refactorer.refactor(args.file, args.rules)

            if result['success']:
                print(f"✅ Refactoring completed successfully!")
                print(f"   Rules applied: {len(result['rules_applied'])}")
                print(f"   Changes made: {result['changes_count']} lines modified")

                if result['backup_file']:
                    print(f"   Backup saved to: {result['backup_file']}")

                if result['rules_applied']:
                    print("   Rules applied:")
                    for rule in result['rules_applied']:
                        print(f"     - {rule}")
            else:
                print(f"❌ Refactoring failed: {result['error']}")
                sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()