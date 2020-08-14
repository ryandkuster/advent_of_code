import sys


pairs_mx = []
orbits_mx = [['COM']]
with open(sys.argv[1]) as f:
    for line in f:
        pairs_mx.append(line.strip().split(')'))


def pair_n_count(pairs_mx, orbits_mx):
    for pair in pairs_mx:
        for orbit in orbits_mx:
            if pair[0] == orbit[-1]:
                new_orbit = orbit.copy()
                new_orbit.append(pair[1])
                if new_orbit not in orbits_mx:
                    orbits_mx.append(new_orbit)
    total = 0
    for i in orbits_mx:
        total += len(i) - 1
    return total


while True:
    total = pair_n_count(pairs_mx, orbits_mx)
    print(total)
    new_total = pair_n_count(pairs_mx, orbits_mx)
    print(new_total)
    if total == new_total:
        break
print(total)

for i in orbits_mx:
    if i[-1] == 'SAN':
        san_ls = i
    if i[-1] == 'YOU':
        you_ls = i
print(san_ls)
print(you_ls)
for counter, (i, j) in enumerate(zip(san_ls, you_ls)):
    if i != j:
        print(i, j)
