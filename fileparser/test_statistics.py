import seaborn as sns
import matplotlib.pyplot as plt
import os

from fileparser.toughreact import ToughReact
from plotting.plotStatistics import PlotStatistics

# iris = sns.load_dataset("iris")
# g = sns.PairGrid(iris)
# g.map(sns.scatterplot)
# plt.show()

filetype_toughreact_min = 'kdd_min.tec'

root_dir = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM " \
           r"Cement flow with batch\Increased depth\Grid Sensitivity "
file_toughreact = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\GOM Ca Onshore flux with Ca offshore"

stat_test = PlotStatistics('toughreact', file_toughreact, filetype_toughreact_min)
# print(stat_test.getAllDataIntoPandas(['calcite', 'jennite', 'portlandite', 'ettringite'], 116))
stat_test.plotRegular(['Porosity', 'calcite', 'dolomite', 'quartz(alpha'], 116)
# stat_test.plotScatter([4, 24, 25, 26], 116)
