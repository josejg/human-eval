import pathlib

from human_eval.data import read_problems


def make_humanreadable_files():
    base_path = pathlib.Path("./problems")
    base_path.mkdir(exist_ok=True, parents=True)

    data = read_problems()

    for example in data.values():
        _, n = example["task_id"].split("/")
        name = f"P{int(n):03d}"
        prompt = example["prompt"]
        solution = example["canonical_solution"]
        test = example["test"]

        dump = f"""#!/usr/bin/env python
# NAME: {name}
# PROMPT: {prompt}

# SOLUTION:
{solution}

# TESTS
{test}
    """

        with open(base_path / f"{name}.py", "w") as f:
            print(dump, file=f)

if __name__ == "__main__":
    make_humanreadable_files()
