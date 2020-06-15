experiments = [["H", "H", "T", "T", "H", "T", "T", "H", "H", "T", "T", "T", "T", "T", "H", "T", "T","T", "T", "H"],
              ["T", "T", "H", "T", "T", "T", "H", "T", "T", "T", "H", "T", "T", "T", "H", "T", "T", "T", "H", "H"],
              ["T", "H", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "H"],
              ["T", "H", "H", "T", "H", "H", "T", "H", "T", "T", "T", "T", "T", "H", "T", "H", "H", "H", "T", "T"],
              ["T", "H", "H", "H", "T", "H", "T", "T", "T", "T", "T", "T", "T", "H", "T", "T", "T", "T", "T", "T"],
              ["H", "H", "T", "H", "T", "H", "T", "T", "T", "T", "H", "H", "H", "H", "T", "T", "T", "T", "T", "H"],
              ["H", "T", "H", "T", "H", "H", "H", "T", "H", "H", "H", "H", "H", "T", "T", "H", "H", "T", "T", "T"],
              ["T", "T", "T", "T", "T", "H", "T", "T", "T", "T", "T", "T", "T", "T", "H", "T", "H", "T", "T", "T"],
              ["T", "T", "T", "H", "H", "T", "T", "H", "T", "T", "H", "T", "H", "T", "T", "T", "T", "H", "T", "T"],
              ["H", "H", "H", "H", "T", "T", "T", "T", "T", "T", "T", "T", "T", "H", "T", "T", "T", "H", "H", "H"],
              ["T", "T", "T", "H", "T", "T", "T", "H", "H", "H", "H", "H", "H", "H", "H", "H", "T", "T", "T", "T"],
              ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H"]]

#probability of head when a coin is bias
H = 0.25
#probability of tail when a coin is bias
T = 0.75
#probability of a coin being Fair and Tail
pFT = 0.4
#probability of a coin being Fair
pF = 0.5


#method to calculate the probability of Tail with Fair coin
def calTailFair():
    #pT is the probability of Tail; you take probability of tail of both bias and fair coin and sum them up
    pT = (0.5*0.75)+(0.5*0.5)
    pTF = (pFT*pT)/pF
    return pTF

def flip(side):
    #prior is set to probability of FT which is 0.4
    prior = pFT
    #get the probability of coin being Tail and Fair
    pTF = calTailFair()
    if side == "H":
        u = pTF/(0.5*prior+H*(1-prior))
        return u
    else:
        u = pTF/(0.5*prior+T*(1-prior))
        return u


#to get the posterior we use this formula:
#posterior=u*prior
u_head = flip("H")
u_tail = flip("T")

#posterior = 0
probability=[]
#for i in range(len(experiments)):
    #for j in range(len(i)):
        #if j=="H":
            #u_head=flip("H")
            #posterior = u_head*(1-pFT)
            #probability.append(posterior)
            
        #else:
            #u_tail = flip("T")
            #posterior = u_tail*pFT
            #probability.append(posterior)

print(probability)


def calc_probability():
    for row in range(len(experiments)):
         coin=experiments[row]
         print(coin)
         for i in range(len(coin)):
             print(i)
             if coin[i] == 'H':
                u_head=flip('H')
                posterior = u_head*(1-pFT)
                probability.append(posterior) 
             else:
                u_tail = flip('T')
                posterior = u_tail*pFT
                probability.append(posterior)  
    return probability

print(calc_probability())      
