# -*- coding: utf-8 -*-
number_PI = []  #照合する円周率の数列
N_max = 10000   #最大試行回数

import random as rnd
def main():
    #1.照合用PI数列の用意
    for pi in [3,1,4,1,5,9,2,6,5]:
        number_PI.append(pi)
    #LOOP
    for cnt in range(N_max):
        #2.randamに1文字出力
        print(rnd.randint(0,9))
        #3.1照合1段階
            #3.2照合2段階
                #3.3照合2段階
                    #3.4照合2段階

    #4.結果まとめ表示
if __name__ == '__main__':
    print("<< pppPi Python PROGRAM >>")
    print("You can stop by \"Ctrl + C\"")
    main()