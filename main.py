import sys
from data import Data
from agglomerativeClustering import AgglomerativeClustering
from link import SingleLink, CompleteLink

def main(argv):
    data = Data(argv[1])
    link = SingleLink()
    agglomerative_clustering = AgglomerativeClustering(link, data.create_samples())
    agglomerative_clustering.run(7)


if __name__ == '__main__':
    main(sys.argv)


