import networkx as nx
import matplotlib.pyplot as plt

# Перше завдання - створення графу та його друк

cities=[['Hadiach', 'Zinkiv', 45], ['Hadiach', 'Lebedyn', 60],
        ['Hadiach', 'Myrhorod', 61], ['Hadiach', 'Lokhvytsia', 81],
        ['Zinkiv', 'Trostianets', 74], ['Trostianets', 'Valky', 102],
        ['Trostianets', 'Bilopillia', 105], ['Zinkiv', 'Lebedyn', 44],
        ['Zinkiv', 'Poltava', 70], ['Lokhvytsia', 'Zavodske', 15],
        ['Zavodske', 'Khorol', 70], ['Khorol', 'Kremenchuk', 80],
        ['Kremenchuk', 'Piatykhatky', 81], ['Trostianets', 'Okhtyrka', 20],
        ['Trostianets', 'Sumy', 51], ['Valky', 'Okhtyrka', 96]]

G=nx.Graph()
G.add_weighted_edges_from(cities)
nx.draw_networkx(G)
plt.show()

# Функція пошуку найкоротшого шляху між містами у графі

def min_len(Gr, cit1, cit2):
        try:
                way=nx.dijkstra_path(Gr, cit1, cit2)
                l=nx.dijkstra_path_length(Gr, cit1, cit2)
                return print(f'Найкоротший маршрут: {way} з протяжністю  {l} км')

        except Exception as ex:
                print(f'Маршрут не знайдено')


min_len(G, 'Lebedyn', 'Sumy')