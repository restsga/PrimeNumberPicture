import random
import numpy as np

#素数判定(ミラーラビン)
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
    #print("サンプル数"+str(sample)+"での検査を開始")

    #sampleの回数分検査を行う
    for i in range(sample):

        #素数の可能性があればTrue
        flag=False

        #底a(1～n-1の整数)をランダムに選ぶ
        a=random.randint(1,n-1)
        
        #経過表示
        #print(str(i+1)+"回目")

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


#順列の全探索用の関数
def search(depth,color_array,result):
    for i in range(0,10):
        if i not in color_array:
            if depth>0:
                search(depth-1,color_array+[i],result)
            else:
                result.append(color_array)
                return


#開始通知
print("判定を開始します")
print()

#画像変換用のオフセット値
offset=100
#色の種類数
colors=3
#画素数(一辺)
pixel_count=16

#絵
picture=np.array([
    [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,2,1,1,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1],
    [0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
    ])

#元画像表示
print("元画像")
print(str(picture))
print()

#オフセット調整
picture=picture+offset

#順列を求める
list=[]
search(colors,[],list)

#いくつ存在するか
prime_result_count=0

#順列ごとに素数判定
for color_array in list:

    #画像を配列としてコピー
    array=picture

    #色を値に置換
    for i in range(0,colors):
        array=np.where(array==offset+i,color_array[i],array)

    #配列を整数に変換
    n=0
    digit=1
    for y in reversed(range(0,pixel_count)):
        for x in reversed(range(0,pixel_count)):
            n=n+int(array[y,x])*digit
            digit*=10

    ##メイン部分##
    sample=50

    if is_prime(n,sample):
        print("該当する素数が見つかりました")
        print(str(array))
        print()
        #print(str(n))
        #print("は")
        #print(str(1.0-pow(1/4,sample))+"以上の確率(サンプル数:"+str(sample)+")で素数")

        prime_result_count+=1
    #else:
        #print("合成数")

#存在しない通知
if prime_result_count<=0:
    print("見つかりませんでした...")
else:
    print(str(prime_result_count)+"個見つかりました")
