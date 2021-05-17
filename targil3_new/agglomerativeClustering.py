from cluster import Cluster
from link import SingleLink, CompleteLink
from sample import Sample

class AgglomerativeClustering:
    def __init__(self,link, samples):
        self.link = link
        self.cluster_lst = []
        self.samples = samples
        for sample in samples:
            new_cluster = Cluster([sample], sample.get_s_id())
            self.cluster_lst.append(new_cluster)

    def in_xi(self,sample,cluster,cluster_size):
        sum = 0
        for cur_sample in cluster.get_samples():
            if sample.get_s_id() != cur_sample.get_s_id():
                sum += cur_sample.compute_euclidean_distance(sample)
        return sum/(cluster_size-1)

    def out_xi(self,sample,cluster):
        min = 0
        first = True
        for cur_cluster in self.cluster_lst:
            sum = 0
            if cur_cluster.get_c_id() != cluster.get_c_id():
                for temp_sample in cur_cluster.get_samples():
                    sum += temp_sample.compute_euclidean_distance(sample)
            cluster_size = len(cur_cluster.get_samples())
            temp_distance = sum/cluster_size
            if first:
                min=temp_distance
                first=False
            if min > temp_distance:
                min = temp_distance
        return min

    def calculate_silhoeutte(self,cluster,sample):
        cluster_size = len(cluster.get_samples())
        if cluster_size <= 1:
            return 0
        in_xi = self.in_xi(sample,cluster,cluster_size)
        out_xi = self.out_xi(sample,cluster)
        return (out_xi-in_xi)/max(in_xi,out_xi)

    def compute_silhoeutte(self):
        silhoeutte_dic = {}
        s_id_keys = []
        for sample in self.samples:
            s_id_keys.append(sample.get_s_id())
        for key in s_id_keys:
            silhoeutte_dic.setdefault(key, 0)
        for cur_cluster in self.cluster_lst:
            for cur_sample in cur_cluster.get_samples():
                silhoeutte_dic[cur_sample.get_s_id()] = self.calculate_silhoeutte(cur_cluster, cur_sample)
        return silhoeutte_dic

    def calculate_cluster_silhoeutte(self,cluster):
        cluster_size = len(cluster.get_samples())
        return self.sum_silhoeutte(cluster)/cluster_size

    def sum_silhoeutte(self,cluster):
        silhoeutte_dic = self.compute_silhoeutte()
        s_id_lst = []
        for sample in cluster.get_samples():
            s_id_lst.append(sample.get_s_id())
        sum = 0
        for id in s_id_lst:
            sum += silhoeutte_dic[id]
        return sum

    def calculate_sample_silhoeutte(self):
        sum=0
        for cluster in self.cluster_lst:
            sum+=self.sum_silhoeutte(cluster)
        sample_size=len(self.samples)
        return sum/sample_size


    def compute_summery_silhoeutte(self):
        silhoeutte_cluster_dic = {}
        for cluster in self.cluster_lst:
            silhoeutte_cluster_dic.setdefault(cluster.get_c_id(), self.calculate_cluster_silhoeutte(cluster))
        silhoeutte_cluster_dic[0] = self.calculate_sample_silhoeutte()
        return silhoeutte_cluster_dic

    def run(self, max_clusters):
        first = True
        min_distance = 0
        while len(self.cluster_lst) > max_clusters:
            for cluster in self.cluster_lst:
                for other in self.cluster_lst:
                    if cluster.get_c_id() != other.get_c_id():
                        temp_distance = self.link.compute(cluster,other)
                        if first:
                            min_distance = temp_distance
                            first = False
                            cluster1 = cluster
                            cluster2 = other
                        if temp_distance < min_distance:
                            min_distance = temp_distance
                            cluster1 = cluster
                            cluster2 = other
            cluster1.merge(cluster2)
        silhoeutte_dic = self.compute_summery_silhoeutte()
        print(len(self.cluster_lst))
        for cluster in self.cluster_lst:
            silhoeutte = silhoeutte_dic[cluster.get_c_id()]
            cluster.print_details(silhoeutte)



