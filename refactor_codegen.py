import re
import sys
from pathlib import Path

# Mapping of Playwright methods to framework methods
REPLACEMENTS = [
    (r'page\\.click\\(([^)]+)\\)', r'click_with_retry(page, \1)'),
    (r'page\\.wait_for_selector\\(([^)]+)\\)', r'wait_for_element(page, \1)'),
]

IMPORTS = '''from playwright_pytest_framework.utils import wait_for_element\nfrom playwright_pytest_framework.actions import click_with_retry\n'''

def refactor_code(input_code: str) -> str:
    code = input_code
    for pattern, repl in REPLACEMENTS:
        code = re.sub(pattern, repl, code)
    # Optionally, add imports if not present
    if 'click_with_retry' in code or 'wait_for_element' in code:
        code = IMPORTS + code
    return code

def main():
    if len(sys.argv) < 2:
        print("Usage: python refactor_codegen.py <input_file.py>")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    output_path = input_path.with_name(input_path.stem + '_refactored.py')
    with open(input_path, 'r') as f:
        input_code = f.read()
    refactored = refactor_code(input_code)
    with open(output_path, 'w') as f:
        f.write(refactored)
    print(f"Refactored code written to {output_path}")

if __name__ == "__main__":
    main() 