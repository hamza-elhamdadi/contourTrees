
var filter_list = [ "median", "min", "max", "gaussian", "savitzky_golay", "mean", "cutoff", "butterworth", "chebyshev", "subsample", "rdp", "tda" ];

var filter_groups = [
    {"title": "Rank Filters", "filters": [ "median", "min", "max"] },
    {"title": "Convolutional Filters", "filters": ["gaussian", "savitzky_golay", "mean"] },
    {"title": "Freq. Domain Filters", "filters": ["cutoff", "butterworth", "chebyshev"] },
    {"title": "Subsampling", "filters": ["subsample", "tda", "rdp" ] }
];

var filter_short_names = {
    "median": "median",
    "gaussian": "Gaussian",
    "cutoff": "cutoff",
    "subsample": "uniform",
    "rdp": "Douglas-Peucker",
    "tda": "topology",
    "butterworth": "Butterworth",
    "chebyshev": "Chebyshev",
    "max": "max",
    "min": "min",
    "mean": "mean",
    "savitzky_golay": "Savitzky-Golay",
    "median_hollow": "median",
    "gaussian_hollow": "Gaussian",
    "cutoff_hollow": "cutoff",
    "subsample_hollow": "uniform",
    "rdp_hollow": "Douglas-Peucker",
    "tda_hollow": "topology",
    "butterworth_hollow": "Butterworth",
    "chebyshev_hollow": "Chebyshev",
    "max_hollow": "max",
    "min_hollow": "min",
    "mean_hollow": "mean",
    "savitzky_golay_hollow": "Savitzky-Golay"
};

var filter_long_names = {
    "median": "median",
    "gaussian": "Gaussian",
    "cutoff": "low-pass cutoff",
    "subsample": "uniform subsampling",
    "rdp": "Douglas-Peucker",
    "tda": "topology",
    "butterworth": "Butterworth",
    "chebyshev": "Chebyshev",
    "max": "max",
    "min": "min",
    "mean": "mean",
    "savitzky_golay": "Savitzky-Golay"
};

var metric_names = ['pearson cc', 'spearman rc', 'L1 norm', 'Linf norm', 'delta volume',
                    'frequency preservation', 'peak bottleneck', 'peak wasserstein'];

var metric_math_name = {'pearson cc': ["\u03C1",''],
                        'spearman rc': ['r','s'],
                        'L1 norm': ['\u2113\u2081',''],
                        'Linf norm': ['\u2113','\u221E'],
                        'delta volume': ["\u03B4a",''],
                        'frequency preservation': ["\u2131",''],
                        'peak wasserstein': ['W\u2081',''],
                        'peak bottleneck': ['W','\u221E'] };

var task_titles = { 'task_retrieve': ["Retrieve Value (average case): L<sup>1</sup>-norm", "Retrieve Value (worst case): L<sup>&#8734;</sup>-norm" ],
                        'task_range' : ["Determine Range (average case): L<sup>1</sup>-norm", "Determine Range (worst case): L<sup>&#8734;</sup>-norm" ],
                        'task_extrema' : ["Find Extrema (average case): Wasserstein", "Find Extrema (worst case): Bottleneck"],
                        'task_anomalies' : ["Find Anomalies (average case): Wasserstein", "Find Anomalies (worst case): Bottleneck"],
                        'task_derive' : ["Compute Derived Value (average case): Volume Preservation", "" ],
                        'task_characterize' : ["Characterize Distribution (average case): Frequency Preservation", ""],
                        'task_cluster_trends' : ["Cluster: Trends (average case): Frequency Preservation", ""],
                        'task_sort' : ["Sort: Pearson Correlation", "Sort: Spearman Rank Correlation"],
                        'task_cluster_points' : ["Cluster: Points: Pearson Correlation", "Cluster: Points: Spearman Rank Correlation"] };

                        

function insert_filter_selector(){
    html = `<div class="form-group">
                <label for="filter">Filter Type</label>
                <select class="form-control form-control-sm" id="filter" name="filter" onchange="changeFilter();">`;

    filter_list.forEach( function(key){
        selected = key==='tda' ? "selected": ""
        html += '<option value="' + key + '" ' + selected + '>' + filter_long_names[key] + '</option>';
    });
    html += '</select></div>';
    document.write(html);
}

