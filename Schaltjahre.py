def leap_year(y):
    years = []
    for i in range(y):
        if i % 4 == 0:
            years.append(i)
        elif i % 100 == 0 and i % 400 == 0:
            years.append(i)
    print(years)


leap_year(3000)
