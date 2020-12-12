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
file_toughreact = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\GOM Ca " \
                  r"Onshore flux with Ca offshore "


stat_test = PlotStatistics('toughreact', file_toughreact, filetype_toughreact_min)
stat_test.plotRegular(['Porosity', 'calcite', 'dolomite', 'quartz(alpha'], 116)
stat_test.plotRegular(['Porosity', 'calcite', 'dolomite', 'mg+2'], 116, format='all')

# root_dir = r"C:\Users\tajayi3\OneDrive - Louisiana State University"
#
# file = os.path.join(root_dir, r"tmvoc\mymodels\paper work\one component\batch biodg")
# print(file)
#
# filetype_tmvoc = "OUTPUT_ELEME.csv"
#
# stat_test = PlotStatistics('tmvoc', file, filetype_tmvoc)
# stat_test.plotRegular(['X_Toluen_L', 'X_Toluen_N'], 0)
