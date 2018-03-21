import sympy as s

def terms_list(a,*symb):
	# polynomial to list of monomials
	return [s.Poly(dict([c]),*symb) for c in a.terms()]

def exponents(p,i):
    #lista di esponenti rispetto all'i-esima variabile
    l=p.as_dict().items()
    return [h[0][i] for h in l]

def coeff(p):
    #lista di coefficienti (ordinata come gli esponenti)
    return [h[1] for h in p.as_dict().items()]

#def gr_monom(p):
#    return [sum(t.as_dict().items()[0][0]) for t in terms_list(a,x,y)]

def gr_monom(p):
    l=p.as_dict().items()
    nter=len(l)
    out=[]
    for i in range(nter):
        out+=[sum(l[i][0])]
    return out