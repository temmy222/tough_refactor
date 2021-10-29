from fileparser.fileread import FileReadMultiple

file1 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca " \
        r"injected sand equil brine Offshore - longer time "
file2 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\new material\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"

all_toughreact_files = [file1, file2]
param_min = ['calcite', 'portlandite', 'Porosity', 'ettringite']

legend = ['Status quo', 'New Material']

filetype_toughreact_min = 'kdd_min.tec'
all_toughreact_filetypes = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min]

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, param_min)
testcodemultitoughreact.plotTime(83, legend, plot_kind='file')

print('correct')