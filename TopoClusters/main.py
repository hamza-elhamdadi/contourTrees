import matplotlib.image as mpimg, os, sys, numpy as np
import TopoClusterPerception.ClusterModels as ClusterModels
from tabulate import tabulate
from cv2 import imread

from hera_tda import BottleneckDistance as bdist, WassersteinDistance as wdist


def generate_persistence_diagram(histogram_res_x,histogram_res_y,img_name):

    # Set grid resolution
    res = [histogram_res_x, histogram_res_y]

    # Read Images
    img = mpimg.imread(img_name)

    # Build histograms
    bins = ClusterModels.histogram(img, res)

    # Build model
    mt = ClusterModels.density_model(bins)
    #print( json.dumps( mt.mt.h0, indent=2) )

    # Return the persistence diagram of the merge tree
    return mt.get_persistence_diagram()

if __name__ == '__main__1':
    np.set_printoptions(threshold=sys.maxsize)
    filepath = './datasets/dataset1/50/saliency_maps/grayscale/hierarchical_social_data1_50_grayscale.jpg'
    img = imread(filepath)
    print(img[9])


if __name__ == '__main__':
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 250
    typ = sys.argv[2] if len(sys.argv) > 2 else ''

    output = []
    datanums = [1,4,3]

    for dset in ['dataset1','dataset2','dataset3']:
        if dset != 'dataset1':
            output.append(['','','',''])
        subfolder = 'saliency_maps' if typ == 'saliency' else 'samples'
        filetype = 'png' if typ == 'saliency' else 'jpg'
        folder = f'./datasets/{dset}/{size}/saliency_maps/grayscale/'
        datanum = datanums[int(dset[-1])-1]
        default = generate_persistence_diagram(30,30,f'./datasets/{dset}/social_data{datanum}_heatmap.png')

        for file in sorted(os.listdir(folder)):
            if file.endswith('.jpg') or file.endswith('.png'):
                output.append([dset, file.split('social')[0], round(wdist(default,generate_persistence_diagram(15,15,folder+file),2),2)])

    print(tabulate(output,headers=['dataset','sampling method', 'wasserstein distance',]))