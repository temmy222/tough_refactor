from fileparser.fileread import FileReadSingle, FileReadMultiple
import os

# root_dir = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2"
root_dir = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Validation2"
# root_dir2 = r"C:\Users\tajayi3\Desktop\Valivation Restart"
root_dir3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2"

file = os.path.join(root_dir, "Cement-Anhydrite")
file_toughreact = os.path.join(root_dir, r"restart right")
file_toughreact2 = os.path.join(root_dir, r"restart right\restart1")
file_toughreact3 = os.path.join(root_dir, r"restart right\restart2")
file_toughreact4 = os.path.join(root_dir, r"restart right\restart3")
file_toughreact5 = os.path.join(root_dir, r"restart right\restart4")
file_toughreact6 = os.path.join(root_dir, r"restart right\restart5")

file_equil = os.path.join(root_dir, r"restart right\run with equilibirum")
file_equil2 = os.path.join(root_dir, r"restart right\run with equilibirum\restart1")
file_equil3 = os.path.join(root_dir, r"restart right\run with equilibirum\restart2")
file_equil4 = os.path.join(root_dir, r"restart right\run with equilibirum\restart3")

# filer = os.path.join(root_dir2, r"restart right\run with equilibirum\reduced gas injection")

# grid_sens1 = os.path.join(root_dir3, r"Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore")
# grid_sens2 = os.path.join(root_dir3,
#                           r"Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer grid")
# grid_sens3 = os.path.join(root_dir3, r"Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer "
#                                      r"grid2")

expt = os.path.join(root_dir, r"experiment")
file1 = r"C:\Users\tajayi3\Desktop\my Folders\write_to_TOUGH\RunScripts\Validate with Case4 - timestoptest"
file2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca " \
        r"injected sand equil brine Offshore - longer time "
file3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Crack investigation\crack run\Gulf " \
        r"of Mexico Sandstone Cement Flow - NaCl brine - 2m - 10E-9 - runagain "

all_toughreact_files = [file1, file2]
# all_toughreact_files = [grid_sens1, grid_sens2, grid_sens3]
legend = ['10E-7', '10E-8', '10E-9']
# all_tmvoc_files = [file_tmvoc, file_tmvoc]
filetype_tmvoc = 'OUTPUT_ELEME.csv'
filetype_toughreact = 'kdd_conc.tec'
filetype_toughreact_min = 'kdd_min.tec'
all_toughreact_filetypes = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min]
all_tmvoc_filetypes = [filetype_tmvoc, filetype_tmvoc]

params_tmvoc = ['DEN_L', 'sat_N']
params_tmvoc_multi = ['DEN_L', 'sat_N', 'X_Toluen_L', 'X_AIR_L']
params2 = ['pH', 't_na+', 't_cl-', 't_ca+2']
# params2 = ['t_mg+2', 't_cl-', 't_al+3', 't_so4-2']
params3 = ['pH', 't_h2o']
params4 = ['pH']
param_min = ['calcite', 'portlandite', 'Porosity', 'ettringite']
# param_min = ['brucite', 'dolomite', 'jennite', 'chalcedony']
labels = ['first plot', 'second plot', 'third plot', 'fourth plot']
restart_files = [file_toughreact2, file_toughreact3, file_toughreact4, file_toughreact5, file_toughreact6]
restart_files_equil = [file_equil2, file_equil3, file_equil4]
expt_file = [expt]

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, param_min)
testcodetoughreact = FileReadSingle("toughreact", file_toughreact, filetype_toughreact, restart_files=restart_files,
                                    experiment=expt_file)
# testcode2 = FileReadSingle("toughreact", filer, filetype_toughreact, experiment=expt_file)
# testcode2_min = FileReadSingle("toughreact", filer, filetype_toughreact_min, experiment=expt_file)
# test_equil = FileReadSingle("toughreact", file_equil, filetype_toughreact, restart_files=restart_files_equil,
#                             experiment=expt_file)
# test_equil_min = FileReadSingle("toughreact", file_equil, filetype_toughreact_min, restart_files=restart_files_equil,
#                                 experiment=expt_file)
testcodetoughreact_min = FileReadSingle("toughreact", file_toughreact, filetype_toughreact_min,
                                        restart_files=restart_files,
                                        experiment=expt_file)

# testcode2_min.plot2D('x', 'z', 'calcite', 2.592e+15, 'grid')
# testcode2.plot2D('x', 'z', 'pH', 0, 'grid')
# testcode2.plotTime('pH', 106, format_of_date='day')
# testcode2_min.plotTime(param_min, 106, format_of_date='day')

# testcodetoughreact_min.plot2D('x', 'z', 'calcite', 0, 'grid')
# testcodetoughreact.plotTime('pH', 106, format_of_date='day')
# testcodetoughreact.plot2D('x', 'z', 'pH', 0, 'grid')
testcodetoughreact_min.plotTime('portlandite', 106, format_of_date='day')
#
# test_equil.plotTime('pH', 106, format_of_date='day')
# test_equil_min.plotTime(param_min, 106, format_of_date='day')


# testcodemultitoughreact.plotTime(83, legend, plot_kind='file')
# testcodetoughreact_min.plotParamWithLayer('X', 'Z', param_min[0], 1, 500)


# dest1 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased
# depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore" os.chdir(dest1) filename =
# 'thddem1214r3_hs.dat'
#
# tre = Miscellaneous(dest1, filename)
# minerals = ['Gypsum', 'Ettringite', 'Friedel_Salt', 'Calcite', 'Sepiolite', 'Tobermorite(11A)', 'Jennite',
#             'Portlandite', 'Chalcedony', 'KatoiteSi1', 'Hydrotalcite', 'Dolomite']
# # minerals = ['Calcite','Portlandite']
# gases = ['CO2(g)']
# tre.plotGasK('CO2(g)')
# tre.plotMineralK('Hydrotalcite')
# tre.plotmultipleMineralK(minerals)
