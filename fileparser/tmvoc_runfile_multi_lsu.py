from fileparser.fileread import FileReadSingle, FileReadMultiple

file_tmvoc = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
             r"manual\Toluene\Toluene Ks sensitivity\High Ks "
file_tmvoc2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
              r"manual\Toluene\Toluene Ks sensitivity\Low Ks "

file_tmvoc3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
             r"manual\Benzene\Benzene Ks sensitivity\High Ks "
file_tmvoc4 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
              r"manual\Benzene\Benzene Ks sensitivity\Low Ks "

file_tmvoc5 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
              r"manual\Benzene\Benzene Uptake sensitivity\C-04 - high benzene uptake "
file_tmvoc6 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
              r"manual\Benzene\Benzene Uptake sensitivity\C-04 - low benzene uptake "

file_tmvoc7 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
              r"manual\Toluene\Toluene Uptake sensitivity\C-04 - high toluene uptake "

file_tmvoc8 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in " \
              r"manual\Toluene\Toluene Uptake sensitivity\C-04 - low toluene uptake "

# all_tmvoc_files = [file_tmvoc, file_tmvoc]
filetype_tmvoc = 'OUTPUT_ELEME.csv'

all_tmvoc_files = [file_tmvoc7, file_tmvoc8]
all_tmvoc_filetypes = [filetype_tmvoc, filetype_tmvoc]

params_tmvoc = ['X_toluen_L', 'X_BENZEN_L']
params_tmvoc_multi = ['DEN_L', 'sat_N', 'X_Toluen_L', 'X_AIR_L']

testcode3tmvoc = FileReadSingle("tmvoc", file_tmvoc, filetype_tmvoc)
testcodemultitmvoc = FileReadMultiple('tmvoc', all_tmvoc_files, all_tmvoc_filetypes, params_tmvoc)

# testcode3tmvoc.plotTime(params_tmvoc[0], 0)
testcodemultitmvoc.plotTime(0, ['High toluene uptake', 'Low toluene uptake'])
