yin = list(map(int,input().split()))
if yin == sorted(yin):
    print('ascending')
elif yin == sorted(yin, reverse=True):
    print('descending')
else:
    print('mixed')
