import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Consulta um inventário de TI.")
    parser.add_argument("arquivo", type=Path, help="Caminho do CSV")
    parser.add_argument("--status", help="Filtra pelo status do equipamento")
    args = parser.parse_args()

    try:
        with args.arquivo.open(encoding="utf-8-sig", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            colunas = ("patrimonio", "equipamento", "setor", "status")
            if not set(colunas).issubset(leitor.fieldnames or []):
                parser.error("O CSV deve conter: " + ", ".join(colunas))
            total = 0
            for numero, registro in enumerate(leitor, start=2):
                if any(not (registro[coluna] or "").strip() for coluna in colunas):
                    parser.error(f"Campo faltando na linha {numero}.")
                if args.status and registro["status"].strip().casefold() != args.status.strip().casefold():
                    continue
                print(" | ".join(registro[coluna].strip() for coluna in colunas))
                total += 1
    except (OSError, UnicodeError, csv.Error) as erro:
        parser.error(f"Não foi possível ler o CSV: {erro}")
    print(f"Equipamentos encontrados: {total}")


if __name__ == "__main__":
    main()
