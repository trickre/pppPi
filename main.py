# -*- coding: utf-8 -*-
import random as rnd

number_PI = []  #照合する円周率の数列
N_max = 1000000   #最大試行回数
pppPI = ["p..","pp.","ppp","pppP","pppPI","pppPI!",]
idx_max = len(pppPI) #最大照合深さ、何桁目まで照合させるのか
N_idx = 0   #現在何回目の施行なのか
cnt_last = 0   #"pppPI!"までいった回数を数える
idx_print = 3   #print出力する深さ
def main():
    #1.照合用PI数列の用意
    for pi in [3,1,4,1,5,9,2,6,5]:
        number_PI.append(pi)
    #LOOP
    for cnt in range(N_max):
        do_func(0)

    #4.結果表示
    print("#Result")
    print("N is   :",end="");print(N_max)
    print("pppPI! :",end="");print(cnt_last)
    
def do_func(idx):#再帰関数として使いたい
    """
    about "idx":
    1.0でスタートする@main
    2.再帰的にidx=1で呼ばれた時点で既にpppPI[0]はprintされている。
    3.再帰的にidx=6で呼ばれた時点で既にpppPI[5]まですべてprintされている
    この時は何も施行もprintもしない
    """
    if idx < idx_max:
        global N_idx
        N_idx +=1   #randomな試行を行う
        #2.randamに1文字出力
        int_rand = rnd.randint(0,9)
        #3.照合
        if int_rand == number_PI[idx]:
            if idx>idx_print:
                print (N_idx,end="");       print(" :",end="")
                print(int_rand,end=" ");    print(pppPI[idx])
            do_func(idx+1)  #再帰利用
    elif idx == idx_max:
        global cnt_last
        cnt_last += 1

if __name__ == '__main__':
    print("<< pppPi Python PROGRAM >>")
    print("You can stop by \"Ctrl + C\"")
    main()