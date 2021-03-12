#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mediator_interface import MediatorInterface
from data import DataIntegration as di
from model import Enrich as en, Model as mod, Measure as eval
from shared import Utilities as util

class Mediator(MediatorInterface):

    def __init__(self):
        pass

    @staticmethod
    def enforce_interface():
        """Interface enforcement called upon instance creation"""
        print('**Checking interface rules**')
        med = Mediator()
        print('Interface rules check out. Proceeding.\n')
        del med

    @staticmethod
    def test_import_workflow():
        ## test DS classes ##
        print('**Testing standard package imports**')
        di().test_import()
        en().test_import()
        mod().test_import()

        ## test common core inheritance ##
        print('**Testing common inheritance**')
        print(f'Common static vars: {di.CONST}')
        di.test_inherit()

        ## test utilities ##
        print('**Testing access to shared utilities**')
        print(f'Utility static vars: {util.CONST}')
        util.test_utility()

    @staticmethod
    def test_db_connect():
        print('**Testing YAML import and DB connection**')
        di().connect_to_sql('DEV')


if __name__ == '__main__':
    """
    Main workflow goes here. Import appropriate packages, and implement pipeline handoffs after each method call.
    """
    # ----------------------------- #
    # Mediator.enforce_interface()
    # Mediator.test_import_workflow()
    # Mediator.test_db_connect()
    # ----------------------------- #

    # Demo logistic regression
    # Import demo bank data
    df = di().import_demo_data('./Documents/github/Hierarchial_Clustering_Practice/Iris.csv')
    print(df.head())

    # Enrich demo data
    enrich = en()
    cleanDf = enrich.preprocess(df)
    num_cols_scaled = enrich.normalize_numerical(cleanDf)


    # Pass to Model layer for recursive feature elimination
    model = mod()
    pca_df, pca_comp= model.pca(num_cols_scaled)
    model.hierarchial_clustering(pca_comp, 4)