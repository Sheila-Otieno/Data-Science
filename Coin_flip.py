
#probability of head when a coin is bias
head=0.25
#probability of tail when a coin is bias
tail=0.75
#probability of a coin being Fair and Tail
pFT=0.4
#probability of a coin being Fair
pF=0.5


#method to calculate the probability of Tail with Fair coin
def calTailFair():
    #pT is the probability of Tail; you take probability of tail of both bias and fair coin and sum them up
    pT=(0.5*0.75)+(0.5*0.5)
    pTF=(pFT*pT)/pF
    return pTF

print(calTailFair())


def flip(side):
    #prior is set to probability of FT which is 0.4
    prior=pFT
    #get the probability of coin being Tail and Fair
    pTF= calTailFair()
    if side == "head":
        u=pTF/(0.5*prior+head*(1-prior))
        return u
    else:
        u=pTF/(0.5*prior+tail*(1-prior))
        return u
print(flip("head"))
print(flip("tail"))

#to get the posterior we use this formula:
#posterior=u*prior
u_head = flip("head")
u_tail = flip("tail")

posterior_head=u_head*(1-pFT)
posterior_tail=u_tail*pFT

print(posterior_head)
print(posterior_tail)
