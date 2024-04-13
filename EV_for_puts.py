import numpy as np

###Fuck With These Values###
CP=353.4       ## stock price
Vol=0.226    ## Volatility as a decimal
Tdays=44     ## dte
longp=345     ## put you bought
shortp=346    ## put you sold
premium=30   ## credit
###Run Code#################

T=Tdays/365
sigma=0.4*Vol*CP*np.sqrt(T)

def gauss(x):
    return 1/(sigma*np.sqrt(2*np.pi))*np.e**((-1/2)*((x-CP)/sigma)**2)

def region_a(): ## all values $$.$$ that are below the long put
    tot=0
    for i in range(0,longp*100+1):
        tot+=gauss(i/100)/100
    max_loss=-(shortp-longp)*100+premium
    eva=tot*max_loss
    return tot, eva

def loss(x):    ## calculates P/L at any point between the strikes
    y=int(x*100-shortp*100)
    return y+premium

def region_b(): ## all values $$.$$ that are between the two strikes
    tot=0
    evb=0
    for i in range(longp*100+1,shortp*100):
        tot+=gauss(i/100)/100
        evb+=gauss(i/100)/100*loss(i/100)
    return tot, evb

def region_c(): ## all values $$.$$ that are above the short strike
    tot=1-region_a()[0]-region_b()[0]
    evc=premium*tot
    return tot, evc

def EV():       ## dollar value expected from this trade on average
    a=region_a()[1]
    b=region_b()[1]
    c=region_c()[1]
    return round(a+b+c-2.6,2)

print(EV())