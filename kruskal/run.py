import set as st
import sys
    
vertices = []
edges = []
sets = dict()


# praca na plikach:
def prepare_data(file_path):
    f = open(file_path, "r")

    count = 0
    for line in f:
        if count == 0:
            vertices.extend(line.split())
        else:
            v1, v2, weight = line.split()
            edges.append([v1, v2, float(weight)])
        
        count += 1
   
def write_to_file(A, total):
    f = open("output", "w")
    f.write("Lista krawedzi:\n")
    for edge in A:
        f.write(str(edge) + "\n")
    f.write("\n")
    f.write("Waga: ")
    f.write(str(total))
    
    f.close()


# lasy zbiorow rozlacznych
def make_set(x): # x jest wartoscia
    x_set = st.Set(x)
    x_set.rank = 0
    x_set.p = x_set
    sets[x] = x_set
    
def find_set(x): # x jest obiektem!
    if x != x.p:
        x.p = find_set(x.p)
    return x.p

def union(x, y): # x i y sa obiektami!
    link(find_set(x), find_set(y))
    
def link(x, y): # x i y sa korzeniami
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1 


# wlasciwy algorytm Kruskala    
def kruskal():
    A = []
    total_w = 0.0
    for vertice in vertices:                        # dla kazdego wierzcholka wywolaj make-set
        make_set(vertice)
    edges.sort(key = lambda x : x[2])               # posortuj krawedzie niemalajco wzgledem wag
    for edge in edges:                              # dla kazdej krawedzi w kolejnosci niemalejacych wag
        v1, v2, weight = edge                       # poczatek, koniec i waga krawedzi
        v1_set = sets[v1]                           # znajdz sety odpowiadajace tym wierzcholkom
        v2_set = sets[v2]
        if (find_set(v1_set) != find_set(v2_set)):  # jesli v1 i v2 sa w roznych drzewach
            A.append(edge)                          # dodaj krawedz (v1, v2) do drzewa rozpietego
            total_w += weight                       # licz wage calego MST
            union(v1_set, v2_set)                   # polacz drzewa
    
    write_to_file(A, total_w)


# wywolanie
file_path = sys.argv[1]
prepare_data(file_path)
kruskal()