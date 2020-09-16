#preferred, what we want to happen, flipping a coin heads, 1
#possible outcomes, what can happen, heads or tails, 2
def probability(preferred,possible):
    return(preferred/possible)
    
probability(1,2)

#probability of getting an ace of spades, is prob ace, and prob spade
def prb_a_and_b(prf_a,pos_a,prf_b,pos_b):
    prob_a = probability(prf_a,pos_a)
    prob_b = probability(prf_b,pos_b)
    return(prob_a*prob_b)
    
prb_a_and_b(1,13,1,4)

#experimental probabilities

def exp_probability(successful,total):
    return(successful/total)

exp_probability(8,10)

#probability of an event (drawing a spade) 
#after drawing a card 20 times (20 trials)
#theoretical probability E(A) = P(A)xn

def exp_probability_2(prf_a,pos_a,trials):
    prob_a = probability(prf_a,pos_a)
    exp = prob_a*trials
    return(exp)

exp_probability_2(1,4,20)

#expected values
#there are three possible outcomes
#hit a - 10 points (probability .5)
#hit b - 20 points (probability .4)
#hit c - 100 points (probability .1)
# E(X) = P(A)*A + P(B)*B + P(C)*C

def expected_value(ap,av,bp,bv,cp,cv):
    return((ap*av)+(bp*bv)+(cp*cv))

expected_value(.5,10,.4,20,.1,100)
