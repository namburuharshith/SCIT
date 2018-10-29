import numpy as np
m=int(input("Input Mean value : "))
md=int(input("Input Meadian value : "))
s=np.random.normal(loc=m,scale=md,size=1000)
import matplotlib.pyplot as pyplot
count, bins, ignored = pyplot.hist(s,15, normed=True)
pyplot.grid(axis='y', alpha=0.75)
pyplot.xlabel('Value')
pyplot.ylabel('Frequency')
pyplot.title('Histogram using normal')
pyplot.text(7, 0.11, "mean = "+str(m)+"\nmedian = "+str(md),fontsize = 12)
pyplot.show()