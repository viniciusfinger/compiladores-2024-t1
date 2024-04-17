Feature: Provê um analizador léxico para um compilador de um subset da linguagem Pascal.

Narrative:
    Para implementar um compilador da linguagem Pascal,
    Como um desenvolvedor de software,
    Quero um analisador léxico que extraia os tokens de um código fonte.


Scenario: Análise léxica de um programa correto.
Given um programa Pascal
    """
    program teste;
    var
        a, b: integer;
    begin
        a := 2;
        b := 3;
        writeln(a + b);
    end;
    """
When a análise léxica é executada
Then nenhum erro ocorre
    And são gerados os tokens
    #
    # O formato da resposta é gerado internamente, pelo teste.
    # O dados vem dos campos token type e token.value, organizados
    # da seguinte forma:
    #
    #     (token.value[0], token.type, token.value[1])
    #
    # Ou seja, o valor de token.value deve conter (<match>, <num_linha>)
    #
    """
    ("program", DIR_PROGRAM, 1)
    ("teste", ID, 1)
    (";", OP_EOC, 1)
    ("var", DIR_VAR, 2)
    ("a", ID, 3)
    (",", OP_COMMA, 3)
    ("b", ID, 3)
    (":", OP_COLON, 3)
    ("integer", TYPE_INTEGER, 3)
    (";", OP_EOC, 3)
    ("begin", DIR_BEGIN, 4)
    ("a", ID, 5)
    (":=", OP_ATRIB, 5)
    (2, LIT_INT, 5)
    (";", OP_EOC, 5)
    ("b", ID, 6)
    (":=", OP_ATRIB, 6)
    (3, LIT_INT, 6)
    (";", OP_EOC, 6)
    ("writeln", FN_WRITELN, 7)
    ("(", OP_OPAR, 7)
    ("a", ID, 7)
    ("+", OP_SUM, 7)
    ("b", ID, 7)
    (")", OP_CPAR, 7)
    (";", OP_EOC, 7)
    ("end", DIR_END, 8)
    (".", OP_PERIOD, 8)
    """


Scenario: Análise léxica com identificadores inválido
Given um programa Pascal
    """
    program teste;
    var
        exceção: integer;
    begin
        exceção := 10;
        writeln(exceção);
    end.
    """
When a análise léxica é executada
Then são gerados os tokens
    """
    ("program", DIR_PROGRAM, 1)
    ("teste", ID, 1)
    (";", OP_EOC, 1)
    ("var", DIR_VAR, 2)
    ("exce", ID, 3)
    """
    And é gerada a exceção LexerException
    And o símbolo que causou o erro é "ç"
    And a exeção ocorreu na linha 3
    # teste opcional
    And o erro ocorreu no caracter da posição 8 da linha

