l1 = ['bat', 'rat', 'hat', 'juggernaut']


def len1(x):
    return x, len(x), x.upper(), x.capitalize(), x[:1]


l2 = list(map(len1, l1))
print(l2)

