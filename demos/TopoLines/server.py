import json
import webbrowser
import time

from flask import Flask
from flask import request
from flask import send_file
from flask import send_from_directory

import lcsmooth.smoothing as lc_smooth
import lcsmooth.measures as lc_measures


app = Flask(__name__)


@app.route('/')
def render_index():
    return send_file('docs/index.html')


@app.route('/<path:path>')
def send_static_html(path):
    return send_from_directory('docs/', path)


@app.errorhandler(404)
def page_not_found(error_msg):
    print("Error: " + str(error_msg))
    return 'This page does not exist', 404


@app.route('/generate', methods=['GET', 'POST'])
def generate_smoothing():
    filter = request.args["filter"]
    level = float(request.args["level"])
    input_signal = request.json
    res = process_smoothing(input_signal, filter, level)

    return app.response_class(
            response=json.dumps(res),
            status=200
        )    



def process_smoothing(input_signal, filter_name, filter_level):

    start = time.time()
    if filter_name == 'mean':
        output_signal = lc_smooth.mean(input_signal, filter_level)
    elif filter_name == 'min':
        output_signal = lc_smooth.min_filter(input_signal, filter_level)
    elif filter_name == 'max':
        output_signal = lc_smooth.max_filter(input_signal, filter_level)
    elif filter_name == 'gaussian':
        output_signal = lc_smooth.gaussian(input_signal, filter_level)
    elif filter_name == 'median':
        output_signal = lc_smooth.median(input_signal, filter_level)
    elif filter_name == 'savitzky_golay':
        output_signal = lc_smooth.savitzky_golay(input_signal, filter_level, 2)
    elif filter_name == 'cutoff':
        output_signal = lc_smooth.cutoff(input_signal, filter_level)
    elif filter_name == 'butterworth':
        output_signal = lc_smooth.butterworth(input_signal, filter_level, 2)
    elif filter_name == 'chebyshev':
        output_signal = lc_smooth.chebyshev(input_signal, filter_level, 2, 0.001)
    elif filter_name == 'subsample':
        output_signal = lc_smooth.subsample(input_signal, filter_level)
    elif filter_name == 'tda':
        output_signal = lc_smooth.tda(input_signal, filter_level)
    elif filter_name == 'rdp':
        output_signal = lc_smooth.rdp(input_signal, filter_level)
    else:
        output_signal = input_signal
    end = time.time()

    info = {"processing time": end - start,
            "filter level": filter_level,
            "filter name": filter_name}

    res_stats = lc_measures.get_stats(output_signal)
    metrics = lc_measures.get_metrics(input_signal, output_signal)

    return {'input': list(enumerate(input_signal)), 'output': list(enumerate(output_signal)), 'stats': res_stats, 'info': info,
            'metrics': metrics}


if __name__ == '__main__':
    webbrowser.open_new_tab("http://localhost:5300")
    app.run(host='0.0.0.0', port=5300)
