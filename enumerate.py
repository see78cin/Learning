import copy
dogs = [['tom','bill'],['billy','jack'],['pete','tim']]
cats = copy.copy(dogs)

for i,k in dogs:
    print (i,k)



print (id(dogs))
print (id(cats))
print (id(k))
print (id(i))


