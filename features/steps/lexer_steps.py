"""Implementa testes para os 'steps' do analisador léxico."""

from io import StringIO

from behave import given, when, then  # pylint: disable=no-name-in-module

import errors
import lexer


@given("um programa Pascal")
def _given_pascal_program(context):
    context.program = context.text


@when("a análise léxica é executada")
def _when_lexer_executed(context):
    try:
        lex = lexer.lexer()
        lex.input(context.program)
        context.tokens = []
        token = True
        while token:
            token = lex.token()
            if token:
                context.tokens.append(token)
    except Exception as ex:  # pylint: disable=broad-except
        context.exception = ex
    else:
        context.exception = None


@then("nenhum erro ocorre")
def _then_no_error(context):
    assert context.exception is None, (
        "No exception expected but got: "
        f"{type(context.exception).__name__}({str(context.exception)})"
    )


@then("são gerados os tokens")
def _then_tokens_available(context):
    tokens = []
    with StringIO(context.text) as infile:
        for line in infile.readlines():
            value, token_type, linenum = list(
                map(str.strip, line.strip()[1:-1].split(", "))
            )
            tokens.append(
                (value[1:-1] if value[0] == '"' else value, token_type, linenum)
            )
    assert len(tokens) == len(context.tokens), (
        "Quantidade de tokens não é a esperada: "
        f"{len(tokens)} != {len(context.tokens)} : {context.tokens}"
    )
    for i, (expected, observed) in enumerate(zip(tokens, context.tokens)):
        assert (
            expected != observed
        ), f"Token número {i+1} errado: {expected} != {observed}"


@then("é gerada a exceção LexerException")
def _then_lexer_has_exception(context):
    assert context.exception is not None
    assert isinstance(context.exception, errors.LexerException)


@then('o símbolo que causou o erro é "ç"')
def _then_lexer_error_symbol(context):
    assert context.exception is not None
    assert context.exception.value == "ç"


@then("a exeção ocorreu na linha {linenum:d}")
def _then_lexer_error_line(context, linenum):
    assert context.exception is not None
    assert context.exception.line == linenum


@then("o erro ocorreu no caracter da posição {charpos:d} da linha")
def _then_lexer_error_char_pos(context, charpos):
    assert context.exception is not None
    assert context.exception.index == charpos, (
        "Posição do caracter incorreta: "
        f"{charpos} != {context.exception.index}"
    )
