from ml1 import s as s1
from ml1 import l as la
from ml2 import s as s2
from ml2 import m as me
from ml2 import md as med
import random
list = []
for i in range(0,100):
	list.append(random.choice(s1))
for i in range(0,100):
	list.append(random.choice(s2))
import matplotlib.pyplot as pyplot
count, bins, ignored = pyplot.hist(list,15, normed=True)
pyplot.grid(axis='y', alpha=0.75)
pyplot.xlabel('Value')
pyplot.ylabel('Frequency')
pyplot.title('Histogram using normal and poisson')
pyplot.text(7, 0.11, "mean = "+str(me)+"\nmedian = "+str(med)+"\nlambda = "+str(la),fontsize = 12)
pyplot.show()
