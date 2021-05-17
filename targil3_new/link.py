from sample import Sample
from cluster import Cluster

class Link:

    def compute(self, cluster, other):
        raise NotImplemented("subclass must implement abstract method")

class SingleLink(Link):
    def compute(self, cluster, other):
        #print(cluster.get_samples()[0])
        min_distance = cluster.get_samples()[0].compute_euclidean_distance(other.get_samples()[0])
        for cluster_sample in cluster.get_samples():
            for other_sample in other.get_samples():
                temp_distance = other_sample.compute_euclidean_distance(cluster_sample)
                if temp_distance < min_distance:
                    min_distance = temp_distance
        return min_distance

class CompleteLink(Link):
    def compute(self, cluster, other):
        max_distance = 0
        for cluster_sample in cluster.get_samples():
            for other_sample in other.get_samples():
                temp_distance = other_sample.compute_euclidean_distance(cluster_sample)
                if temp_distance > max_distance:
                    max_distance = temp_distance
        return max_distance
