pw_ls = []

for i in range(152085,670283):
    pw = [int(x) for x in str(i)]
    doubles_ls = ['']
    for idx, j in enumerate(pw):
        if idx > 0:
            if j >= pw[idx-1]:
                pass
            else:
                break
            if j == pw[idx-1]:
                if str(j) in doubles_ls[-1]:
                    doubles_ls[-1] = doubles_ls[-1] + str(j)
                else:
                    doubles_ls.append(str(j)+str(j))
        if idx == 5:
            doubles_ls.pop(0)
            if len(doubles_ls) > 0:
                for idx, j in enumerate(doubles_ls):
                    if len(j) == 2:
                        pw_ls.append(pw)
                        print(pw)
                        break


print(len(pw_ls))
