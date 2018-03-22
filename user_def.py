import sympy as s

def terms_list(p):
    # polynomial to list of monomials
    return [s.Poly(dict([c]),p.free_symbols) for c in p.terms()]

def exponents(p,symb):
    #exponent of p with respect to variable symb
    return [s.Poly(t,symb).as_dict().items()[0][0][0] for t in terms_list(p)]

def deg_monom(p):
    #degree of each monomial in 
    return [sum(t.as_dict().items()[0][0]) for t in terms_list(p)]

def coeff(p):
    return [t.as_dict().items()[0][1] for t in terms_list(p)]
