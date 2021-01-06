from gensim.models import LdaModel
from gensim.corpora import Dictionary

import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering


def main():

    # Load a pretrained model from disk.
    lda = LdaModel.load("RC_LDA_50_True.lda")

    # Load pre-determined topic names
    dictionary = ["Marijuana vs\nalcohol/tobacco","UNCLEAR/JUNK","Hemp growing",
    "Party politics", "Quantity (mass,time,fine)","UNCLEAR/JUNK",
    "Government & Systemic Power","Organized crime","Federal legalization",
    "Marijuana in the media","Marijuana and crime","Legal Marijuana Market",
    "Relation to hard drugs\nand hallucinogens","Reasons for legalization",
    "State-level legalization","Police car search","Medicinal Marijuana",
    "Marijuana Plant Contents","International + Employment",
    "FDA Schedule Classification","UNCLEAR/JUNK","President and\nInternational Affairs",
    "Use and family","Canada and Housing Prices","User stereotypes",
    "Private Industry","West Coast + Supplements","International","Police house search",
    "Legal procedures","UNCLEAR/JUNK","Reddit","UNCLEAR/JUNK","UNCLEAR/JUNK",
    "Legal cases","Drug Testing","UNCLEAR/JUNK","Individual punishment",
    "Legalization as\nan electoral issue","Local delivery","Local legislatures",
    "Research about effects","Driving Drunk/High","Racial Disparities",
    "Court processes in cases","Effects of Smoking\nMarijuana/Tobacco/E-Cig",
    "Edible Foods/Mixed","Reliability of Enforcement","Gun Control","Expletives"]

    # Get the topic-word probability distributions
    distribution = lda.get_topics()

    # Remove predetermined junk topics
    remove_index = np.array([1, 5, 18, 20, 21, 23, 26, 27, 30, 31, 32, 33, 36, 39, 46])

    track_array = np.arange(50) # track array

    # Remove the junk topic distributions from the matrix
    for i in range(len(remove_index)):
        current_index = remove_index[len(remove_index) - i - 1]
        distribution = np.delete(distribution, current_index, 0)
        track_array = np.delete(track_array, current_index, 0)

    # Apply Agglomerative Clustering to the topic-word distributions
    # NOTE: setting distance_threshold=0 ensures we compute the full tree.
    model = AgglomerativeClustering(distance_threshold=0, n_clusters=None, affinity="l1", linkage="complete")

    # train
    model.fit(distribution)

    # plot
    plt.title('Hierarchical Clustering Dendrogram of Topics in Marijuana Legalization Reddit Discourse')

    # plot the dendrogram
    plot_dendrogram(model, truncate_mode='level', p=100, leaf_label_func=(lambda id: dictionary[track_array[id]]),
                    leaf_rotation=90)
    plt.xlabel("Topic title",fontsize=16)
    plt.ylabel("Regularized Euclidean Distance",fontsize=16)
    plt.xticks(fontsize=11)
    plt.tight_layout()
    plt.show()

# function to create linkage matrix and then plot the dendrogram
def plot_dendrogram(model, **kwargs):

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    # create the linkage matrix
    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the dendrogram
    dendrogram(linkage_matrix, **kwargs)

# run the code
if __name__ == "__main__":
    main()
