def inverter_string(string_original):
  """
  Inverte os caracteres de uma string.

  Args:
    string_original: A string a ser invertida.

  Returns:
    A string invertida.
  """

  string_invertida = ""
  for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]
  return string_invertida

# Exemplo de uso:
string_original = "Exemplo de string"
string_invertida = inverter_string(string_original)
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")