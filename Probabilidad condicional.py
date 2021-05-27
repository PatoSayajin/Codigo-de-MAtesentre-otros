from fractions import Fraction
print("Probabilidad condicional:\n\nEjemplo: ")
ejemplo = {"titulo": "apro--repro = total","H": "H:12-----4 =    16", "M": "M:20-----4 =    24", "T": "T:32-----8 =    40"}
p_r_h = (4/40)/(16/40)
p_r_h_f = str(Fraction(p_r_h))
print(ejemplo["titulo"])
print(ejemplo["M"])
print(ejemplo["H"])
print(ejemplo["T"])
print(f"La probabilidad de cuantos hombres reprobaron es: (4/40)/(16/40) = {p_r_h} = {p_r_h_f}\n")

print("La probsbilidad de P(A|B) =   P(A/\B)\n                            ----------\n                               P(B)\n")

evento = float(input("Introduce evento: "))
condicion = float(input("Introduce condicion: "))
total = float(input("Introduce la suma total: "))
p_e_c = (evento/total)/(condicion/total)
p_e_c_f = Fraction(p_e_c).limit_denominator()
print(f"La probabilidad es ({evento}/{total})/({condicion}/{total}) = {p_e_c} = {p_e_c_f}")