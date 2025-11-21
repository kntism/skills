#!/usr/bin/env python3
"""
Clean Code Analyzer
Analyzes code files for Clean Code principle violations
"""

import ast
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class Violation:
    """Represents a Clean Code violation"""
    rule_category: str
    rule_name: str
    severity: str  # 'error', 'warning', 'info'
    line_number: int
    description: str
    suggestion: str
    code_snippet: str


class CleanCodeAnalyzer:
    """Main analyzer class for Clean Code principles"""

    def __init__(self, language: str):
        self.language = language.lower()
        self.violations: List[Violation] = []

        # Define Clean Code rules
        self.rules = {
            'naming': self._check_naming_conventions,
            'functions': self._check_function_design,
            'comments': self._check_comments,
            'formatting': self._check_formatting,
            'error_handling': self._check_error_handling,
            'duplication': self._check_duplication,
            'complexity': self._check_complexity,
            'testability': self._check_testability,
            'design_patterns': self._check_design_patterns,
            'magic_numbers': self._check_magic_numbers
        }

    def analyze(self, file_path: str) -> List[Violation]:
        """Analyze a file for Clean Code violations"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                lines = content.split('\n')

            self.violations = []

            # Apply all rules
            for rule_name, rule_func in self.rules.items():
                try:
                    rule_func(content, lines)
                except Exception as e:
                    print(f"Warning: Rule {rule_name} failed: {e}")

            return sorted(self.violations, key=lambda v: (v.severity, v.line_number))

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file: {e}")

    def _check_naming_conventions(self, content: str, lines: List[str]):
        """Check naming convention violations"""

        # Variable/Function naming patterns
        if self.language in ['js', 'ts']:
            # camelCase for variables and functions
            pattern = r'\b(let|const|var|function)\s+([a-z][a-zA-Z0-9_]*)'
            for i, line in enumerate(lines, 1):
                matches = re.finditer(pattern, line)
                for match in matches:
                    if '_' in match.group(2):
                        self.violations.append(Violation(
                            'naming', 'camelCaseConvention', 'error',
                            i, f"Use camelCase: {match.group(2)}",
                            "Change variable/function name to camelCase",
                            line.strip()
                        ))

        elif self.language == 'python':
            # snake_case for variables and functions
            pattern = r'\b(def|class)\s+([a-zA-Z_][a-zA-Z0-9_]*)'
            for i, line in enumerate(lines, 1):
                matches = re.finditer(pattern, line)
                for match in matches:
                    name = match.group(2)
                    if name != name.lower() and '_' not in name:
                        self.violations.append(Violation(
                            'naming', 'snakeCaseConvention', 'error',
                            i, f"Use snake_case: {name}",
                            "Change function/class name to snake_case",
                            line.strip()
                        ))

    def _check_function_design(self, content: str, lines: List[str]):
        """Check function design principles"""

        if self.language in ['js', 'ts']:
            # Function length check
            function_pattern = r'function\s+\w+\s*\([^)]*\)\s*{([^}]*)}'
            for i, line in enumerate(lines, 1):
                if 'function ' in line:
                    # Find the complete function
                    func_start = i - 1
                    func_lines = [line]
                    brace_count = line.count('{') - line.count('}')

                    j = i
                    while j < len(lines) and brace_count > 0:
                        brace_count += lines[j].count('{') - lines[j].count('}')
                        func_lines.append(lines[j])
                        j += 1

                    func_content = '\n'.join(func_lines)
                    if len(func_lines) > 20:
                        self.violations.append(Violation(
                            'functions', 'functionLength', 'warning',
                            func_start, f"Function is too long ({len(func_lines)} lines)",
                            "Break down into smaller functions",
                            func_content[:100] + "..."
                        ))

        elif self.language == 'python':
            # Function length check
            for i, line in enumerate(lines, 1):
                if line.strip().startswith('def '):
                    func_start = i - 1
                    func_lines = []
                    indent_level = len(line) - len(line.lstrip())

                    j = i
                    while j < len(lines):
                        current_indent = len(lines[j]) - len(lines[j].lstrip())
                        if lines[j].strip() and current_indent <= indent_level:
                            break
                        func_lines.append(lines[j])
                        j += 1

                    if len(func_lines) > 20:
                        self.violations.append(Violation(
                            'functions', 'functionLength', 'warning',
                            func_start, f"Function is too long ({len(func_lines)} lines)",
                            "Break down into smaller functions",
                            '\n'.join(func_lines[:3]) + "..."
                        ))

    def _check_comments(self, content: str, lines: List[str]):
        """Check comment quality and usage"""

        for i, line in enumerate(lines, 1):
            # Check for useless comments
            stripped = line.strip()
            if stripped.startswith('//') or stripped.startswith('#'):
                comment = stripped[1:].strip()
                # Check for obvious comments that just repeat code
                if (comment.lower() in ['todo', 'fixme', 'hack'] or
                    comment.lower().startswith('this function') or
                    comment.lower().startswith('this variable')):
                    self.violations.append(Violation(
                        'comments', 'uselessComment', 'info',
                        i, f"Potentially useless comment: {comment}",
                        "Remove or make the comment more meaningful",
                        line.strip()
                    ))

    def _check_formatting(self, content: str, lines: List[str]):
        """Check code formatting issues"""

        for i, line in enumerate(lines, 1):
            # Check line length
            if len(line) > 100:
                self.violations.append(Violation(
                    'formatting', 'lineLength', 'warning',
                    i, f"Line too long ({len(line)} characters)",
                    "Break line or shorten variable names",
                    line.strip()
                ))

            # Check for trailing whitespace
            if line.rstrip() != line:
                self.violations.append(Violation(
                    'formatting', 'trailingWhitespace', 'info',
                    i, "Line has trailing whitespace",
                    "Remove trailing whitespace",
                    line.strip()
                ))

    def _check_error_handling(self, content: str, lines: List[str]):
        """Check error handling patterns"""

        for i, line in enumerate(lines, 1):
            # Check for empty catch blocks
            if self.language in ['js', 'ts'] and 'catch' in line and '{' in line:
                # Find catch block
                j = i
                while j < len(lines) and not lines[j].strip().endswith('}'):
                    if 'console.log' in lines[j] or 'throw' in lines[j]:
                        break
                    if lines[j].strip() and not lines[j].strip().startswith('//'):
                        self.violations.append(Violation(
                            'error_handling', 'emptyCatch', 'warning',
                            j, "Empty catch block or only console.log",
                            "Add proper error handling or re-throw",
                            lines[j].strip()
                        ))
                    j += 1

            elif self.language == 'python' and 'except' in line:
                if ':' in line and (line.strip().endswith(':') or
                    (i < len(lines) and not lines[i].strip().startswith('pass') and
                     not lines[i].strip().startswith('#'))):
                    continue
                else:
                    self.violations.append(Violation(
                        'error_handling', 'poorExcept', 'warning',
                        i, "Poor exception handling",
                        "Add proper error handling logic",
                        line.strip()
                    ))

    def _check_duplication(self, content: str, lines: List[str]):
        """Check for code duplication"""
        # Basic duplicate line detection
        line_counts = {}
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped and not stripped.startswith(('#', '//', '/*', '*/')):
                line_counts[stripped] = line_counts.get(stripped, []) + [i]

        for line, occurrences in line_counts.items():
            if len(occurrences) > 2 and len(line) > 20:  # Avoid short repeated lines
                self.violations.append(Violation(
                    'duplication', 'duplicateCode', 'warning',
                    occurrences[0], f"Duplicate code found ({len(occurrences)} times)",
                    "Extract to a function or utility",
                    line
                ))

    def _check_complexity(self, content: str, lines: List[str]):
        """Check code complexity"""

        for i, line in enumerate(lines, 1):
            # Check for deep nesting
            if line.strip().startswith(('if ', 'for ', 'while ', 'with ')):
                nesting_level = len(line) - len(line.lstrip())
                if nesting_level > 8:
                    self.violations.append(Violation(
                        'complexity', 'deepNesting', 'warning',
                        i, f"Deep nesting level ({nesting_level//4})",
                        "Use guard clauses or extract to function",
                        line.strip()
                    ))

    def _check_testability(self, content: str, lines: List[str]):
        """Check testability issues"""

        # Check for hardcoded values that make testing difficult
        for i, line in enumerate(lines, 1):
            if any(keyword in line.lower() for keyword in ['new date()', 'datetime.now()', 'math.random']):
                self.violations.append(Violation(
                    'testability', 'hardcodedDependencies', 'warning',
                    i, "Hardcoded time/random values make testing difficult",
                    "Inject dependencies or use test doubles",
                    line.strip()
                ))

    def _check_design_patterns(self, content: str, lines: List[str]):
        """Check appropriate design pattern usage"""
        # Basic check for overly complex classes
        class_count = 0
        function_count = 0

        for line in lines:
            if 'class ' in line:
                class_count += 1
            elif 'function ' in line or 'def ' in line:
                function_count += 1

        if class_count > 10:
            self.violations.append(Violation(
                'design_patterns', 'tooManyClasses', 'warning',
                1, f"Too many classes ({class_count}) in single file",
                "Consider breaking into modules",
                "File structure analysis"
            ))

    def _check_magic_numbers(self, content: str, lines: List[str]):
        """Check for magic numbers"""

        # Pattern to find numbers that might be magic numbers
        number_pattern = r'\b\d+\b'
        for i, line in enumerate(lines, 1):
            matches = re.finditer(number_pattern, line)
            for match in matches:
                num = int(match.group())
                # Skip common numbers that are usually not magic
                if num not in [0, 1, 2, 10, 100, 1000] and len(str(num)) > 1:
                    # Check if it's in a context that suggests it's a magic number
                    if any(ctx in line.lower() for ctx in ['=', '+', '-', '*', '/', 'if', 'for']):
                        self.violations.append(Violation(
                            'magic_numbers', 'magicNumber', 'info',
                            i, f"Potential magic number: {num}",
                            "Replace with a named constant",
                            line.strip()
                        ))


def main():
    parser = argparse.ArgumentParser(description='Analyze code for Clean Code violations')
    parser.add_argument('--file', required=True, help='Path to the code file to analyze')
    parser.add_argument('--language', required=True, choices=['js', 'ts', 'python'],
                       help='Programming language of the file')
    parser.add_argument('--output', choices=['text', 'json'], default='text',
                       help='Output format')

    args = parser.parse_args()

    try:
        analyzer = CleanCodeAnalyzer(args.language)
        violations = analyzer.analyze(args.file)

        if args.output == 'json':
            import json
            result = {
                'file': args.file,
                'language': args.language,
                'total_violations': len(violations),
                'violations': [
                    {
                        'category': v.rule_category,
                        'rule': v.rule_name,
                        'severity': v.severity,
                        'line': v.line_number,
                        'description': v.description,
                        'suggestion': v.suggestion,
                        'snippet': v.code_snippet
                    }
                    for v in violations
                ]
            }
            print(json.dumps(result, indent=2))
        else:
            print(f"\nClean Code Analysis Report")
            print(f"File: {args.file}")
            print(f"Language: {args.language.upper()}")
            print(f"Total Violations: {len(violations)}\n")

            if not violations:
                print("No Clean Code violations found!")
            else:
                for violation in violations:
                    severity_icon = {'error': '[ERROR]', 'warning': '[WARN]', 'info': '[INFO]'}
                    print(f"{severity_icon[violation.severity]} Line {violation.line_number}: {violation.description}")
                    print(f"   Suggestion: {violation.suggestion}")
                    print(f"   Code: {violation.code_snippet[:50]}...\n")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()