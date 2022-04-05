from fileparser.fileread import FileReadMultiple

sec = 1
min = 60 *sec
hour = 60 * min
day = 24*hour
year = 365*day

file1 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file2 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file3 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file4 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file1a = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\base\base_batch\Gulf of Mexico Cement Batch - Ca injected sand equil brine Offshore - longer time"
file2a = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\base\base_batch\Gulf of Mexico Cement Batch - Ca injected sand equil brine Onshore - longer time"
file3a = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\base\base_batch\Gulf of Mexico Cement Batch - Na acetate sand equil injected Onshore - longer time"
file4a = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\base\base_batch\Gulf of Mexico Cement Batch - NaCl sand equil brine injected Onshore - longer"

file6 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - Ca injected sand equil brine Offshore - longer time"
file7 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - Ca injected sand equil brine Onshore - longer time"
file8 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - Na acetate sand equil injected Onshore - longer time"
file9 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - NaCl sand equil brine injected Onshore - longer"

file10 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file11 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file12 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file13 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file14 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file15 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file16 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file17 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file18 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file19 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file20 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file21 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file22 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite1\Gulf of Mexico Cement Batch - Ca injected sand equil brine Offshore - longer time"
file23 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite1\Gulf of Mexico Cement Batch - Ca injected sand equil brine Onshore - longer time"
file24 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite1\Gulf of Mexico Cement Batch - Na acetate sand equil injected Onshore - longer time"
file25 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite1\Gulf of Mexico Cement Batch - NaCl sand equil brine injected Onshore - longer"

file26 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite2\Gulf of Mexico Cement Batch - Ca injected sand equil brine Offshore - longer time"
file27 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite2\Gulf of Mexico Cement Batch - Ca injected sand equil brine Onshore - longer time"
file28 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite2\Gulf of Mexico Cement Batch - Na acetate sand equil injected Onshore - longer time"
file29 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite2\Gulf of Mexico Cement Batch - NaCl sand equil brine injected Onshore - longer"

file30 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite3\Gulf of Mexico Cement Batch - Ca injected sand equil brine Offshore - longer time"
file31 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite3\Gulf of Mexico Cement Batch - Ca injected sand equil brine Onshore - longer time"
file32 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite3\Gulf of Mexico Cement Batch - Na acetate sand equil injected Onshore - longer time"
file33 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite3\Gulf of Mexico Cement Batch - NaCl sand equil brine injected Onshore - longer"

file34 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime1\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file35 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime1\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file36 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime1\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file37 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime1\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file38 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime2\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file39 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime2\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file40 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime2\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file41 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime2\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file42 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime3\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file43 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime3\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file44 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime3\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file45 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\analcime3\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

all_toughreact_files = [file18, file1]
all_toughreact_files2 = [file19, file2]
all_toughreact_files3 = [file20, file3]
all_toughreact_files4 = [file42,file1a]

param_min = ['calcite', 'portlandite', 'Porosity', 'ettringite']

legend = ['New Material - Analcime 3%' ,'Status quo']

filetype_toughreact_min = 'kdd_min.tec'
all_toughreact_filetypes = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min]

joint = dict(zip(param_min, all_toughreact_filetypes))

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files4, all_toughreact_filetypes, param_min , x_slice_value=1000)
testcodemultitoughreact.plotTimePerPanelSingle(0,joint,legend,format_of_date='year')

print('correct')