import numpy as np
import matplotlib.pyplot as plt

# Reads csv file 'coin-flips.csv'
coin_flips = np.genfromtxt('coin-flips.csv', delimiter=',',filling_values=np.nan, dtype=str)

#probability of coin being fair
f=0.5
#probability of coin being bias
b=0.5
#probability of coin being head or tail if fair coin
tf = 0.5
hf = 0.5
#probability of coin being head or tail if bias coin
hb = 0.25
tb = 0.75
probability = []

#calculating posterior
def calc_posterior(pF, pB, f, b, li):
    cp = calc_prior(pF, pB, f, b)
    prior = b
    posterior = (li * prior) / cp
    return posterior



#calculating the prior
def calc_prior(pf, pb, fair, bias):
    pTF = (pf * fair) + (pb * bias)
    return pTF


#calculating the probability of each coin flip
def flip_coin(f_head, f_tail, b_head, b_tail, f, b):
    for i in range(len(coin_flips)):
        flips=coin_flips[i]
        for j in range(len(flips)):
            if flips[j] == 'H':
                possibility = 0.25
                u_head = calc_posterior(b_head,f_head,f,b,possibility)
                bias = u_head
                pos = 1 - bias
                probability.append(pos)
            else:
                possibility = 0.75
                u_head = calc_posterior(b_tail,f_tail,f,b,possibility)
                bias = u_head
                pos = 1 - bias
                probability.append(pos)
    return probability


print(flip_coin(hf, tf, hb, tb, f, b))
