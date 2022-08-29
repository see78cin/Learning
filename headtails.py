import random

numberOfStreaks = 0  # keep track of streaks
HnumberOfStreaks = 0  # keep track of streaks
TnumberOfStreaks = 0  # keep track of streaks
count = 0
temp = list()
trials = int(input('Enter number of trials: '))
coinflips = int(input('Enter number of coin flips per trial: '))
for trial in range(trials):

    tail = 0  # keep track of tail count
    head = 0  # keep track of head count
    outcome = list() # list of outcomes
    temlist = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    for coinflip in range(coinflips):
       # ht = random.randint(0, 1) # tail is 1 , head is 0
        ht = temlist[coinflip]
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
            tail = 0
        if head == 6:
            HnumberOfStreaks += 1 # there is 6 head, so increase streak count
            head = 0
    count += 1
    print(f'Trial # {count}')
    print(f'Head streak {HnumberOfStreaks}')
    print(f'Tail streak {TnumberOfStreaks}')
    temp.append(outcome) # keeps a list of trial.
numberOfStreaks = HnumberOfStreaks+TnumberOfStreaks
print(f'{trials} trials of {coinflips} coin flips')
print(f'Total Head streak {HnumberOfStreaks}')
print(f'Total Tail streak {TnumberOfStreaks}')
print(f'Total streak {numberOfStreaks}')
format_numOfStreaks = format(numberOfStreaks/trials,'.5f')
print(f'Chance of streak from {trials} trials of {coinflips} coin flips: {format_numOfStreaks}')

#print out list of trials
for i, j in enumerate(temp):
    print (i, j)

print(tail)


