from fileparser.fileread import FileReadSingle, FileReadMultiple

file = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch biodg"
file2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch biodg - two biomass"
file3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch no biodg"
file4 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\biodegradation"
file5 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\no biodegradation"
file6 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\biodegradation"
file7 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\no biodegradation"
filetype_tmvoc = "OUTPUT_ELEME.csv"

read_file = FileReadSingle("tmvoc", file4, filetype_tmvoc)
read_file_multi = FileReadMultiple("tmvoc", [file4, file5, file6, file7], [filetype_tmvoc, filetype_tmvoc, filetype_tmvoc, filetype_tmvoc], ['X_Toluen_L', 'X_AIR_L',  'X_Toluen_L', 'X_AIR_L'], per_file=True)
# read_file.plot2D('x', 'z', 'X_AIR_G', 39999, 'grid')
# read_file.plotTime('X_Toluen_L', 0, )
# read_file.plot2D('x', 'z', 'X_Toluen_L', 200000000, 'grid')
read_file_multi.plotTime(0, ['X_Toluen_L', 'X_AIR_L','X_Toluen_L', 'X_AIR_L'])
