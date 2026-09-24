def calcular_media(valores):
  if not valores:
    return 0
  return sum(valores) / len(valores)


# Exemplo de uso:
notas = [7.5, 8.0, 9.2, 6.5, 10.0]
media = calcular_media(notas)

print(f"Os valores são: {notas}")
print(f"A média calculada é: {media:.2f}")
