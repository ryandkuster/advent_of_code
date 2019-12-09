import sys


def fuel_calc(mass):
    '''
    use // to return floor of division of mass
    '''
    fuel = mass//3 - 2
    if fuel > 6:
        fuels_fuel = fuel_calc(fuel)
        fuel += fuels_fuel
    return fuel


total_fuel = 0
with open(sys.argv[1]) as f:
    mass_ls = [int(i) for i in f]

for mass in mass_ls:
    total_fuel += fuel_calc(mass)
print(total_fuel)
