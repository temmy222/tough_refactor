import csv
import os


class Experiment(object):
    def __init__(self, filelocation, filetitle):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle

    def read_file(self):
        os.chdir(self.filelocation)
        with open(self.filetitle) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            self.file_as_list = []
            for row in csv_reader:
                self.file_as_list.append(row)
        return self.file_as_list