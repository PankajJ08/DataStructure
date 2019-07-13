x = 1

def tower_of_hanoi_sol(h, initial, end, aux):
    global x
    if h >= 1:
        tower_of_hanoi_sol(h - 1, initial, aux, end)
        print(x, ": ", "Move from ", initial, " to ", end)
        x += 1
        tower_of_hanoi_sol(h - 1, aux, end, initial)


tower_of_hanoi_sol(3, 1, 2, 3)
