import numpy as np
import matplotlib.pyplot as plt

# Read csv file 'coin-flips.csv'
coin_flips = np.genfromtxt('coin-flips.csv', delimiter=',', filling_values=np.nan, dtype=str)

#probability of coin being fair
f = 0.5
#probability of coin being bias
b = 0.5
#probability of coin being head or tail if fair coin
tf = 0.5
hf = 0.5
#probability of coin being head or tail if bias coin
hb = 0.25
tb = 0.75
probability = []


# calculating posterior
def cal_posterior(xf, xb, f, b, pos):
    cp = cal_prior(xf, xb, f, b)
    prior = b
    posterior = (pos * prior) / cp
    return posterior


# calculating the prior
def cal_prior(pf, pb, f, b):
    pTf = (pf * f) + (pb * b)
    return pTf


# Calculate the probability of a coin being fair from the twelve experiments
def flip_coin(f_head, f_tail, b_head, b_tail, fair, bias):
    for i in range(len(coin_flips)):
        sides = coin_flips[i]
        for j in range(len(sides)):
            if sides[j] == 'H':
                possibility = 0.25
                u_head = cal_posterior(b_head, f_head, fair, bias, possibility)
                bias = u_head
                pos = 1 - bias
                probability.append(pos)
            else:
                possibility = 0.75
                u_tail = cal_posterior(b_tail, f_tail, fair, bias, possibility)
                bias = u_tail
                pos = 1 - bias
                probability.append(pos)

    return probability


flips = flip_coin(hf, tf, hb, tb, f, b)
print(flips)
#plt.plot(flips)
#plt.show()
flips_reshape = np.reshape(flips, (12, 20))

#plot the graph   
for i in range(len(flips_reshape)):
    y = flips_reshape[i, :]    
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13, 14, 15, 16, 17, 18, 19, 20)
    plt.plot(x, y)
    plt.show()



