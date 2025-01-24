# Projeto Integrado de Estruturas de Dados

Este projeto implementa duas estruturas de dados: uma árvore B+ e uma tabela hash linear. O usuário pode escolher entre usar uma dessas estruturas para realizar operações de inserção, remoção e busca de registros.

## Estrutura do Projeto

```
projeto-integrado
├── src
│   ├── main.py            # Ponto de entrada da aplicação
│   ├── mainBTree.py       # Implementação da árvore B+
│   ├── mainHash.py        # Implementação da tabela hash linear
│   ├── bPlusTree.py       # Classe que define a árvore B+
│   ├── hashLinear.py      # Classe que define a tabela hash linear
│   └── testes
│       └── teste1.csv     # Arquivo de teste em formato CSV
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## Como Executar

1. **Clone o repositório:**
   ```
   git clone <URL do repositório>
   cd projeto-integrado
   ```

2. **Instale as dependências:**
   Se houver dependências listadas no `requirements.txt`, instale-as usando:
   ```
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   Para iniciar a aplicação, execute o arquivo `main.py`:
   ```
   python src/main.py
   ```

## Funcionalidades

- **Árvore B+:**
  - Inserir registros
  - Remover registros
  - Buscar registros por chave
  - Buscar registros em intervalos
  - Mostrar a estrutura da árvore

- **Tabela Hash Linear:**
  - Inserir registros
  - Remover registros
  - Buscar registros por chave
  - Mostrar a tabela hash

## Testes

O arquivo `testes/teste1.csv` contém dados de teste que podem ser utilizados para verificar o funcionamento das estruturas de dados.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, crie um fork do repositório e envie um pull request com suas alterações.