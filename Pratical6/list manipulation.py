gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]# the list of
exon_counts=[51,1142,42,216,25,650,32533,57,1,523] # the data of exon counts
average_exon_lengths=[a/b for a,b in zip(gene_lengths,exon_counts)] # calculate the length
print(average_exon_lengths)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data is the exon lengths
data=[184.50980392156862, 345.1322241681261, 105.76190476190476, 487.6759259259259, 765.96, 118.12153846153846, 3.8898964128730826, 636.7719298245614, 842.0, 30.55640535372849]
# draw the boxplot
df = pd.DataFrame(data)
df.plot.box(title='average gene length')
plt.grid(linestyle="--", alpha=0.3)
plt.show()