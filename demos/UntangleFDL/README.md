# Persistent Homology Makes Force-Directed Layouts Better

## IEEE VIS 2021 Submission #1455


## Goal
The main purpose of our project is to use H0 and H1 persistent homology features to generate better graph layouts that bring out the characteristics of the topology that will otherwise remain hidden by the layout. We provide a topology-guided initial graph layout algorithm and interactive persistence bars that manipulate the attractive force in the visualization. Two columns of bars representing H0 and H1 features are shown on the left, and when hovered over by the mouse pointer, they highlight the corresponding persistent feature in the visualization.


## Running the demo

Open a terminal and navigate to the project directory

    % cd PH_On_Graphs

Run the webserver from the terminal window.

For Python 2, use the below command in the terminal
    
    % python -m SimpleHTTPServer 8000

For Python 3, use the below command in the terminal
    
    % python -m http.server 8000

If you can see the ' Serving HTTP on...' message in the terminal, then in the web browser, open
    "http://localhost:8000"    

* A different port can also be used just by replacing 8000 in the above commands.


 ## Implementation and Interaction
 
We used D3 and JavaScript to implement the visualizations.  The web page provides the user with an option of choosing different datasets from the drop-down provided. The selected dataset will be visualized. 

You can also choose from various initial layout methods available from the button options provided below the dataset drop-down. The random layout will be the default visualization method.

The slider can be used to manipulate the threshold, and based on the value, the corresponding H0 and H1 feature bars fade when not applicable.

H0 and H1 feature bars can be chosen, and the corresponding features will be highlighted in the visualization. 

All the layouts and performance metrics for all the datasets are shown on the 'initial layout figures' page. Furthermore, other figures from the paper are available on their associated pages.

