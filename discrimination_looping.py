from lib2to3.pygram import Symbols
from re import A
import sympy as sym
import numpy as np

# Dummy = [t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34]
def Output_states_list(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34):
    # f below is a list of four elts, each one is the general output of an input bell state    
    f= [[r24*(-np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))+t24*(r23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14)),r34*(-r24*(r23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2)))+t34*(-r23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14)+t23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)),-r34*(-r23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14)+t23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12))+t34*(-r24*(r23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))),r12*r13*t13*t14**2+r14*t12*t13*t14,r34*(np.sqrt(2)*r24*t24*(r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(-r12*r13*r23**2*t13+r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)))+t34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))),-r34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2)))+t34*(np.sqrt(2)*r24*t24*(r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(-r12*r13*r23**2*t13+r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))),r24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14)+np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23),-np.sqrt(2)*r34*t34*(-r12*r13*t13*t23**2-r23*t12*t13*t23)+np.sqrt(2)*r34*t34*(r24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14))+(-r34**2+t34**2)*(-r24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))),r34**2*(r24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14))+np.sqrt(2)*r34*t34*(-r24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(-r12*r13*t13*t23**2-r23*t12*t13*t23),r34**2*(-r12*r13*t13*t23**2-r23*t12*t13*t23)-np.sqrt(2)*r34*t34*(-r24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(r24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14))],[r24*(np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))+t24*(r23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14)),r34*(-r24*(r23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2)))+t34*(-r23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)),-r34*(-r23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12))+t34*(-r24*(r23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))),-r12*r13*t13*t14**2+r14*t12*t13*t14,r34*(np.sqrt(2)*r24*t24*(-r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(r12*r13*r23**2*t13-r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)))+t34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))),-r34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2)))+t34*(np.sqrt(2)*r24*t24*(-r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(r12*r13*r23**2*t13-r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))),r24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14)+np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23),-np.sqrt(2)*r34*t34*(r12*r13*t13*t23**2+r23*t12*t13*t23)+np.sqrt(2)*r34*t34*(r24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14))+(-r34**2+t34**2)*(-r24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))),r34**2*(r24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14))+np.sqrt(2)*r34*t34*(-r24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(r12*r13*t13*t23**2+r23*t12*t13*t23),r34**2*(r12*r13*t13*t23**2+r23*t12*t13*t23)-np.sqrt(2)*r34*t34*(-r24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(r24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14))],[r24*((1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)+t24*(r23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12)),r34*(-r24*(r23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12))+t24*((1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14))+t34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))),-r34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2)))+t34*(-r24*(r23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12))+t24*((1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)),r34*(np.sqrt(2)*r24*t24*(-r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)))+t34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)),-r34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23))+t34*(np.sqrt(2)*r24*t24*(-r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))),r24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13)+np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13),-np.sqrt(2)*r34*t34*(r12*r23*t13*t23-r13*t12*t13*t23**2)+np.sqrt(2)*r34*t34*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13))+(-r34**2+t34**2)*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))),r34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13))+np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2),r34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2)-np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13)),r12*r14*t13*t14+r13*t12*t13*t14**2],[r24*(-(1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)+t24*(r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12)),r34*(-r24*(r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12))+t24*(-(1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14))+t34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12)+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))),-r34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12)+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2)))+t34*(-r24*(r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12))+t24*(-(1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)),r34*(np.sqrt(2)*r24*t24*(r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)))+t34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)),-r34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23))+t34*(np.sqrt(2)*r24*t24*(r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))),r24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13)+np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13),-np.sqrt(2)*r34*t34*(r12*r23*t13*t23-r13*t12*t13*t23**2)+np.sqrt(2)*r34*t34*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13))+(-r34**2+t34**2)*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))),r34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13))+np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2),r34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2)-np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13)),-r12*r14*t13*t14+r13*t12*t13*t14**2]]
    return f

def Dummy(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34):
    # f below is a trial
    f= t12+r12+t13+r13+t14+r14+t23+r23+t24+r24+t34+r34
    return f 

possible_values = [0,.5]#, 1/(np.sqrt(2))] #, -1/(np.sqrt(2)),-1]

t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34 = sym.symbols("t12, r12, t13, r13, t14, r14, t23, r23, t24, r24, t34, r34")



k = len(possible_values)
for i in range(len(possible_values)):
    t12 = possible_values[i]
    r12 = np.sqrt(1-possible_values[i]**2)
    for j in range(len(possible_values)):
        t13 = possible_values[j]
        r13 = np.sqrt(1-possible_values[j]**2)
        for k in range(len(possible_values)):
            t14 = possible_values[k]
            r14 = np.sqrt(1-possible_values[k]**2)
            for l in range(len(possible_values)):
                t23 = possible_values[l]
                r23 = np.sqrt(1-possible_values[l]**2)
                for m in range(len(possible_values)):
                    t24 = possible_values[m]
                    r24 = np.sqrt(1-possible_values[m]**2)
                    for n in range(len(possible_values)):
                        t34 = possible_values[n]
                        r34 = np.sqrt(1-possible_values[n]**2)
                        print(Dummy(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34))
                       

# print(AllCombinations(Dummy))

