"""Erros do compilador."""


class LexerException(Exception):
    """Provê uma classe base para exceções do analisador léxico."""

    def __init__(self, value, line, index=-1):
        """Cria uma exceção do analisador léxico."""
        self.value = value
        self.line = line
        self.index = index
        Exception.__init__(self, "Invalid input.")

    def __str__(self):
        """Retorna a mensagem de erro formatada como string."""
        return (
            f"{Exception.__str__(self)}:{self.line}:{self.index}: "
            f"'{self.value}'"
        )
