import numpy as np
import matplotlib.pyplot as pl
from to_do_list_final import *
l=[]
for i in rang(1,message+1):
  l.append('Task'+str(i))

y=l
pl.plot(x,y)
