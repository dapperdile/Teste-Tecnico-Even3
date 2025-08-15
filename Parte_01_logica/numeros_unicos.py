from typing import List

def numeros_unicos(lista: List[int]) -> List[int]:
    # Recebe lista com números repetidos e retorna lista com os números que não se repetem
    
    lista_unica = []
    for numero in lista:
        if numero not in lista_unica:
            # Adiciona numero se ele já não estiver na lista_unica
            lista_unica.append(numero)
        else:
            # Se já estiver, remove o numero
            lista_unica.remove(numero)
    
    return lista_unica


if __name__ == "__main__":
    lista_exemplo = [1, 2, 2, 3, 4, 4, 5]
    resultado = numeros_unicos(lista_exemplo)
    print(f"Números únicos na lista {lista_exemplo}: {resultado}")
