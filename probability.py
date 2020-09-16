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
