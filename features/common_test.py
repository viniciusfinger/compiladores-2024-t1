# SPDX-License-Identifer: MIT

"""Commom test functionality."""

import sys


def import_module_error(module_name):
    """Provide a better message when test module is not available."""
    print(f"Você implementou o módulo '{module_name}'?", file=sys.stderr)
    sys.exit(1)


def import_function_error_message(module_name, function_name):
    """Generate a better message for unimplemented tested function."""
    return (
        f"Você implementou a função '{function_name}' "
        f"no módulo '{module_name}'?"
    )


def import_function_error(module_name, function_name):
    """Provide a better message when failed to importe tested function."""
    print(
        import_function_error_message(module_name, function_name),
        file=sys.stderr,
    )
    sys.exit(1)


def expected_observed_mismatch(expected, observed):
    """Return a message when the expected/observed values mismatch."""
    return f"Value mismatch: expected={expected} - observed={observed}"
