def f(x): #f(x)
    return 3 * x - 1

def g(x): # g(x)
    return x + 2

# função de composição de funções, usando (a) e (b) para representar (função ° função)
def composition(a, b): # Entrada de Funções
    def calc(x): # calculo de (função(função(x)))
        return a(b(x))
    return calc

x = 4

gf = composition(g, f) # g ° f
fg = composition(f, g) # f ° g
ff = composition(f, f) # f ° f
gg = composition(g, g) # g ° g

result_gf = gf(x)
result_fg = fg(x)
result_ff = ff(x)
result_gg = gg(x)

# f para formatar as strings e usar {} para chamar os resultados, sem precisar separar tudo por ,
print(f"(g o f)({x}) = {result_gf}")
print(f"(f o g)({x}) = {result_fg}")
print(f"(f o f)({x}) = {result_ff}")
print(f"(g o g)({x}) = {result_gg}")


