nota1 = int(input("Coloque sua primeira nota: "))
nota2 = int(input("Coloque sua segunda nota: "))

media = (nota1 + nota2) / 2.0
print(f"Sua média é {media}")

if media < 6:
    print("Reprovado!")

else:
    print("Aprovado!")
