#C is current price, s is strike price, t=time to maturity
from scipy.stats import norm
from math import *
def PutGreeks(C, S, T):
    v=0.30
    r=0.06
    T_sqrt = sqrt(T)
    d1 = (log(float(C)/S)+r*T)/(v*T_sqrt) + 0.5*v*T_sqrt
    d2 = d1-(v*T_sqrt)
    Delta = -norm.cdf(-d1)
    Gamma = norm.pdf(d1)/(C*v*T_sqrt)
    Theta = -(C*v*norm.pdf(d1)) / (2*T_sqrt)+ r*S * exp(-r*T) * norm.cdf(-d2)
    Vega = C * T_sqrt * norm.pdf(d1)
    Roh = -S*T*exp(-r*T) * norm.cdf(-d2)
    return Delta, Gamma, Theta, Vega, Roh

def CallGreeks(C, S, T):
 v = 0.30
 r = 0.06
 d=0
 T_sqrt = sqrt(T)
 d1 = (log(float(C)/S)+((r-d)+v*v/2.)*T)/(v*T_sqrt)
 d2 = d1-v*T_sqrt
 Delta = norm.cdf(d1)
 Gamma = norm.pdf(d1)/(C*v*T_sqrt)
 Theta =- (C*v*norm.pdf(d1))/(2*T_sqrt) - r*S*exp( -r*T)*norm.cdf(d2)
 Vega = C * T_sqrt*norm.pdf(d1)
 Roh = S*T*exp(-r*T)*norm.cdf(d2)
 return Delta, Gamma, Theta, Vega, Roh

C=float(input("enter current price of the option"))
S=float(input("enter strike price"))
T=float(input("enter time left"))
option=input("put or call?")
if option=="put":
    print(PutGreeks(C,S,T))
else:
    print(CallGreeks(C,S,T))
