import json
import shutil
# import networkx as nx
import os
import time
import random
import string
import webbrowser

from flask import Flask
from flask import request
from flask import send_file
from flask import send_from_directory

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import TopoClusterPerception.ClusterModels as ClusterModels

if os.path.exists("tmp"): shutil.rmtree("tmp")
os.mkdir("tmp")

app = Flask(__name__, static_url_path="/docs", static_folder='docs')


def generate_image(data, opacity, psize, pcount):
    img_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16)) + '.png'
    img_name = os.path.join('tmp', img_name)

    input_count = len(data['x'])
    sample_set = random.sample(range(input_count), int(input_count*pcount))

    use_x = [data['x'][i] for i in sample_set]
    use_y = [data['y'][i] for i in sample_set]

    plt.figure(figsize=(7, 7))
    ax = plt.subplot(111)
    plt.axis('off')
    # plt.scatter(data['x'], data['y'], s=psize, alpha=opacity, lw=0, color='black')
    plt.scatter(use_x, use_y, s=psize, alpha=opacity, lw=0, color='black')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([])
    plt.yticks([])
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.savefig(img_name)
    plt.close()

    return img_name


def generate_threshold_plot(histogram_res_x,histogram_res_y,img_name):

    # Set grid resolution
    res = [histogram_res_x, histogram_res_y]

    # Read Images
    time_1 = time.time_ns()
    img = mpimg.imread(img_name)

    # Build histograms
    time_2 = time.time_ns()
    bins = ClusterModels.histogram(img, res)
    mpimg.imsave(img_name + ".hist.png", bins, cmap='Greys_r')

    # Build model
    time_3 = time.time_ns()
    mt = ClusterModels.density_model(bins)
    #print( json.dumps( mt.mt.h0, indent=2) )

    # Plot the result
    time_4 = time.time_ns()
    threshold, clusters = mt.threshold_plot()
    time_5 = time.time_ns() 

    return [threshold, clusters]
    # print(threshold)   
    # print(clusters)


@app.route('/')
def send_main():
    return send_file('docs/index.html')


@app.route('/<path:path>')
def send_static(path):
    if os.path.exists('docs/' + path):
        return send_from_directory('docs', path)
    return "", 404


@app.route('/tmp/<path:path>')
def send_tmp_image(path):
    if os.path.exists('tmp/' + path):
        return send_from_directory('tmp', path)
    return "", 404


@app.route('/generate', methods=['GET', 'POST'])
def generate_image_and_threshold_plot():
    # print(request.json)
    opacity = float(request.args['popacity'])/100
    psize = int(request.args['psize'])
    pcount = float(request.args['npoints'])/100
    print(opacity, psize, pcount)
    img_name = generate_image(request.json, opacity, psize, pcount)
    threshold, clusters = generate_threshold_plot(30,30,img_name)
    return app.response_class(
            response=json.dumps({'image': img_name, 'threshold': threshold, 'clusters': clusters}),
            status=200
            # ,
            # mimetype='application/json'
        )    


# @app.route('/graph_quality', methods=['GET', 'POST'])
# def g_quality():
#     # qual_queue.put( request.json )

#     # Save the data to process later
#     b = request.json

#     try:
#         if not os.path.exists('experiments/' + b['experiment']):
#             os.mkdir('experiments/' + b['experiment'])
#     except:
#         print(" > Directory already exists")

#     if not ( os.path.exists('experiments/' + b['experiment'] + "/frame_" + str(b['frame']).zfill(5) + '.json') or os.path.exists('experiments/' + b['experiment'] + "/data_" + str(b['frame']).zfill(5) + '.json')):
#         f = 'experiments/' + b['experiment'] + "/data_" + str(b['frame']).zfill(5) + '.json'
#         with open(f, 'w') as fp:
#             json.dump(b, fp, indent=1)
#         qual_queue.put(f)

#     return app.response_class(
#         response=json.dumps({'result': 'ok'}),
#         status=200,
#         mimetype='application/json'
#     )


if __name__ == '__main__':
    webbrowser.open_new_tab("http://localhost:5250")
    app.run(host='0.0.0.0', port=5250)
