def print_results_table(data, teams_list):
    str_l = max(len(t) for t in teams_list)
    print(" ".join(['{:>{length}s}'.format(t, length = str_l) for t in [" "] + teams_list]))
    for t, row in zip(teams_list, data):
        print(" ".join(['{:>{length}s}'.format(str(x), length = str_l) for x in [t] + row]))

teams_list = ["Id Projeto", "Nome", "Data inicio", "Data Final",   "Porcentagem"]
data = [[1, 2, 1],
        [0, 1, 0],
        [2, 4, 2]]

print_results_table(data, teams_list)

def print_results_table(data, teams_list):
    str_l = max(len(t) for t in teams_list)
    print(" ".join(['{:>{length}s}'.format(t, length = str_l) for t in [" "] + teams_list]))
    for t, row in zip(teams_list, data):
        print(" ".join(['{:>{length}s}'.format(str(x), length = str_l) for x in [t] + row]))

teams_list = ["Id Projeto", "Nome", "Data inicio", "Data Final",   "Porcentagem"]
data = [[1, 2, 1],
        [0, 1, 0],
        [2, 4, 2]]

print_results_table(data, teams_list)