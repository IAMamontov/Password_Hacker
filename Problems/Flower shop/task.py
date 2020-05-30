import itertools
# flower_names = ['rose', 'tulip', 'sunflower']
for i in range(1, 4):
    for j in itertools.combinations(flower_names, i):
        print(j)