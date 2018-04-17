# -*- coding: utf-8 -*-
import random as rnd

number_PI = []  #照合する円周率の数列
N_max = 10000   #最大試行回数
pppPI = ["p","p","p","P","I","!",]
idx_max = len(pppPI) #最大照合深さ、何桁目まで照合させるのか

def main():
    #1.照合用PI数列の用意
    for pi in [3,1,4,1,5,9,2,6,5]:
        number_PI.append(pi)
    #LOOP
    for cnt in range(N_max):
        do_func(0)
    #4.結果まとめ表示

def do_func(idx):#再帰関数として使いたい
    if idx < idx_max:
        #2.randamに1文字出力
        int_rand = rnd.randint(0,9)
        print(int_rand,end=" ")
        #3.照合
        if int_rand == number_PI[idx]:
            print(pppPI[idx])
            do_func(idx+1)  #再帰利用
        print("\n")

if __name__ == '__main__':
    print("<< pppPi Python PROGRAM >>")
    print("You can stop by \"Ctrl + C\"")
    main()