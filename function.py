import pandas as pd


def Search(x):
    global list_search
    list_search = []

    c = input()

    for i in x:
        if c in i.lower():
            list_search.append(i)

    if len(list_search) == 0:
        print("Name was not found!")
