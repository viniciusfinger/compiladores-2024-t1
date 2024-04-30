"""Programa de teste para auxiliar no desenvolvimento."""

# Nota: Este arquivo é para uso livre, não será avaliado.

from lexer import lexer
import errors


if __name__ == "__main__":
    try:
        with open("write_a_plus_b_int.pas", "rt", encoding="utf-8") as input_file:
            lex = lexer()
            lex.input(input_file.read())
            TOKEN = True
            while TOKEN:
                TOKEN = lex.token()
                if TOKEN:
                    print((TOKEN.value, TOKEN.type, TOKEN.lineno))
    except errors.LexerException as lexerror:
        print(f"ERROR: {str(lexerror)}")
