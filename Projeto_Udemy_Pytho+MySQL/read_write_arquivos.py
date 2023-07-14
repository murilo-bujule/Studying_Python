# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt", "a+", encoding="utf-8")

arquivo.write("\nEssa é a segunda linha")
arquivo.close()

arquivo = open("arquivo.txt", 'r', encoding="utf-8")
texto = arquivo.read()
print(texto)