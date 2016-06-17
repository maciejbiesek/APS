import sys
    
men = {}
women = {}
marriage = {}

# praca na plikach:
def prepare_data(file_path):
    f = open(file_path, "r")

    for line in f:
        char, pref = line.split()
        lst = [x for x in pref]
        if (char.islower()):
            women[char] = lst
        else:
            men[char] = lst
        
def write_to_file():
    f = open("output", "w")
    f.write("Lista skojarzonych par:\n")
    for x in sorted(marriage):
        f.write(str(x) + str(marriage[x]) + " ")
    
    f.close()


# stable marriage problem
def is_intrested(x, X):
    prefs = women[x]
    fiance = marriage[x]
    if (fiance == "omega"):
        return True, fiance                             # kazdy jest lepszy od omegi
    else:
        return prefs.index(X) < prefs.index(fiance), fiance

def smp():
    for key, prefs in women.iteritems():
        marriage[key] = "omega"                         # wszystkie kobiety zareczone z wdowcem
    
    for X in men:                                       # dopoki nie skoncza sie mezczyzni
        while (X != "omega"):                           # dopoki mezczyzna X nie jest tym, ktorego nie chce zadna kobieta
            x = men[X][0]                               # pobierz kobete, ktora jest utopijnym marzeniem X
            intrested, fiance = is_intrested(x, X)
            if (intrested):                             # ale czy ta kobieta chce rzucic swojego obecnego narzeczonego i zwiazac sie z X?
                marriage[x] = X                         # jesli tak, to polacz w pare x i X
                X = fiance                              # i znajdz zone porzuconemu, zeby nie byl samotny
            if (X != "omega"):
                men[X].remove(x)                        # mezczyzna nienawidzi kobiety, ktora porzucila go dla innego
            
    write_to_file()


# wywolanie
file_path = sys.argv[1]
prepare_data(file_path)
smp()