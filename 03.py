nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aprovado! Média: {media:.2f}")
elif 5 <= media < 7:
    print(f"Recuperação! Média: {media:.2f}")
else:
    print(f"Reprovado! Média: {media:.2f}")
