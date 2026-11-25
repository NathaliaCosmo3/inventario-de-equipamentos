# Inventário de equipamentos de TI

## Abrir a versão visual

1. Abra o [arquivo index.html](https://github.com/NathaliaCosmo3/inventario-de-equipamentos/blob/main/index.html).
2. Na barra acima do código, clique no ícone de download (**Download raw file**).
3. Na pasta **Downloads**, abra `index.html` com dois cliques. Ele funciona offline no Chrome ou Edge, sem instalar Python.

**[Baixar todos os arquivos em ZIP](https://github.com/NathaliaCosmo3/inventario-de-equipamentos/archive/refs/heads/main.zip)**

Cadastre e edite equipamentos, confira os indicadores de uso e manutenção e exporte a lista filtrada em CSV. Inclui dados fictícios para demonstração. Os registros ficam no navegador usado.

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
