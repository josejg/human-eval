import re

def extract_python_code_blocks(markdown_text: str) -> list:
    # Define the regular expression pattern for Python code blocks
    # Optional 'python' syntax declaration
    pattern = r"```(?:python)?\n(.*?)```"

    # Use re.DOTALL to make the '.' special character match any character at all, including a newline
    matches = re.findall(pattern, markdown_text, re.DOTALL)

    return matches


def basic_sanitize(completion: str) -> str:
    stop_words = [
        "\nclass", "\n#", "\ndef", "\nassert", '\n"', "\nprint", "\nif",
    ]
    regex = '(' + '|'.join(stop_words) + ')'
    return re.split(regex, completion)[0]


def prepare_solution(problem, completion):
    entry_point = problem["entry_point"]

    # Deal with markdown, this is the common case for instruction
    # following models
    if '```' in completion:
        if completion.count('```') % 2 != 0:
            completion += '\n```'
        blocks = extract_python_code_blocks(completion)
        for block in blocks:
            if f'def {entry_point}(' in block:
                completion = block
                break
        else:
            completion = blocks[0]

    # Ensure the completion has the entry point
    # This is the common case for base models
    if f'def {entry_point}(' not in completion or completion.startswith('  '):
        completion = basic_sanitize(completion)

    # elif not completion.startswith(problem["prompt"]):
    #     # include prompt so imports are included
    #     completion = completion

    return completion
