X, Y = map(float, input().split())

M = ((Y - X) / X) * 100
print('%.2f' % M, '%', sep='')
