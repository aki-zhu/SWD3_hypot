def hyp_func(opp, adj):

    hyp = (opp**2) + (adj**2)

    hyp = (hyp) ** 0.5

    return hyp


opp = 3
adj = 4
y = hyp_func(opp, adj)
print(y)
