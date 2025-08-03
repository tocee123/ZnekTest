a, b = 1, 10
listam = [(a<b, "a kisebb mint b"), (a>b, "a nagyobb, mint"), (a == b), "egyenlo"]
for x in listam:
    if(x[0]):
        print(x[1])