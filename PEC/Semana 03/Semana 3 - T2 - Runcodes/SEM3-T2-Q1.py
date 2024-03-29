PI = 3.141592
raio = float(input())
circunferencia = 2 * PI * raio
a_circulo = PI * raio ** 2
a_esfera = 4 * PI * raio ** 2
vol_esfera = 4 / 3 * PI * raio ** 3

print(f"{circunferencia:.6f}")
print(f"{a_circulo:.6f}")
print(f"{a_esfera:.6f}")
print(f"{vol_esfera:.6f}")
