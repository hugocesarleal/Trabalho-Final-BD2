# Trabalho Final - Banco de Dados II

Este projeto implementa duas estruturas de dados: Árvore B+ e Hash Linear. Ele foi desenvolvido por Andressa Caroline Lopes de Assis (RA:0072749) e Hugo César Leal (RA:0072753) como parte do trabalho final da disciplina de Banco de Dados II.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `main.py`: Função principal que permite ao usuário escolher entre usar a Árvore B+ ou o Hash Linear.
- `bPlusTree.py`: Implementação da Árvore B+.
- `hashLinear.py`: Implementação do Hash Linear.
- `mainBTree.py`: Funções auxiliares e menu para interagir com a Árvore B+.
- `mainHash.py`: Funções auxiliares e menu para interagir com o Hash Linear.
- `testes/`: Diretório contendo arquivos CSV para testes.

## Como Executar

Para executar o projeto, basta rodar o arquivo `main.py`. Ele exibirá um menu para que você escolha entre usar a Árvore B+ ou o Hash Linear.

```sh
python main.py
```

## Funcionalidades

### Árvore B+

A Árvore B+ é uma estrutura de dados balanceada que permite buscas, inserções e exclusões eficientes. As principais funcionalidades implementadas são:

- Inserção de registros
- Remoção de registros
- Busca por igualdade
- Busca por intervalo
- Exibição da estrutura da árvore

### Hash Linear

O Hash Linear é uma técnica de hashing que utiliza endereçamento linear para lidar com colisões. As principais funcionalidades implementadas são:

- Inserção de registros
- Remoção de registros
- Busca de registros
- Exibição do estado atual da tabela hash

## Menu de Opções

### Árvore B+

Ao escolher a opção de Árvore B+, o seguinte menu será exibido:

- Casos de teste
- Inserir registro
- Remover registro
- Busca por igualdade
- Busca por intervalo
- Mostrar árvore
- Voltar

### Hash Linear

Ao escolher a opção de Hash Linear, o seguinte menu será exibido:  

- Casos de teste
- Inserir registro
- Remover registro
- Fazer busca
- Mostrar hash linear
- Voltar

## Casos de Teste

Os casos de teste são executados a partir de arquivos CSV localizados no diretório `testes`, que foram gerados com o gerador de dados sintéticos disponível em [Siogen](https://ribeiromarcos.github.io/siogen/). Cada linha do arquivo deve começar com `+` para inserção ou `-` para remoção, seguido pelos valores dos registros separados por vírgula.

## Exemplo de Uso

### Inserir Registro na Árvore B+

```sh
Informe o tamanho da página em bytes: 4096
Informe quantos campos tem o registro: 3
Registro completo (campos separados por '-'): 1-2-3
```

### Inserir Registro no Hash Linear

```sh
Informe a quantidade de buckets inicial: 10
Informe o tamanho da página (em bytes): 4096
Quantidade de campos do registro: 3
Registro completo (campos separados por '-'): 1-2-3
```

## Autores

- [Andressa Caroline Lopes de Assis](https://github.com/AndreessaLopes)
- [Hugo César Leal](https://github.com/hugocesarleal/)