import re

# Especifique uma expressão regular que faça match com qualquer string binária desde que esta não contenha a substring "011".

expressao = r"^(?!.*011)[01]*$"


# Testes
 
def testar():
    pattern = re.compile(expressao)
    
    # Casos que devem fazer match
    casos = ["010101", "111111", "000000", "0101101", "011", "1100110"]
    
    for caso in casos:
        resultado = bool(pattern.match(caso))
        print(f"'{caso}': {resultado}")
    

testar()
