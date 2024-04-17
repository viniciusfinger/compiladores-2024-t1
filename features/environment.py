# SPDX-License-Identifer: MIT

"""Environment definition and grading implementation."""

import sys
import os
from behave.model import Status


# Code may be in "<repo>/src" directory
sys.path.append("src")

__grade = {"success": [], "failed": []}


def after_all(_context):
    """Save result to file RESULT."""
    positive = sum((value for _, value in __grade["success"]), 0)
    negative = sum((value for _, value in __grade["failed"]), 0)
    total = positive + negative
    with open("RESULT", "wt") as result_file:  # pylint: disable=W1514
        for result in ["success", "failed"]:
            result_msg = "\n\t".join(name for name, _ in __grade[result])
            msg = f"{result.capitalize()} scenarios:\n\t{result_msg}"
            # print(msg)
            print(msg, file=result_file)
        max_grade = os.environ.get("MAX_GRADE", total)
        # print("MAX", max_grade)
        # print("positive", positive)
        # print("negative", negative)
        grade_ratio = (max_grade * positive) / (1.0 * positive + negative)
        final_grade = int(10 * grade_ratio) / 10
        # print(f"Grade: {final_grade} / {max_grade}")
        print(f"{final_grade} / {max_grade}", file=result_file)


def after_scenario(_context, scenario):
    """Add scenario to proper grading list."""
    weight_tags = [
        tag
        for tag in scenario.tags
        if tag.startswith("value") or tag.startswith("peso")
    ] + ["default:1"]
    peso = weight_tags[0].split(":")[-1]
    result = "success" if scenario.status == Status.passed else "failed"
    __grade[result].append((scenario.name, float(peso)))
