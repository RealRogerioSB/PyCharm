def alg_romano(num_rom):
    val_int = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    val_rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    num_romano = ""
    b = 0
    while num_rom > 0:
        for _ in range(num_rom // val_int[b]):
            num_romano += val_rom[b]
            num_rom -= val_int[b]
        b += 1
    return num_romano


num = int(input("Digite um número a ser convertido: "))

print(">>>", alg_romano(num))
