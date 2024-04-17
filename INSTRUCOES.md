---
title: Implementação de um analisador léxico com PLY
date: 2024-05-01
---

## Objetivo

Experimentar sobre a implementação de um componente do processo de compilação, a análise léxica, utilizando uma ferramenta para criação dos automatos finitos para realização da tarefa.

Para esse experimento, será implementado um analisador léxico para um subconjunto da linguagem de programação [Pascal](https://pt.wikipedia.org/wiki/Pascal_\(linguagem_de_programa%C3%A7%C3%A3o\)).

## Pré-requisitos

* Todos os alunos necessitarão de contas no site [Github](https://github.com)
* Para o desenvolvimento serão utilizados os seguintes componentes:
    * `git`
    * `python`
    * [`ply`](https://github.com/dabeaz/ply)
    * `behave`

## Tarefas

1. Criar um _fork_ do projeto [`compiladores_2024_t1`](https://github.com/exercicios-programacao/compiladores_2024_t1)
2. Deve ser criado um "módulo" com o nome `lexer` com uma função `lexer` que irá retornar um objeto que realizará as operações da análise léxica.
3. O analisador léxico deve ser capaz de reconhecer diversos _tokens_. A lista a seguir mostra as construções que devem ser reconhecidas, associadas com o tipo do _token_:
    * identificadores (`ID`), por exemplo, nomes de funções e variáveis, devem começar com uma letra ou o carectere de "sublinhado" (`_`), seguidos de um número qualquer de letras, números ou "sublinhado".
    * Apenas caracteres alfanuméricos no conjunto ASCII-7 são aceitos na definição de identificadores.
    * Literais:
        * números inteiros (`123`), com tipo `LIT_INT`
        * números de ponto flutuante (`3.1425`) e números de ponto flutuante em notação científica (`1.24e-14`), com tipo `LIT_REAL`
        * As cadeias de caracteres (_strings_) devem estar entre aspas (`"`) ou apóstrofes(`'`), por exemplo, `'palavra'` e `"A"` são cadeias de caracteres, com tipo `LIT_STRING`.
    * Palavras reservadas da linguagem incluem:
        * Diretivas:
            ```nohl
            program (DIR_PROGRAM)
            var (DIR_VAR)
            procedure (DIR_PROC)
            function (DIR_FUNC)
            begin (DIR_BEGIN)
            end (DIR_END)
            type (DIR_TYPE)
            of (DIR_OF)
            const  (DIR_CONST)
            with (DIR_WITH)
```
        * Comandos:
        ```nohl
            if (STMT_IF)
            then (STMT_THEN)
            else (STMT_ELSE)
            while (STMT_WHILE)
            repeat (STMT_REPEAT)
            for (STMT_FOR)
            do (STMT_DO)
            until (STMT_UNTIL)
            to (STMT_TO)
            downto (STMT_DOWNTO)
            case (STMT_CASE)
```
        * Tipos de dados:
        ```nohl
            array (TYPE_ARRAY)
            set (TYPE_SET)
            record (TYPE_RECORD)
            file (TYPE_FILE)
            integer (TYPE_INT)
            real (TYPE_REAL)
            character (TYPE_CHAR)
            boolean (TYPE_BOOL)
            string (TYPE_STRING)
```
        * Funções _built-in_:
        ```nohl
            read    (FN_READ)
            readln  (FN_READLN)
            write   (FN_WRITE)
            writeln (FN_WRITELN)
```
        * Representação de valor nulo: `nil` (`OP_NIL`)
    * Operadores:
        * Atribuição: `:=` (`OP_ATRIB`)
        * Aritméticos: `+ -` (`OP_SUM`) `* / div mod` (`OP_MUL`)
        * Relacionais: `= <> <= >= > <` (`OP_REL`)
        * Lógicos: `and or not` (`OP_LOGIC`)
        * Range: `..` (`OP_RANGE`)
        * Comentários: (`COMMENT`)
            * Multi-linha: `{ }` ou `(* *)`
            * Fim de Linha: `//`
        * Outros operadores:
            * `(` (`OP_OPAR`)
            * `)` (`OP_CPAR`)
            * `[` (`OP_OBRA`)
            * `]` (`OP_CBRA`)
            * `,` (`OP_COMMA`)
            * `;` (`OP_EOC`)
            * `.` (`OP_PERIOD`)
            * `:` (`OP_COLON`)
4. O analisador léxico implementado deve controlar também o número da linha sendo processada no arquivo.
5. Os _tokens_ retornados pelo analisazdor léxico devem conter:
    * A string extraída
    * O tipo do token (de acordo com as tabelas anteriores)
    * A linha em que o token foi encontrado
    * E a representação do valor do token quando for adequado.
6. No caso do processamento encontrar um erro léxiro, deve ser gerada uma exceção com o caracter que gerou o erro, o número da linha onde ocorreu o erro, e a posição do caracter na linha onde ocorreu o erro.
7. Serão fornecidos testes automatizados para a avaliação do trabalho. Os testes podem ser executadosu utilizando o utilitário `behave` ou o utilitário `tox`, que podem ser instalados em um ambiente virtual do Python.

## Entrega do trabalho

Um único aluno do grupo de alunos que trabalhou na execução do trabalho deverá criar um _pull request_ contra o repositório original do trabalho. O título do _pull request_ é livre, porém o corpo deve conter os **nomes completos** de todos os alunos do grupo.

Uma vez criado o _pull request_ ele pode ser atualizado a qualquer momento, até a data limite de entrega.

Na data limite, o _pull request_ receberá um _label_ de `AVALIADO`, um comentário com o resultado da avaliação, será fechado, e não poderá mais ser alterado.

No `LEX`, **todos** os alunos do grupo devem inserir, até a data limite, o link para o _pull request_ de entrega do trabalho.

A data máxima de entrega é dia **1 de maio de 2024**.

## Observações

* Nenhum arquivo fora do diretório `src` pode ser modificado.
* O trabalho pode ser realizado em dupla.
* Todo código fornecido em aula pode ser utilizado no trabalho.
* Em caso de plágio, a nota atribuída ao trabalho será 0 (zero).

## Referências

* [Documentação do PLY](https://ply.readthedocs.io/en/latest/index.html)

