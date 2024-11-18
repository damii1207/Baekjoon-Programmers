n = int(input())

for i in range(n):
    coin = int(input())
    qua = coin//25
    ra = (coin-qua*25)//10
    da = (coin-qua*25-ra*10)//5
    pe = (coin-qua*25-ra*10-da*5)//1
    print('%d' % qua,'%d' % ra,'%d' % da,'%d'% pe,sep=" ")