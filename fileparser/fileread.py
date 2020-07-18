import os

from fileparser.TMVOC import TMVOC



class FileRead(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        """

        :type simulatortype: object
        """
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle +  ' for ' + self.simulatortype

    def read_file(self):
         if self.simulatortype.lower()=="tmvoc":
             tmvoc = Toughtest3( self.simulatortype, self.filelocation, self.filetitle)

