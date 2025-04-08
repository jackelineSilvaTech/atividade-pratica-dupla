
def remove_elemento(nums, val):
    """
    Remove todas as ocorrências de um valor específico da lista.

    Parâmetros:
    nums (list) : Lista de números inteiros.
    val (int): Valor que deve ser removido da lista.

    Retorno:
    int: A quantidade de elementos que restaram na lista após a remoção (diferentes de 'val').

    Observações:
    - A função não cria uma nova lista; ela reorganiza a lista original.
    - Os 'k' primeiros elementos da lista resultante (nums[:k]) conterão os valores válidos.
   
    Exemplo:
    nums = [3, 2, 2, 3]
    val = 3
    k = remove_elemento(nums, val)
    Resultado: k = 2, nums[:k] = [2, 2]
    """
    k = 0  # posição para onde vamos mover os valores válidos

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

# Exemplo de uso
nums = [3, 2, 2, 3]
val = 3
k = remove_elemento(nums, val)

print("Resultado k:", k)            # Imprime quantos elementos diferentes de 'val' foram encontrados
print("Array modificado:", nums[:k])  # Imprime os 'k' primeiros elementos do array modificado