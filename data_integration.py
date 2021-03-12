#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shared import Common
from data.db import Sql
import pandas as pd

class DataIntegration(Common):
    """
    USAGE: This script is responsible for acquiring data from the source repository
        via SQL or reading in files. Store integrated data in the ./cache directory;
        versioned by date.
    """

    def __init__(self):
        pass

    def test_import(self):
        print(f'Package {__name__} imported. {self.__doc__}')

    def connect_to_sql(self, env):
        # initialize the Sql object
        if env not in ['DEV', 'STAGE', 'PROD']:
            raise AssertionError(f'Must provide a valid DB environment variable. {env} provided.')
        sql = Sql(env)

        # EX. get list of categories in colX, eg ['hr', 'finance', 'tech', 'c_suite']
        # categories = list(sql.manual("SELECT colX AS 'category' FROM generic_jan GROUP BY colX", response=True)['category'])

    def import_demo_data(self, file: str) -> pd.DataFrame:
        demoDf = pd.read_csv(file)
        return demoDf

if __name__ == '__main__':
    """
    Local module testing workflow goes here.
    """
    print('Local test run')

    di = DataIntegration()
    myDf = di.import_demo_data('./cache/demo_bank_data_3_5_2021.csv')

    print(myDf.head())
    print(list(myDf.columns))