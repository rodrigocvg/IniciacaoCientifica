import copy


produtos = [

    ["Ipad", 5000],

    ['Iphone', 4500],

]

produtos_2 = produtos.copy()

produtos_2[0][1] = 6000

print(produtos_2)

print(produtos)

produtos_3 = copy.deepcopy(produtos)

produtos_3.append(['Icaralho',2222])

print("P3",produtos_3)

produtos4 = produtos

produtos4.append(['Icaralho',2222])

print(produtos)