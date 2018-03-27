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



def secondogrado(a,b,c):
    if a==0:
        return [-c/b]
    Delta=b**2-4*a*c
    if Delta <0:
        return []
    elif Delta==0:
        return [-b/(2*a)]
    else:
        return [(-b-s.sqrt(Delta))/(2*a),(-b+s.sqrt(Delta))/(2*a)]

def intersezione(C,r):
    x,y=s.symbols('x y')
    eq=C.equation(x,y)
    c=r.coefficients
    m,q=-c[0]/c[1], -c[2]/c[1]
    eq2=eq.subs(y,m*x+q).as_poly().as_expr()
    a,b,c=eq2.coeff(x**2), eq2.coeff(x), eq2.subs(x,0)
    xlist=secondogrado(a,b,c)
    return [s.Point(x_,m*x_+q) for x_ in xlist]

def tangente(C,r):
    x,y=s.symbols('x y')
    eq=C.equation(x,y)
    c=r.coefficients
    m,q=-c[0]/c[1], -c[2]/c[1]
    eq2=eq.subs(y,m*x+q).as_poly().as_expr()
    a,b,c=eq2.coeff(x**2), eq2.coeff(x), eq2.subs(x,0)
    return b**2-4*a*c==0

def implicita(r):
    c=r.coefficients
    return -c[0]/c[1], -c[2]/c[1]