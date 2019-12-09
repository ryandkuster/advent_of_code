pw_ls = []

for i in range(152085,670283):
    double = False
    pw = [int(x) for x in str(i)]
    for idx, j in enumerate(pw):
        if idx > 0:
            if j >= pw[idx-1]:
                pass
            else:
                break
            if j == pw[idx-1]:
                double = True
        if idx == 5 and double is True:
            pw_ls.append(pw)

print(len(pw_ls))
