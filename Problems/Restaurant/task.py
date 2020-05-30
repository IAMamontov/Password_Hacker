import itertools
#
#
# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
#
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
#
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]


for i in itertools.product(zip(main_courses, price_main_courses),
                                    zip(desserts, price_desserts),
                                        zip(drinks, price_drinks)):
    s = 0
    for j in i:
        s += int(j[1])
    if s <= 30:
        for k in i:
            print(k[0], sep="", end=" ")
        print(s)