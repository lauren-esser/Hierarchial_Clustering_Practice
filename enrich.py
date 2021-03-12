-enrich.py-
import pandas as pandas
import numpy as np 
import seaborn as sns 
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn import preprocessing
from scipy.stats import norm




Class Enrich(Common):
    """
    USEAGE: This script is responsible for Hierarchial Clustering feature transformation.
            Enriched data will be stored in the ./cache directory.
    """

    #is init only used when adding new information? ex adding name =. Why do we need it for this?
    def __init__(self):
        pass
    
    def test_import(self):
        print(f'Package {__name__} imported. {self.__doc__}')

    def preprocess(self, df: pd.DataFrame:)
        #set id to index
        df = df.set_index(['Id'])

        #checks
        print(df.info())
        print(df.describe())
        print(df.isna().sum())
        return df
        
    def normalize_numerical(self, df: pd.DataFrame)
        #separate and normalize numerical columns using StandardScaler
        num_cols = df.select_dtypes('number')
        x = num_cols.values
        Standard_Scaler = preprocessing.StandardScaler()
        x_scaled = Standard_scaler.fit_transform(x)
        num_cols_scaled = pd.DataFrame(x_scaled, index = num_cols.index,
                                        columns = num_cols.columns)
        return num_cols_scaled
    
    def Inverse_AER(member1, member2, df: pd.DataFrame):
        """
        Takes in vector of Member1 and Member2 and returns the Inverse Absolute Error Rate
        """
        num = 0
        sum1 = 0
        sum2 = 0

        n = len(member1)
        for i in range(n):
            num = num + abs(member1[i] - member2[i])

        for i in member1:
            sum1 = sum1 + i

        for j in member2:
            sum2 = sum2 + j

        den = sum1 + sum 2

        Inverse_Error_Rate = 1 - (num/den)

        Return Inverse_Error_Rate

    def cdf(element_vector):
        """
        Takes in vector of all numeric values within the data set for the element being evaluated and returns 
        a cdf object.
        """
        output_cdf = norm.cdf(element_vector)
        return output_cdf


if __name__ == '__main__':
    """
    Local module testing workflow goes here.
    """
    print('Local test run')