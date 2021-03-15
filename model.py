#hierarchial clustering libraries
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as shc
from scipy.spatial.distance import euclidean
from scipy.cluster.hierarchy import dendrogram,linkage
from sklearn.cluster import AgglomerativeClustering 

class Model(Common):
    """
    USEAGE: This script is used to create the Hierarchial Model.
    """

    def __init__(self):
        pass

    def test_import(self):
        print(f'Package {__name__} imported. {self.__doc__}')

    def pca(self, num_cols_scaled):
        #create pca dataframe
        pca = PCA()
        pca_comp= pca.fit_transform(num_cols_scaled)
        print('PCA Components: ', pca.components_)
        print('Expalined Variance Ratio: ', pca.explained_variance_ratio_)
        print('Singular Values: ', pca.singular_values_)
        pca_df = pd.DataFrame(pca_comp, columns = ['PCA1','PCA2', 'PCA3', 'PCA4'])

        ### any visuals we will want to save to a file. 

        #PCA visuals -> comparing pca 1 and 2
        fig = plt.figure(figsize = (12, 8))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_title('Plot of 1st and 2nd Principal Components')
        ax.scatter(pca_comp[:, 0]
                , pca_comp[:, 1])
        ax.grid()

        #Visualize scree Plot
        df_scree = pd.DataFrame({'Variance':pca.explained_variance_ratio_,
             'Principal Components':['PC1','PC2','PC3','PC4']})
        ax = sns.barplot(x='Principal Components',y="Variance", 
           data=df_scree, color="c").set_title('Scree Plot')
        plt.show()

        #plot dengrogram
        plt.figure(figsize=(10, 7))  
        dend = shc.dendrogram(shc.linkage(pca_comp, method='ward'))
        plt.axhline(linestyle='--', y=8) 
        plt.ylabel('Euclidean Distances')
        plt.xlabel('Sample Index')
        plt.title('Iris Hierarchial Clustering Dendrogram')
        plt.show()

        return pca_df.head(), pca_comp


#save cluster as a file and then read back in for new_data
    def hierarchial_clustering(pca_comp, n_clusters):
        cluster = AgglomerativeClustering(n_clusters = n_clusters, 
                                    affinity = 'euclidean',
                                    linkage = 'ward')
        cluster.fit(pca_comp)
        labels = cluster.labels_

        #visualize clusters
        plt.figure(figsize = (12,8))
        plt.scatter(pca_comp[:,0], pca_comp[:,1], c=cluster.labels_, cmap = 'prism')
        plt.title('Clusters', fontsize = 20)
        plt.xlabel('PC1', fontsize = 18)
        plt.ylabel('PC2', fontsize = 18);

    def new_data(new_df):
        #normalize new data in the same way
        x = new_df
        Standard_scaler = preprocessing.StandardScaler()
        x_scaled = Standard_scaler.fit_transform(x)
        new_scaled = pd.DataFrame(x_scaled, index = new_df.index, 
                                    columns = new_df.columns)
        new_scaled.head()

        #assign to cluster from hierarchial clustering model
        model = cluster.fit(pca_comp)
        assigned_cluster = model.fit_predict(new_scaled)
        return assigned_cluster