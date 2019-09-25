#!/usr/bin/python -tt
"""
Created on 23/09/2019

@author: adeacon
"""
import os
import src.utilities as utilities


class Test:

    def setup_method(self, test_method):
        '''remove temp dir containing dummy html and csv'''
        # configure self.attribute
        try:
            os.remove('tests/temp/dummy.html')
        except:
            pass

        try:
            os.rmdir("tests/temp")
        except:
            pass

        os.mkdir("tests/temp")

        with open('tests/temp/dummy.html','w') as f:
            message = """<html>
            <head></head>
            <body><p>Hello World!</p></body>
            </html>"""

            f.write(message)
            f.close()


    def teardown_method(self, test_method):
        '''remove temp dir containing dummy html and csv'''
        # tear down self.attribute
        os.remove('tests/temp/dummy.html')
        os.rmdir("tests/temp")
        

    # # test returns first line of dummy csv file
    # def read_header(filepath):
    #     with open(filepath, "rb") as f:
    #         reader = csv.reader(f)
    #         i = reader.next()
    #         i = filter(None, i)
    #         # print i
    #         return i


    def test_make_soup(url):
        assert utilities.make_soup('file://tests/temp/dummy.html') == """<html>
            <head></head>
            <body><p>Hello World!</p></body>
            </html>"""


    def test_ensure_dir(self):
        assert utilities.ensure_dir('tests/temp/dummy.html') == 0


    def test_master_path(self):
        assert "mydir" + os.sep + "ftb_test.txt" == utilities.master_path("test", directory="mydir")


    # # test return dummy dataframe from dummy csv
    # def get_master(stub):
    #     # print "Fetching "+master_path(stub)
    #     return pd.read_csv(master_path(stub), encoding = "utf8", sep='|')


    # # test save dummy dataframe to dummy csv
    # def save_master(dframe, stub, enc='utf-8'):
    #     dframe.to_csv(master_path(stub), encoding=enc, sep='|')
    #     # dframe.to_csv(master_path(stub), sep='|')
    #     # print "... saved to "+master_path(stub)