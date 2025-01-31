import csv
with open('fix/produtos.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([
        'produto', 'ncm', 'importado', 'preco', 'estoque', 'estoque_minimo'
    ])
    # escrever mais de uma linha com o writerows (plural)
    rows = [
        ['Apontador', 14669768, True, 15.54, 125, 30],
        ['Caderno 100 folhas', 44716505, True, 6.52, 120, 10],
        ['Caderno capa dura 200 folhas', 61556783, False, 24.46, 92, 20],
        ['Caneta esferográfica azul', 80951350, False, 11.42, 138, 20],
        ['Caneta esferográfica preta', 19009230, True, 3.71, 148, 40],
        ['Caneta esferográfica vermelha', 62358012, False, 13.74, 186, 50],
        ['Durex', 52181421, False, 7.43, 11, 20],
        ['Giz de cera 12 cores', 54194976, True, 23.66, 46, 10],
        ['Lapiseira 0.3 mm', 14122061, False, 10.76, 141, 40],
        ['Lapiseira 0.5 mm', 44284736, True, 0.71, 199, 40],
        ['Lapiseira 0.7 mm', 40347035, False, 11.28, 192, 50],
        ['Lápis de cor 24 cores', 73784057, False, 13.80, 103, 10],
        ['Lápis', 67410825, True, 3.27, 154, 20],
        ['Papel sulfite A4 pacote 100 folhas', 31000281, False, 18.26, 197, 20],
        ['Pasta elástica', 85605700, True, 7.10, 48, 40],
        ['Tesoura', 13750972, False, 9.68, 77, 10],
    ]
    csv_writer.writerows(rows)