def missing_number(liste):
    my_liste = []
    for i in range(len(liste) - 1):
        if liste[i] + 1 != liste[i + 1]:
            my_liste.append(liste[i + 1] - 1)
    return my_liste


print(missing_number([1, 2, 4, 6]))
