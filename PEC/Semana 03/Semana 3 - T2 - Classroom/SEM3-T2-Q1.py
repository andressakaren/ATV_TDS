PI = 3.141592
raio = float(input("Digite o raio: "))
circunferencia = 2 * PI * raio
a_circulo = PI * raio ** 2
a_esfera = 4 * PI * raio ** 2
vol_esfera = 4 / 3 * PI * raio ** 3

print(f"Circunferência: {circunferencia:.6f}.")
print(f"Área do círculo: {a_circulo:.6f}.")
print(f"Área da esfera: {a_esfera:.6f}.")
print(f"Volume da esfera: {vol_esfera:.6f}.")
