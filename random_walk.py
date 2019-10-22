import numpy as np
import matplotlib.pyplot as plt 

#todos os walks ficam aqui
all_walks = []


#Simulando um random_walk 1000 vezes

for i in range(1000):
    random_walk = [0]
    for z in range(10):
        step = random_walk[-1] #step vai ser o ultimo random_walk
        dice = np.random.randint(1,7) #Simula um dado com 6 faces
        if dice <= 2:
            step = max(0, step - 1) # Se o dado cair entre 1 e 2, eu volto uma casa, a função max impede que o valor do step seja menor do que zero
        elif dice <= 5:
            step += 1 # Se o dado cair entre 3 e 5 eu ando uma casa
        else:
            step = step + np.random.randint(1,7) # Se cair 6 eu ando um número aleatório de casas, que depende do step passado
        if np.random.rand() <= 0.01: #Adiciona clumsiness aos dados
             step = 0
        random_walk.append(step) #Coloca o step na lista de random_walk

    all_walks.append(random_walk) #Coloca todos os random_walk no all_walks

#Criando o plot do random_walk

np_aw_t = np.transpose(np.array(all_walks))

print(np_aw_t)

plt.plot(np_aw_t)

plt.show()
