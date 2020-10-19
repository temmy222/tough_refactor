from fileparser.experiment import Experiment
from fileparser.fileread import FileReadSingle, FileReadMultiple
from fileparser.tough3 import Tough3
from fileparser.toughreact import ToughReact, MultiToughReact
from plotting.plotmultifiles import PlotMultiFiles
from plotting.plotmultitough import PlotMultiTough
from plotting.plottough import PlotTough
import os

loca6 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same high cond"
loca7 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same high cond - longer time"
loca8 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same high cond - longer time"
loca9 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same high cond - longer time"

loca10 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same low cond  - longer time"
loca11 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same low cond - longer time"
loca12 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same low cond  - longer time"
loca13 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same low cond"

loca85 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Offshore"
loca86 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
loca87 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Na acetate brine"
loca88 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - NaCl brine"

loca28 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca29 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca30 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca31 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca101 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - shorter time"
loca102 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer time3"

loca99 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - shorter time"
loca100 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time3"

loca25 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore"
loca26 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - larger"
loca26b = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - muchlar"
loca27 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - smaller"

loca109 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\same RSA\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - order higher"
loca110 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\same RSA\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - order lower"

loca35 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"
loca37 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca38 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca39 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca40 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca41 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca64 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Offshore"
loca65 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
loca66 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Na acetate brine"
loca67 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - NaCl brine"

loca68 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - Ca injected brine Offshore"
loca69 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - Ca injected brine Onshore"
loca70 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - Na acetate brine"
loca71 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - NaCl brine"

loca111 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore"
loca112 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer grid"
loca113 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer grid2"

params2 = ['pH', 't_h2o', 't_h+', 't_na+']
params_min = ['gypsum', 'ettringite', 'calcite', 'Porosity']
param3 = ['portlandite', 'calcite', 'jennite', 'monosulfoalu']
param5 = ['katoitesi1', 'c3fh6', 'tobermorite(', 'hydrotalcite']
param6 = ['brucite', 'chalcedony', 'dolomite', 'pH']
filetype_toughreact = 'kdd_conc.tec'
filetype_toughreact_min = 'kdd_min.tec'
params2 = ['pH', 't_h+', 't_na+']

# legend = ['Ca Offshore (Case 4)', 'Ca Onshore (Case 3)', 'Na acetate (Case 2)', 'NaCl (Case 1)']
# legend = ['1.53E-7 m$^3$/day', '1.53E-5 m$^3$/day (base case)', '1.53E-3 m$^3$/day']
# legend = ['$1.65E-11 m^{2}/s$', '$1.65E-10 m^{2}/s$ (base case)', '$1.65E-9 m^{2}/s$', '$1.65E-5 m^{2}/s$']
# legend = ['Closed boundary', 'Open boundary (base case)']
# legend = ['RSA-1 (higher order of magnitude)', 'RSA (base case)', 'RSA-2 (lower order of magnitude)']
legend = ['gypsum', 'ettringite', 'calcite', 'Porosity']
# legend = ['125 grid blocks', '625 grid blocks', '1000 grid blocks']

title = ['Ca Offshore (Case 4)', 'Ca Onshore (Case 3)', 'Na acetate (Case 2)', 'NaCl (Case 1)']

all_toughreact_files = [loca38, loca39, loca40, loca41]
all_toughreact_filetypes = [filetype_toughreact, filetype_toughreact, filetype_toughreact, filetype_toughreact]
all_toughreact_filetypes_min = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min]
all_toughreact_filetypes_min_chem = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min,
                                     filetype_toughreact]

# testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, params2)
testcodemultitoughreact_min = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes_min,
                                               params_min, per_file=True, title=title)
# testcodemultitoughreact_min_chem = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes_min_chem,
#                                                param6)

param_min = ['portlandite', 'calcite']

# testcodetoughreact = FileReadSingle("toughreact", loca88, filetype_toughreact)
# testcodetoughreact_min = FileReadSingle("toughreact", loca88, filetype_toughreact_min)

# testcodetoughreact.plot2D('x', 'z', 'pH', 2.592e+25, 'plain')
# testcodemultitoughreact.plotTime(106, legend)
# testcodetoughreact_min.plotTime(param3, 106, format_of_date='year')

# testcodemultitoughreact_min.plotParamWithLayer('X', 'Z', 4, 2.592e+15, legend)
testcodemultitoughreact_min.plotTime(106, legend)

# tough_data = ToughReact("toughreact", loca68, 'kdd_min.tec')
# x_data = tough_data.get_unique_coord_data('Z', 2.592e+15)
# print(x_data)
# result_data = tough_data.getLayerData('Z', 4, 1.71310257E+07, 'calcite')
# print(result_data)
