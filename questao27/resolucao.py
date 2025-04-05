
## Função que remove todas as ocorrências do valor 'val' no array 'nums'

def remove_elemento(nums, val):
    k = 0  # posição para onde vamos mover os valores válidos

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

# Exemplo de uso da função remove_elemento
nums = [3, 2, 2, 3]
val = 3
k = remove_elemento(nums, val)

print("Resultado k:", k) # função print para Imprimir quantos elementos diferentes de 'val' foram encontrados
print("Array modificado:", nums[:k]) # função print para imprimir os 'k' primeiros elementos do array modificado 