import random

#criar lista com 20 elementos entre -10 e 10
original = [random.randint(-10, 10) for _ in range (20)]
editada = original.copy()

#encontrar o intervalo com a maior quantidade de negativos
max_seq = []
atual_seq = []
inicio_max = 0
inicio_atual = 0

for i, num in enumerate (editada):
    if num < 0:
        if not atual_seq: inicio_atual = i
        atual_seq.append(num)
    else:
        if len (atual_seq) > len(max_seq):
            max_seq = atual_seq.copy()
            inicio_max = inicio_atual
            atual_seq = []

            #checagem final caso a maior sequência esteja no fim da lista
            if len (atual_seq)> len (max_seq):
                max_sq = atual_seq
                inicio_max = inicio_atual

                #deletar o intervalo encontrado
                if max_seq:
                    del editada [inicio_max : inicio_max + len (max_seq)]

                    print (f"original:{original}")
                    print (f"editada: {editada}")