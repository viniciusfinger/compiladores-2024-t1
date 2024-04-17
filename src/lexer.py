"""Implantação do analisador léxico."""

import ply.lex

import errors


@ply.lex.TOKEN(r"\n+")
def t_ignore_newline(token):
    """Conto o número de linhas."""
    token.lexer.lineno += token.value.count("\n")


def lexer():
    """Cria o objeto do analisador léxico."""
    return ply.lex.lex()
