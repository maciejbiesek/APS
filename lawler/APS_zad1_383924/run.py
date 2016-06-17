import task as tsk
import sys

tasks = []

def print_diag(S):
    diag_str1 = "|"
    diag_str2 = "0"
    diag_str3 = " "
    count = 0
    for elem in S:
        count += elem.time
        diag_str1 += elem.time * "-"
        diag_str2 += elem.time * " " + str(count)
        diag_str3 += str(elem.index) + (elem.time - 1) * " "
        diag_str1 += "|"
        diag_str3 += " "
        
    return diag_str3 + "\n" + diag_str1 + "\n" + diag_str2
    
def prepare_data(file_path):
    tim = []
    func = []
    depend = []

    f = open(file_path, "r")

    count = 0
    for line in f:
        if count == 0:
            tim = line.split()
        elif count == 1:
            tmp_split = line.split()
            for elem in tmp_split:
                tmp_elem = ""
                for char in elem:
                    if char != "[" and char != "]":
                        tmp_elem += char
                tmp_lst = [float(x) for x in tmp_elem.split(",")]
                func.append(tmp_lst)
        else:
            depend = line.split()
        count += 1
        
    for i in range(len(tim)):
        task = tsk.Task(i+1, int(tim[i]), func[i])
        tasks.append(task)
        
    for dep in depend:
        x, y = dep.split("->")
        x = int(x)
        y = int(y)
        tasks[x-1].set_succ(y)
   
def write_to_file(S, maxm):
    line = [x.index for x in S]
    f = open("output", "w")
    f.write("Uszeregowanie:\n")
    f.write(str(line))
    f.write("\n\n")
    f.write("Diagram:\n")
    f.write(print_diag(S))
    f.write("\n\n")
    f.write("Wartosc kryterium optymalizacji: ")
    f.write(str(maxm))
    
    f.close()
   
def lawler():
    S = []
    crit = []
    while (tasks):
        t = sum(x.time for x in tasks)                                          # suma czasow wykonania zadan
        not_succ = [task for task in tasks if not(task.successors)]             # podzbior nieposiadajacy nastepnikow
        local_crit = [(task, task.get_value(t)) for task in not_succ]
        task_delete, best_crit = sorted(local_crit, key=lambda x: x[1])[0]      # wybierz takie zadanie, ze funkcja kosztu jest najmniejsza
        crit.append(best_crit)
        S.append(task_delete)                                                   # dopisz zadanie do wyjsciowego uszeregowania
        tasks.remove(task_delete)                                               # usun dopasowane zadanie z listy
        for task in tasks:                                                      # dla kazdego zadania usun dopasowane zadanie z listy nastepnikow
            task.rem_succ(task_delete.index)

    S.reverse()
    write_to_file(S, max(crit))


file_path = sys.argv[1]
prepare_data(file_path)
lawler()

