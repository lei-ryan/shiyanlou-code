for i in range(1,101):
    reminder = i % 7
    if reminder != 0 and str(7) not in str(i):
        print(i)
