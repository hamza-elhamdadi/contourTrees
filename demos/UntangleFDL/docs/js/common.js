

////////////////////////////////////////////////////////////////////////////////////
//////
////// Navigation Helpers
//////
////////////////////////////////////////////////////////////////////////////////////
var pages = [{page: 'layout_figures.html', title: 'Initial Layout Figures'},
                {page: 'large_figures.html', title: 'Large Data Figures'},
                {page: 'h1_figures.html', title: 'H1 Feature Figures'},
                {page: 'other_algos.html', title: 'Other Algorithms'}]


function insert_navbar( curpage ){
    html = `<nav class="navbar navbar-expand-lg navbar-light bg-light">
              <div class="container-fluid">
                <a class="navbar-brand" href="index.html">Untangling FDL</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav me-auto mb-2 mb-lg-0">`

    pages.forEach(function(p){
        html += '<li class="nav-item">'
        if( curpage === p.page ){
            html += '<a class="nav-link active" aria-current="page" href="' + p.page + '">' + p.title + '</a>'
        }
        else{
            html += '<a class="nav-link" href="' + p.page + '">' + p.title + '</a>'
        }
        html += '</li>'
    });

     html += `</ul>
                    </div>
                  </div>
                </nav>`

    document.write(html);
}


////////////////////////////////////////////////////////////////////////////////////
//////
////// Download Helpers
//////
////////////////////////////////////////////////////////////////////////////////////
function downloadText(text, filename) {
    var a = document.createElement('a');
    a.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    a.setAttribute('download', filename);
    a.click()
}

function downloadJson(obj, filename) {
    downloadText(JSON.stringify(obj), filename);
}

function downloadSVG( plotID, filename=null ){
    if(filename ===null) filename = plotID + ".svg"
    let svgData = $("#"+plotID)[0].outerHTML;
    let svgBlob = new Blob([svgData], {type:"image/svg+xml;charset=utf-8"});
    let svgUrl = URL.createObjectURL(svgBlob);
    let downloadLink = document.createElement("a");
    downloadLink.href = svgUrl;
    downloadLink.download = filename
    downloadLink.click();
}



////////////////////////////////////////////////////////////////////////////////////
//////
////// Coloring Helpers
//////
////////////////////////////////////////////////////////////////////////////////////
let grp_colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896',
                '#9467bd', '#c5b0d5', '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7',
                '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

//let deg_color = (t)=>{ return d3.interpolateYlOrRd( t<0 ? 0 : ( t>1 ? 0.7 : t*0.7 ) ) }
let deg_color = (t)=>{ return d3.interpolatePlasma( t<0 ? 0.85 : ( t>1 ? 0 : (1-t)*0.85 ) ) }


function update_graph_draw_colors( graph_draw, color_by_group, color_by_degree, color_by_degree_ranked ){

    let graph = graph_draw.graph()
    let degree_range = [0,0]

    if( color_by_degree ) degree_range = d3.extent( graph.nodes, n => n.degree )
    if( color_by_degree_ranked ) degree_range = d3.extent( graph.nodes, n => n.degreeRank )

    if(degree_range[0] === degree_range[1]){
        degree_range[0] -= 1
        degree_range[1] += 1
    }

    graph_draw.setNodeFill( (d)=>{
        if( color_by_group && 'group' in d ) return grp_colors[d.group%grp_colors.length]
        if( color_by_degree || !('group' in d) ) return deg_color((d.degree-degree_range[0])/(degree_range[1]-degree_range[0]))
        if( color_by_degree_ranked || !('group' in d) ) return deg_color((d.degreeRank-degree_range[0])/(degree_range[1]-degree_range[0]))
        return 'black'
    })

    graph_draw.setNodeStroke( (d)=>{
        if( color_by_group && 'group' in d ) return "white"
        if( color_by_degree || color_by_degree_ranked || !('group' in d) ) return "#666"
        return 'black'
    })
}



////////////////////////////////////////////////////////////////////////////////////
//////
////// Naming Helpers
//////
////////////////////////////////////////////////////////////////////////////////////
let layouts = ["random","layered_layout","radial_layout"]
let stat_fields = ['lcmc_q_local', 'trustworthy_q_local', 'continuity_q_local', 'crossing', 'crossingAngle', 'angularResolutionMin']
let stat_names ={ crossing: "Edge Crossings", crossingAngle: "Crossing Angle", angularResolutionMin: "Minimum Angular Resolution",
                        trustworthy_q_local: "Trustworthiness", continuity_q_local: "Continuity", lcmc_q_local: "LCMC"}

let proper_names = {'random': "Random Layout (conventional)",
                    "layered_layout": "Layered Layout (our approach)",
                    'radial_layout': "Radial Layout (our approach)",
                    "Maximum Motion": "Maximum Displacement",
                    "Average Motion": "Average Displacement",
                    "Angular resolution (min)": "Minimum Angular Resolution"}

function get_proper_name( v ){
    if( v in proper_names ) return proper_names[v]
    if( v in stat_names ) return stat_names[v]
    return v
}





////////////////////////////////////////////////////////////////////////////////////
//////
////// Misc Helpers
//////
////////////////////////////////////////////////////////////////////////////////////

// Helper function to bring a selcted object to the front of the display
d3.selection.prototype.moveToFront = function() {
  return this.each(function(){
    this.parentNode.appendChild(this);
  });
};



