import numpy as np
import math as m
import sympy as sym
import random as rand
import Functions_module_beta as fn
import Data

from Functions_module_beta import MatrixAction, SystemAction


bell_V = [fn.phiplus_V,fn.phiminus_V,fn.psiplus_V,fn.psiminus_V]
bell_C = [fn.phiplus_C,fn.phiminus_C,fn.psiplus_C,fn.psiminus_C]


mirror_list = [12,13,14,23,24,34]


#Chekcs out:  phiplus



def radians(degrees):           # degrees  to radians
    rad = (sym.pi/180)*degrees
    return rad 


#######_Definitions_######

theta = sym.symbols('theta')
theta = 45                                          # theta in degrees, default 45 gives Bell states

phiplus_like_V = [fn.ten_states_2,fn.ten_states_5]                      #Bell-like vectors
phiminus_like_V = [fn.ten_states_2,fn.ten_states_5]
psiplus_like_V = [fn.ten_states_3,fn.ten_states_4]
psiminus_like_V = [fn.ten_states_3,fn.ten_states_4]

phiplus_like_C = [sym.cos(radians(theta)),sym.sin(radians(theta))]              #Bell-like coeffs ie. disturbing C slightly away from the perfect ones in bell states, like theta degrees instead of theta
phiminus_like_C = [sym.sin(radians(theta)), -sym.cos(radians(theta))]
psiplus_like_C = [sym.cos(radians(theta)),sym.sin(radians(theta))]
psiminus_like_C = [sym.sin(radians(theta)), -sym.cos(radians(theta))]

bell_like_V = [phiplus_like_V,phiminus_like_V,psiplus_like_V,psiminus_like_V]           # making lists of bell-like vectos (and coeffs) so easier to change them as arguments later
bell_like_C = [phiplus_like_C,phiminus_like_C,psiplus_like_C,psiminus_like_C]





zz = fn.SystemAction(bell_V[0],bell_C[0], [0,sym.pi/2,sym.pi/4,0,0,0], 34, True)[1]

mirr = Data.big_phi_abstract[100]

def four_list(splitter_comb, Bell_or_BellLike = 'B', rounding = False, compared = False):     # splitter comb is a six-list of the six splitters, change to 'BL' for bell like, change to True for rounding, compared to True if want in output-by-output comparison format 
    if Bell_or_BellLike == 'B':
        Bell_V = bell_V
        Bell_C = bell_C
    else:
        Bell_V = bell_like_V
        Bell_C = bell_like_C
    four_list = []
    for i in range(4):
        bell_out_C = fn.SystemAction(Bell_V[i],Bell_C[i], splitter_comb, 34, rounding)[1]
        four_list.append(bell_out_C)
    compared_four_list = [[four_list[i][j] for i in range(4)] for j in range(10)]
    if compared == False:
        return four_list
    else:
        return compared_four_list


# dd = fn.SystemAction(bell_V[0],bell_C[0], mirr, 34, True)[1]
# print(dd)
# print(four_list(mirr))
# print(fn.AvgProbability(four_list(mirr)))


good_avg_prob_choices = []
best_avg_prob_choices = []
for i in range(2978,len(Data.big_phi_abstract)):
    mirr = Data.big_phi_abstract[i]
    avg = fn.rounding([fn.AvgProbability(four_list(mirr))])[0]
    if avg >= .24:
        good_avg_prob_choices.append([avg,i])
        if avg > .49:
            best_avg_prob_choices.append([avg,i])
            
print(f'Best avg prob choices = {best_avg_prob_choices}')                      # works. gives list of pairs [avg_prob,i] where avg is the avg prob of the four list corresp to the ith splitter comb of the splitter comb list in Data.py 

# choice = 2230
# print(f'choice {choice} : {four_list(Data.big_phi_abstract[choice], rounding = True)}')
# print(f'choice {choice} compared : {four_list(Data.big_phi_abstract[choice], rounding = True, compared = True)}')


# about first one third of the best choices, each with avg_prb 0.5 = [886,888,896,898,930,932,934,940,942,944,980,982,984,990,992,994,1136,1138,1146,1148,1180,1182,[ 1667], 1669,1670,1671,1672,1673,1674,1676,1678,1700,1702,1704,1705,1707,1709,1710,1711,1712,1713,1714,1715,1717,1719,1720,1721,1722,1723,1724,1726,1728,2136,
# 2138,2146,2148,2180,2182,2184,2190,2192,2194,2230,2232,2234,2240,2242,2244,2386,2388,2396,2398,2430,2432,2434,2440,2442,2444,2480,2482,2484,2490,2492,2494,2626,2628,2650,2652,2654,2655,2657,2659,2660,2661,2662,2663,2664,2665,2667,2669,2670,2671,2672,2673,2674,2676,2678,2700,2702,2704,2705,2707,2709,2710,2711,2712,2713,2714,
# 2715,2717,2719,2720,2721,2722,2723,2724,2726,2728,2876,2878,2900,2902,2904,2905,2907,2909,2910,2911,2912,2913,2914,2915,2917,2919,2920,2921,2922,2923,2924,2926,2928,2950,2952,2954,2955,2957,2959,2960,2961,2962,2963,2964,2965,2967,2969,2970,2971,2972,2973,2974,2976,2978]



#[1405,1407,1409,1411,1413,1415,1417,1419,1421,1423,1455,1457,1459,1461,1463,1465,1467,1469,1471,1473,1655,1657,1659,1661,1663,1665,1667,1669,1671,1673,1705,1707,1709,1711,1713,1715,1717,1719,1721,1723,2655,2657,2659,2661,2663,2665,2667,2669,2671,2673,2705,2707,2709,2711,2713,2715,2717,2719,2721,2723,2905,2907,2909,2911,2913,2915,2917,2919,2921,2923,2955,2957,2959,2961,2963,2965,2967,2969,2971,2973,7655,7657,7659,7661,7663,7665,7667,7669,7671,7673,7705,7707,7709,7711,7713,7715,7717,7719,7721,7723,7905,7907,7909,7911,7913,7915,7917,7919,7921,7923,7955,7957,7959,7961,7963,7965,7967,7969,7971,7973,8905,8907,8909,8911,8913,8915,8917,8919,8921,8923,8955,8957,8959,8961,8963,8965,8967,8969,8971,8973,9155,9157,9159,9161,9163,9165,9167,9169,9171,9173,9205,9207,9209,9211,9213,9215,9217,9219,9221,9223,13905,13907,13909,13911,13913,13915,13917,13919,13921,13923,13955,13957,13959,13961,13963,13965,13967,13969,13971,13973,14155,14157,14159,14161,14163,14165,14167,14169,14171,14173,14205,14207,14209,14211,14213,14215,14217,14219,14221,14223,15155,15157,15159,15161,15163,15165,15167,15169,15171,15173,15205,15207,15209,15211,15213,15215,15217,15219,15221,15223,15405,15407,15409,15411,15413,15415,15417,15419,15421,15423,15455,15457,15459,15461,15463,15465,15467,15469,15471,15473]



























