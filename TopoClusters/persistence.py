from ripser import ripser
from tabulate import tabulate
from hera_tda import BottleneckDistance as bdist, WassersteinDistance as wdist
import os, sys, numpy as np, json, hickle as hkl

num_data_points = [50,100,250,500,1000]
methods = ['hierarchical','weighted_sampling','top_k','xsample','ysample']
vals = [1,4,3]

formattable = './datasets/dataset{}/{}/data/{}_social_data{}_{}.json'
formattable_dir = './datasets/dataset{}/persistence/'
formattable_file = '{}_persistence_{}.hkl'

def dist(point1, point2):
    return np.linalg.norm(point1-point2)

def pairwise_dist(data):
    dists = np.zeros((len(data),len(data)))
    for x in range(len(data)):
        for y in range(x,len(data)):
            distval = dist(data[x],data[y])
            dists[x,y] = distval
            dists[y,x] = distval
    return dists

if __name__ == '__main_2':
    data = [np.array([x,x]) for x in [1,2,3]]
    print(pairwise_dist(data))

if __name__ == '__main__':
    output = []
    for i in range(1,4):
        if not os.path.isdir(formattable_dir.format(i)):
            os.mkdir(formattable_dir.format(i))
        if os.path.exists(formattable_dir.format(i) + 'entire_persistence.hkl'):
            entpd = hkl.load(formattable_dir.format(i) + 'entire_persistence.hkl')
        else:
            entdata = [np.array(x[:-1]) for x in json.load(open(f'./datasets/dataset{i}.json','r'))['data']]
            entdists = pairwise_dist(entdata)
            entpd = ripser(entdists,distance_matrix=True)['dgms']
            entpd = np.concatenate((entpd[0],entpd[1]))
            hkl.dump(entpd, formattable_dir.format(i) + 'entire_persistence.hkl')

        for num_points in num_data_points:
            for method in methods:
                if not os.path.isdir(formattable_dir.format(i)):
                    os.mkdir(formattable_dir.format(i))
                if os.path.exists(formattable_dir.format(i) + formattable_file.format(method,num_points)):
                    pd = hkl.load(formattable_dir.format(i) + formattable_file.format(method,num_points))
                else:
                    filepath = f'./datasets/dataset{i}/{num_points}/data/{method}_social_data{vals[i-1]}_{num_points}.json'
                    print(filepath)
                    data = [np.array(x[:-1]) for x in json.load(open(filepath,'r'))['data']]
                    dists = pairwise_dist(data)
                    pd = ripser(dists,distance_matrix=True)['dgms']
                    pd = np.concatenate((pd[0],pd[1]))
                    #print(pd)
                    hkl.dump(pd, formattable_dir.format(i) + formattable_file.format(method,num_points))
                
                output.append([f'dataset{i}',f'{num_points}',method,wdist(pd.tolist(),entpd.tolist(),2)])
                    
                
        
    print(tabulate(output,['dataset','sample size','method','wasserstein-2 distance']))
        