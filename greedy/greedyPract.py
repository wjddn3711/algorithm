def coin(price):
    cnt =0
    while price>0:
        if price >= 500:
           cnt += price//500
           price = price%500
        elif price >= 100:
            cnt += price//100
            price = price%100
        elif price >= 50:
            cnt += price//50
            price = price%50
        else:
            cnt +=price//1
            price = price%1
    return cnt

print(coin(4720))
