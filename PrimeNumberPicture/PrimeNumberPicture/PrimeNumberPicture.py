import random

def is_prime(n,sample):
    #自然数以外は判定しない
    if n<=0:
        return False
    #2は素数
    if n==2:
        return True
    #1は素数でない
    if n==1:
        return False
    #2以外の偶数は素数でない
    if n&1==0:
        return False

    #ここまででnは必ず奇数となる(=n-1は偶数)
    #n-1,0で開始
    d=n-1
    count=0

    #(2**s)*dのdを求める
    #2で割り切れる間割り続ける
    while d&1==0:
        d=d>>1
        count+=1

    #値を出力
    #print("2^"+str(count)+"*"+str(d))

    #最低1回は検査を行う
    if sample<=0:
        sample=1

    #サンプル数を表示
    print("サンプル数"+str(sample)+"での検査を開始")

    #sampleの回数分検査を行う
    for i in range(sample):

        #素数の可能性があればTrue
        flag=False

        #底a(1～n-1の整数)をランダムに選ぶ
        a=random.randint(1,n-1)
        
        #経過表示
        #print(str(i+1)+"回目:底a="+str(a))
        print(str(i+1)+"回目")

        #(a**d)%n==1ならば素数の可能性あり
        if pow(a,d,n)==1:
            flag=True

        #0～count-1について(a**((2**k)*d))%n==n-1ならば
        #素数の可能性あり
        for k in range(0,count):
            if pow(a,d,n)==n-1:
                flag=True
            d=d<<1

        #全てFalseのまま通過した場合は確実に合成数
        if flag==False:
            return False

    #全てのサンプルについて合成数と判定されなければ
    #一定以上の確率で素数
    return True

##メイン部分##
n=2**9941-1
sample=10

if is_prime(n,sample):
    print(str(1.0-pow(1/4,sample))+"以上の確率で素数")
else:
    print("合成数")
