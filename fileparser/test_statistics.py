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

root_dir = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\post-submision minor review\Gulf " \
           r"of Mexico Sandstone Cement Flow - NaCl brine - 2m - 10E-7 "
file_toughreact = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Crack investigation\crack " \
                  r"run\Gulf of Mexico Sandstone Cement Flow - NaCl brine - 2m - 10E-9 "
restart = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Crack investigation\crack run\Gulf " \
          r"of Mexico Sandstone Cement Flow - NaCl brine - 2m - 10E-9 - restart "


stat_test = PlotStatistics('toughreact', root_dir, filetype_toughreact_min)
stat_test.plotRegular(['Porosity', 'calcite', 'dolomite', 'portlandite'], 108)
stat_test.plotRegular(['Porosity', 'calcite', 'dolomite', 'mg+2'], 108, format='all')

# root_dir = r"C:\Users\tajayi3\OneDrive - Louisiana State University"
#
# file = os.path.join(root_dir, r"tmvoc\mymodels\paper work\one component\batch biodg")
# print(file)
#
# filetype_tmvoc = "OUTPUT_ELEME.csv"
#
# stat_test = PlotStatistics('tmvoc', file, filetype_tmvoc)
# stat_test.plotRegular(['X_Toluen_L', 'X_Toluen_N'], 0)
