import random

numberOfStreaks = 0  # keep track of streaks
TnumberOfStreaks = 0
HnumberOfStreaks = 0
temp = list()

for trials in range(2):

    tail = 0  # keep track of tail count
    head = 0  # keep track of head count
    outcome = list() # list of outcomes
    for coinflip in range(100):
        ht = random.randint(0, 1) # tail is 1 , head is 0
        # print(ht)
        if ht == 1:
            outcome.append(ht)  # outcome is tail, so add to list
            tail += 1  # add to tail count
        else:
            tail = 0  # there is no tail, so reset tail count to 0
        if ht == 0:
            outcome.append(ht)  # outcome is head, so add to list
            head += 1  # add to tail count
        else:
            head = 0  # there is no head, so reset head count to 0
        if tail == 6:
            TnumberOfStreaks += 1 # there is 6 tails, so increase streak count
        if head == 6:
            HnumberOfStreaks += 1 # there is 6 head, so increase streak count
    temp.append(outcome)
numberOfStreaks = TnumberOfStreaks+HnumberOfStreaks
print(f'{trials+1} trials of {coinflip+1} coin flips')
#print(outcome, len(outcome))
print(f'Tail streak {TnumberOfStreaks}')
print(f'Head streak {HnumberOfStreaks}')
print(f'Total streak {numberOfStreaks}')
format_numOfStreaks = format(numberOfStreaks/10000,'.5f')
print(f'Chance of streak: {format_numOfStreaks}')
print('List of trials')
print(temp)




