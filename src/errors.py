"""Erros do compilador."""


class LexerException(Exception):
    """Provê uma classe base para exceções do analisador léxico."""

    def __init__(self, value, line, index=-1):
        self.value = value
        self.line = line
        self.index = index
        Exception.__init__(self, "Invalid input.")

    def __str__(self):
        return (
            f"{Exception.__str__(self)}:{self.line}:{self.index}: "
            f"'{self.value}'"
        )
