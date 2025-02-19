# Imports
import random
from collections import deque

# Funcao GERAR MAPA (7x7)
def gerar_mapa(tam=7):

    # Bordas do mapa sao paredes (#) 
    while True:
        grade = [['#' if i == 0 or i == tam-1 or j == 0 or j == tam-1 else '.' for j in range(tam)] for i in range(tam)]
        
        # Adiciona paredes aleatórias no interior da grade
        for _ in range(tam):
            x, y = random.randint(1, tam-2), random.randint(1, tam-2)
            grade[x][y] = '#'
        
        # Posicao inicial do jogador (S)
        inicio_x, inicio_y = random.randint(1, tam-2), random.randint(1, tam-2)
        while grade[inicio_x][inicio_y] == '#':
            inicio_x, inicio_y = random.randint(1, tam-2), random.randint(1, tam-2)
        grade[inicio_x][inicio_y] = 'S'
        
        # Posicao do tesouro (T)
        tesouro_x, tesouro_y = random.randint(1, tam-2), random.randint(1, tam-2)
        while grade[tesouro_x][tesouro_y] in ('#', 'S'):
            tesouro_x, tesouro_y = random.randint(1, tam-2), random.randint(1, tam-2)
        grade[tesouro_x][tesouro_y] = 'T'
        
        # Verifica se ha caminho entre o jogador (S) e o tesouro (T) -> Verifica se o mapa e valido
        if buscaV2(grade, (inicio_x, inicio_y), (tesouro_x, tesouro_y)):
            return grade, (inicio_x, inicio_y), (tesouro_x, tesouro_y)

# Funcao EXIBIR MAPA
def exibir_mapa(grade):
    for row in grade:
        print(" ".join(row))
    print()

# def busca(grade, inicio, tesouro):

#     tam = len(grade)
#     fila = deque([(inicio, [inicio])])
#     explorados = set()
#     explorados.add(inicio)
    
#     # Movimentos possiveis p o jogador
#     #  DIREITA - BAIXO - ESQUERDA - CIMA
#     movimentos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
#     while fila:
#         (x, y), caminho = fila.popleft()
        
#         # Caminho encontrado
#         if (x, y) == tesouro:
#             return caminho
        
#         for dx, dy in movimentos:
#             nx, ny = x + dx, y + dy
            
#             # Verificar se o movimento e valido
#             # Dentro do limite & nao e parede & ainda nao foi explorado
#             if 0 <= nx < tam and 0 <= ny < tam and grade[nx][ny] != '#' and (nx, ny) not in explorados:
#                 fila.append(((nx, ny), caminho + [(nx, ny)]))
#                 explorados.add((nx, ny))
    
#     # Nenhum caminho encontrado (impossivel?)
#     return None

def buscaV2(grade, inicio, tesouro):
    tam = len(grade)
     #  DIREITA - BAIXO - ESQUERDA - CIMA
    movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pilha = [(inicio, [inicio])]
    explorados = set()
    explorados.add(inicio)
    possiveis_caminhos = []
    
    while pilha:
        #ponto atual, caminho
        (x, y), caminho = pilha.pop()
        
        if (x, y) == tesouro:
            return caminho
        
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < tam and 0 <= ny < tam and grade[nx][ny] != '#' and (nx, ny) not in explorados:
                pilha.append(((nx, ny), caminho + [(nx, ny)]))
                #print(pilha)
                explorados.add((nx, ny))
                break
        else:
            # Sem saída, voltar para última bifurcação
            while possiveis_caminhos:
                (bx, by), caminho_anterior = possiveis_caminhos.pop()
                pilha.append(((bx, by), caminho_anterior))
                break
    
    return None

def main():
    print("\n=====================================")
    print("           Bem-vindo ao")
    print("         CACA TESOUROS 3000\n")

    
    while True:
        jogar = input("Você deseja jogar? (sim/não): ").strip().lower()
        if jogar != "sim" and jogar != "s":
            print("\n TCHAU :( \n")
            break
        
        # Geracao do mapa
        grade, inicio, tesouro = gerar_mapa()
        print("\n=====================================")
        # Exibicao do mapa
        print("\nMAPA\n")
        exibir_mapa(grade)
        
        # Procura um caminho!!
        #caminho = busca(grade, inicio, tesouro)
        caminho = buscaV2(grade, inicio, tesouro)


        
        if caminho:
            print("Caminho encontrado:")
            for passo in caminho:
                print(passo)

            # Contagem do numero de movimentos necessarios para o jogador chegar ao tesouro
            print(f"Número de movimentos necessários: {len(caminho) - 1}")


            # Exibe o caminho no mapa com asteriscos (*)
            for x, y in caminho[1:-1]:  # Não marca S e T
                grade[x][y] = '*'
            print("\nMapa com caminho:")
            exibir_mapa(grade)
        else:
            print("Nenhum caminho encontrado!")

if __name__ == "__main__":
    main()
