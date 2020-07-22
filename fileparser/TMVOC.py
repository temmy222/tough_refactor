import csv

import fileparser.tough3 as tough3


class TMVOC(tough3.Tough3):
    def __init__(self, simulatortype, filelocation, filetitle):
        super().__init__(simulatortype, filelocation, filetitle)

    # super().__init__(getfileinfo.FileRead)
