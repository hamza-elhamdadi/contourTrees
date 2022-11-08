import matplotlib.image as mpimg, os
import TopoClusterPerception.ClusterModels as ClusterModels

def generate_persistence_diagram(histogram_res_x,histogram_res_y,img_name):

    # Set grid resolution
    res = [histogram_res_x, histogram_res_y]

    # Read Images
    img = mpimg.imread(img_name)

    # Build histograms
    bins = ClusterModels.histogram(img, res)
    mpimg.imsave(img_name + ".hist.png", bins, cmap='Greys_r')

    # Build model
    mt = ClusterModels.density_model(bins)
    #print( json.dumps( mt.mt.h0, indent=2) )

    # Return the persistence diagram of the merge tree
    return mt.get_persistence_diagram()

if __name__ == '__main__':
    folder = './images/sample_size_250/'

    for file in os.listdir(folder):
        print(generate_persistence_diagram(30,30,folder+file))
        break