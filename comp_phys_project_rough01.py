import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math as m
import sympy as sym
import sys
import Functions_module_beta as fn 
from Functions_module_beta import MatrixAction_old
import Data
sys.path.append('C:/Users/pranj/Desktop/Python/Research_python')
from Data import big_phi, big_phi_abstract


choice159 =[0, 1, 1/(np.sqrt(2)), 1/(np.sqrt(2)), 1/(np.sqrt(2)), 0]
choice401 =[1, 1, 1/(np.sqrt(2)), 1/(np.sqrt(2)), 1, 1/(np.sqrt(2))]
choice449 =[1, 1/(np.sqrt(2)), 1, 1, 1/(np.sqrt(2)), 1/(np.sqrt(2))]




outs = [[1,0],[0,1]]
def MatrixAction_onephoton_reduced(reducedstate, phi= m.pi/4):                # reduced state is either [1,0] or [0,1]. phi is splitter angle
    t = m.cos(phi)
    r = m.sin(phi)
    prob_t = abs(t**2)
    prob_r = abs(r**2)
    upper = 10000
    x = rand.randint(1,upper)

    if reducedstate == [1,0]:
        if x <= prob_t*upper:
            out = [1,0]
        else:
            out = [0,1]
    elif reducedstate == [0,1]:
        if x <= prob_t*upper:
            out = [0,1]
        else:
            out = [1,0]
    elif reducedstate == [0,0]:
        out = [0,0]
    return out
# print(MatrixAction([0,1],.5))

def MatrixAction_reduced_complete(reducedstate, phi= m.pi/4):                # reduced state is either [1,0] or [0,1]. phi is splitter angle
    if reducedstate == [1,0] or reducedstate == [0,1] or reducedstate == [0,0]:
        out_full = MatrixAction_onephoton_reduced(reducedstate, phi)
    elif reducedstate == [2,0]:
        out_1 = MatrixAction_onephoton_reduced([1,0],phi)
        out_2 = MatrixAction_onephoton_reduced([1,0],phi)
    elif reducedstate == [0,2]:
        out_1 = MatrixAction_onephoton_reduced([0,1],phi)
        out_2 = MatrixAction_onephoton_reduced([0,1],phi)
    elif reducedstate == [1,1]:
        out_1 = MatrixAction_onephoton_reduced([1,0],phi)
        out_2 = MatrixAction_onephoton_reduced([0,1],phi)
    
    if reducedstate == [2,0] or reducedstate == [0,2] or reducedstate == [1,1]:
        if out_1 == [1,0] and out_2==[1,0]:
            out_full = [2,0]
        elif out_1 == [0,1] and out_2==[0,1]:
            out_full = [0,2]
        elif out_1 == [1,0] and out_2==[0,1]:
            out_full = [1,1]
        elif out_1 == [0,1] and out_2==[1,0]:
            out_full = [1,1]
    return out_full
# print(full_MatrixAction([2,0], m.pi/15))

counter,counter2,counter3,counter4,counter5,counter6,counterelse = 0,0,0,0,0,0,0
# print([counter3,counter4,counter2, counter5,counter6, (counter2+counter3+counter4)])


def MatrixAction_full(matrix_index, inputstate, phi):            # matrixindex is a string like '12' etc, inputstate is a list like [1,0,0,1]
    matrix_index_12_1 = int(matrix_index[0])
    matrix_index_12_2 = int(matrix_index[1])
    reduced_inputstate = [inputstate[matrix_index_12_1-1],inputstate[matrix_index_12_2-1]]
    reduced_out = MatrixAction_reduced_complete(reduced_inputstate, phi)
    full_out = [i for i in inputstate]
    full_out[matrix_index_12_1-1] = reduced_out[0]
    full_out[matrix_index_12_2-1] = reduced_out[1]
    return full_out

def SystemAction_classical(inputstate ,splitter_comb):                    # inputstate is a vector like [1,0,0,1], splitter_comb is a list of six splitter angles
    M12_out = MatrixAction_full('12', inputstate, splitter_comb[0])
    M13_out = MatrixAction_full('13', M12_out, splitter_comb[1])
    M14_out = MatrixAction_full('14', M13_out, splitter_comb[2])
    M23_out = MatrixAction_full('23', M14_out, splitter_comb[3])
    M24_out = MatrixAction_full('24', M23_out, splitter_comb[4])
    M34_out = MatrixAction_full('34', M24_out, splitter_comb[5])
    return M34_out

