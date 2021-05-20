import sys
from data import Data
from agglomerativeClustering import AgglomerativeClustering
from link import SingleLink, CompleteLink
from test import Cat


def main(argv):
    cat1= Cat()
    cat2=Cat()
    lst=[cat1,cat2]
    del cat1
    print(lst)
    print(len(lst))


    data = Data(argv[1])
    link = SingleLink()
    agglomerative_clustering = AgglomerativeClustering(link ,data.create_samples())
    agglomerative_clustering.run(7)



if __name__ == '__main__':
    main(sys.argv)


