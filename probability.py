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
