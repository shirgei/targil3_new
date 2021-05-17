import pandas
from sample import  Sample

class Data:
    def __init__(self,path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        samples_lst=[]
        for i, sample in enumerate(self.data["samples"]):
            genes_lst=[]
            s_id=sample
            label=self.data["type"][i]
            for key in self.data.keys()[2:]:
                genes_lst.append(self.data[key][i])
            samples_lst.append(Sample(s_id,genes_lst,label))
        return samples_lst

    def get_genes_label(self):
         return list(set(self.data["type"]))


