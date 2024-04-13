import numpy as np

###Fuck With These Values###
CP= 17.8    ## stock price
Vol=0.507    ## Volatility as a decimal
Tdays=45      ## dte
longc=19     ## call you bought
shortc=18    ## call you sold
premium=35   ## credit
###Run Code#################

T=Tdays/365
sigma=0.4*Vol*CP*np.sqrt(T)

def gauss(x):
    return 1/(sigma*np.sqrt(2*np.pi))*np.e**((-1/2)*((x-CP)/sigma)**2)

def region_a(): ## all values $$.$$ that are below the short call
    tot=0
    for i in range(0,int(shortc*100+1)):
        tot+=gauss(i/100)/100
    max_loss=-(longc-shortc)*100+premium
    eva=tot*premium
    return tot, eva

def loss(x):    ## calculates P/L at any point between the strikes
    y=int(shortc*100-x*100)
    return y+premium

def region_b(): ## all values $$.$$ that are between the two strikes
    tot=0
    evb=0
    for i in range(int(shortc*100+1),int(longc*100)):
        tot+=gauss(i/100)/100
        evb+=gauss(i/100)/100*loss(i/100)
    return tot, evb

def region_c(): ## all values $$.$$ that are above the long strike
    tot=1-region_a()[0]-region_b()[0]
    max_loss=-(longc-shortc)*100+premium
    evc=max_loss*tot
    return tot, evc

def EV():       ## dollar value expected from this trade on average
    a=region_a()[1]
    b=region_b()[1]
    c=region_c()[1]
    return round(a+b+c-2.6,2)

print(EV())