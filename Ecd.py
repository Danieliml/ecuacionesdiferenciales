import sympy
from scipy import integrate

#Imprimir con notacion matematica
sympy.init_printing(use_latex='mathjax')

#Resolviendo ecuacion diferencial
#Defino las incognitas

x = sympy.Symbol('x')
y = sympy.Function('y')

#Expreso la ecuacion
f = 6*x**2 - 3*x**2*(y(x))
sympy.Eq(y(x).diff(x),f)

#Resolvemos la ecuacion
sympy.dsolve(y(x).diff(x) - f)



