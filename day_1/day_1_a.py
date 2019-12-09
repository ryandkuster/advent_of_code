import sys


def fuel_calc(mass):
    '''
    use // to return floor of division of mass
    '''
    fuel = mass//3 - 2
    return fuel

fuel = 0
with open(sys.argv[1]) as f:
    mass_ls = [int(i) for i in f]

for mass in mass_ls:
    fuel += fuel_calc(mass)

print(fuel)
