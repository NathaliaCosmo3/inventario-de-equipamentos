# Inventário de equipamentos de TI

## Baixar e abrir no navegador

**[Baixar projeto em ZIP](https://github.com/NathaliaCosmo3/inventario-de-equipamentos/archive/refs/heads/main.zip)**

1. Extraia o ZIP. No Windows, clique com o botão direito no arquivo e escolha **Extrair Tudo**.
2. Na pasta extraída, abra `index.html` com duplo clique. A interface funciona offline e dispensa instalação.

A interface inclui três equipamentos fictícios para demonstração. Cadastre ou edite itens, filtre por status e baixe a lista exibida em CSV. Os registros do painel ficam no navegador e o programa Python consulta o CSV informado no terminal.

## Versão em Python para terminal


Consulta um inventário em CSV e filtra equipamentos por status. O resultado mostra patrimônio, equipamento, setor e o total de registros encontrados.

## Como executar

Com Python 3, rode estes comandos na pasta do projeto:

```shell
python inventario.py exemplo.csv
python inventario.py exemplo.csv --status "Manutenção"
```

O segundo comando retorna apenas a impressora do exemplo. O arquivo `exemplo.csv` contém dados fictícios.

Projeto de portfólio desenvolvido com assistência de IA.
