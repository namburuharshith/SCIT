import numpy as np
l=int(input("Enter Lambda Value : "))
s = list(np.random.poisson(l, 1000))

import matplotlib.pyplot as pyplot
count, bins, ignored = pyplot.hist(s, 15, normed=True)
pyplot.grid(axis='y', alpha=0.75)
pyplot.xlabel('Value')
pyplot.ylabel('Frequency')
pyplot.title('Histogram using poisson')
pyplot.text(5.7, 0.4, "lam = "+str(l),fontsize = 12)
pyplot.show()