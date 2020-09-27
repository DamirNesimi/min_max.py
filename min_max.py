"""
Dette programmet bruker funksjonene egen_max og egen_min som beregner maximum og minimum av to tall
skrevet inn av en bruker.
27.09.2020

"""

# funksjon som returnerer den største verdien av tall_1 og tall_2
def egen_max(tall_1, tall_2):
    max = (tall_1 + tall_2 + abs(tall_1 - tall_2))//2
    return max

# funksjon som returnerer den minste verdien av tall_1 og tall_2
def egen_min(tall_1, tall_2):
    min = (tall_1 + tall_2 - abs(tall_1 - tall_2))//2
    return min

# variabler som lagrer verdien fra input av bruker
tall_1 = input("Tall 1: ")
tall_2 = input("Tall 2: ")

# verdien konverteres til heltallsverdi
tall_1_int = int(tall_1)
tall_2_int = int(tall_2)

# output til skjerm
print()
print("egen_max(" + tall_1 + ", " + tall_2 + ") = " + str(egen_max(tall_1_int, tall_2_int)))
print("max(" + tall_1 + ", " + tall_2 + ") = " + str(max(tall_1_int, tall_2_int)))

print()
print("egen_min(" + tall_1 + ", " + tall_2 + ") = " + str(egen_min(tall_1_int, tall_2_int)))
print("min(" + tall_1 + ", " + tall_2 + ") = " + str(min(tall_1_int, tall_2_int)))
