compiladores-2024-t1
====================

Preparação para a execução do trabalho
--------------------------------------

Para iniciar este trabalho, faça um _fork_ do repositório 
[https://github.com/exercicios-programacao/compiladores-2024-t1](https://github.com/exercicio-programacao/compiladores-2024-t1)
para o seu usuário do Github.

Siga as orientações para a preparação do ambiente de desenvolvimento 
contidas nesse documento.

Todo o código implementado deve estar dentro do diretório `src`. Siga as 
instruções contidas no arquivo [`INSTRUCOES.md`](INSTRUCOES.md), que contém
os objetivos e etapas para a realização do trabalho.


Instalação das Dependências
---------------------------

Para realizar este trabalho você deverá utilizar a linguagem de programação 
Python, na versão 3.11 ou superior.

Para isolar o ambiente de desenvolvimento, é sugerido o uso de ambientes 
virtuais do Pyhton

```
$ python -m venv .venv
```

Em cada seção de desenvolvimento você deve iniciar e atualizar o ambiente
de desnevolvimento:

```
$ . .venv/bin/activate
$ pip install -e .
```

Se você quiser utilizar o `tox` para executar os testes, você deve instalar
o ambiente com a opção `tox`:

```
$ pip install -e .[tox]
```


Desenvolvimento
---------------

Durante o desenvolvimento do trabalho, você pode executar os testes, 
localmente, utilizando os comandos `tox` ou `behave`. A diferença entre os 
dois é que o `behave` executa apenas os testes funcionais e o `tox` executa 
os testes de qualidade de código, como formatação e boas práticas.

É sugerido que se trabalhe em um cenário de cada vez, o que pode ser obtido 
utilizando-se o comando `behave --stop`, para que os testes funcionais 
parem na primeira falha.

Além dos testes de _features_ do `behave` o comando `tox` executa testes de
qualidade de código através do `pylint`, `flake8` e `pydocstyle`.


Entrega
-------

Para entregar o trabalho, faça commit do código, envie para o seu _fork_ no 
Github, e abra um _pull request_ contra o
[repositório original](https://github.com/exercicios-programacao/compiladores-2024-t1).

O título do _pull request_ deve conter o nome do aluno que o está criando. 
Na mensagem deve constar o nome completo do autor do _pull request_, e de 
todos os alunos que realizaram o trabalho, no caso de trabalhos em grupo. 
Qualquer informação necessária para a entrega do trabalho deve estar 
presente no corpo dessa mensagem.

Você deve garantir que os testes (`checks`) executaram corretamente, pois é 
a partir deles que será realizada a avaliação.


Discussões Online
-----------------

Dúvidas e disccussões sobre o trabalho podem ser realizadas utilizando as
[discussões do Github](https://github.com/exercicios-programacao/compiladores-2024-t1/discussions).
