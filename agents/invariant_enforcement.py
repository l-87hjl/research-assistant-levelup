import re
from agents.modes import ModeViolationError

CODE_BLOCK_PATTERN = re.compile(r"```")


def assert_no_code_blocks(text_items):
    for item in text_items:
        if CODE_BLOCK_PATTERN.search(item):
            raise ModeViolationError("Code blocks detected in research output")
