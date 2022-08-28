import random

numberOfStreaks = 0 # keep track of streaks

for trials in range(1):

    tail = 0 # keep track of tail count
    head = 0 # keep track of head count
    outcome = list()
    for i in range(100):
        ht = random.randint(0,1)
        #print(ht)
        if ht == 1:
            outcome.append(ht)
            tail += 1
        else:
            tail = 0 # there is no streak so reset tail count to 0
        if ht == 0:
            outcome.append(ht)
            head += 1
        else:
            head = 0 # there is no streak so reset head count to 0
        if tail == 6:
            numberOfStreaks +=1
        if head == 6:
            numberOfStreaks +=1
print(outcome, len(outcome))
print (numberOfStreaks)


