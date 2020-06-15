import numpy as np
import matplotlib.pyplot as plt

# Reads csv file 'coin-flips.py'
data = np.genfromtxt('coin-flips.csv', delimiter=',', filling_values=np.nan, dtype=str)

# Probability of picking a fair or biased coin
f = b = 0.5

# Probability of coin toss resulting in head/tail for fair/biased
tf = 0.5
hf = 0.5
hb = 0.25
tb = 0.75
prob_fair_data = []


# Prior Assumptions
# pbh = 1
# pbt = 0


# Find the posterior probability using Bayes's Theorem
def posterior_cal(xf, xb, f, b, li):
    e = evidence(xf, xb, f, b)
    prior = b
    prob_data = (li * prior) / e
    return prob_data


# Find likelihood of coin being fair for head & tail
# If head then likelihood of bias is 0.25
# If tail then likelihood of bias is 0.75

# Find evidence for the posterior i,e denominator
def evidence(xf, xb, f, b):
    evi = (xf * f) + (xb * b)
    return evi


# Loop for each coin flip for 12 experiments
def count(fhead, ftail, bhead, btail, fair, bias):
    for rows in range(len(data)):
        eloop = data[rows]
        for row in range(len(eloop)):
            if eloop[row] == 'H':
                likelihood = 0.25
                res = posterior_cal(bhead, fhead, fair, bias, likelihood)
                bias = res
                fair = 1 - bias
                prob_fair_data.append(fair)
            else:
                likelihood = 0.75
                res = posterior_cal(btail, ftail, fair, bias, likelihood)
                bias = res
                fair = 1 - bias
                prob_fair_data.append(fair)

    return prob_fair_data


counts = count(hf, tf, hb, tb, f, b)
print(counts)
rcounts = np.reshape(counts, (12, 20))


def plot(graph):
    for row in range(len(graph)):
        y = graph[row, :]
        x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        plt.plot(x, y)
        plt.show()


plot(rcounts)