splitters = [m.pi/4,m.pi/4,m.pi/4,m.pi/4,m.pi/4,m.pi/4]  
# SystemAction(fn.ten_states_9, splitters)
    
def rounding_centered(L):
    roundoffs = [.5,.70710,1,0]
    for j in roundoffs:
        for i in range(len(L)):              # removing the .499999, .70734.. etc. roundoff errors
            # if abs(L[i]) < 1e-12:
            #     L[i] = 0
            if abs((abs(L[i])-j)) < .002:
                if L[i] > 0:
                    L[i] = j
                elif L[i] < 0:
                    L[i] = -j
    return L
    


def probabilities(inputstate_list, coeff_list, splitter_comb, n = 10000):            # n is #of trials
    numbers = [0,0,0,0,0,0,0,0,0,0]
    input_prob_list = [abs(i)**2 for i in coeff_list ] 
    for i in range(n):
        collapsed_state = rand.choices(inputstate_list, input_prob_list, k =1)[0]           # [0] coz the choices fn outputs a list but we just want the element
        out = SystemAction_classical(collapsed_state, splitter_comb)
        j = fn.TenStateBasis.index(out)             # tells the position where we want to add +1
        numbers[j] +=1
    out_prob_list = [i/n for i in numbers] 
    return out_prob_list


bell_V = [fn.phiplus_V,fn.phiminus_V,fn.psiplus_V,fn.psiminus_V]
bell_C = [fn.phiplus_C,fn.phiminus_C,fn.psiplus_C,fn.psiminus_C]


def coeff_to_prob(L):
    return [abs(i)**2 for i in L] 
    

ac = (probabilities(bell_V[0], bell_C[0], big_phi[105]))

aq = (coeff_to_prob(fn.SystemAction(bell_V[0], bell_C[0], big_phi_abstract[105], 34, True)[1]))


# print(f'{rounding_centered(ac)} , with sum {sum(ac)}')
# print(f'{rounding_centered(aq)} , with sum {sum(aq)}')


def fourlist(splitters, kind = 'qm'):                   # change kind to 'cm' for classical probabilities 
    out_four = []
    if kind == 'cm':
        out_four.append(rounding_centered(probabilities(bell_V[0], bell_C[0], splitters)))
        out_four.append(rounding_centered(probabilities(bell_V[1], bell_C[1], splitters)))
        out_four.append(rounding_centered(probabilities(bell_V[2], bell_C[2], splitters)))
        out_four.append(rounding_centered(probabilities(bell_V[3], bell_C[3], splitters)))
    elif kind == 'qm':
        out_four.append(fn.rounding((coeff_to_prob(fn.SystemAction(bell_V[0], bell_C[0], splitters,34,True)[1])),3))
        out_four.append(fn.rounding((coeff_to_prob(fn.SystemAction(bell_V[1], bell_C[1], splitters,34,True)[1])),3))
        out_four.append(fn.rounding((coeff_to_prob(fn.SystemAction(bell_V[2], bell_C[2], splitters,34,True)[1])),3))
        out_four.append(fn.rounding((coeff_to_prob(fn.SystemAction(bell_V[3], bell_C[3], splitters,34,True)[1])),3))
    return out_four

print(fourlist(choice159, 'cm'))

# take : big_phi: 0, 105

# PLOTTING

barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
prob_classical = rounding_centered(ac)
prob_QM = rounding_centered(aq)

# Set position of bar on X axis
br1 = np.arange(len(prob_classical))
br2 = [x + barWidth for x in br1]
# br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, prob_classical, color ='r', width = barWidth,
        edgecolor ='grey', label ='IT')
plt.bar(br2, prob_QM, color ='g', width = barWidth,
        edgecolor ='grey', label ='ECE')
# plt.bar(br3, CSE, color ='b', width = barWidth,
#         edgecolor ='grey', label ='CSE')
 
# Adding Xticks
plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(prob_classical))],
        ['2015', '2016', '2017', '2018', '2019','d1f','df2','d3f','d3f','df4'])
 
plt.legend()
# plt.show()






    




