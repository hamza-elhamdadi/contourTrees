# Untangling Force-Directed Layouts with Persistent Homology


## Abstract

Force-directed layouts belong to a popular class of methods used to position nodes in a node-link diagram. However, they typically lack direct consideration of global structures, which can result in visual clutter and the overlap of unrelated structures. In this paper, we use the principles of persistent homology to untangle force-directed layouts thus mitigating these issues. First, we devise a new method to use 0-dimensional persistent homology to efficiently generate an initial graph layout. The approach results in faster convergence and better quality graph layouts. Second, we provide a new definition and an efficient algorithm for 1-dimensional persistent homology features (i.e., tunnels/cycles) on graphs. We then provide users the ability to interact with these 1-dimensional features by highlighting them and adding cycle-emphasizing forces to the layout. Finally, we evaluate our approach with 32 synthetic and real-world graphs by computing various metrics, e.g., co-ranking, edge crossing, crossing angle, and angular displacements, to demonstrate the efficacy of our proposed method.


## To run the demo:

We have tested this setup on Mac and Linux distributions. 

### [required] Install python3

    On Debian linux, such as Ubuntu
    > sudo apt install python3

    On Mac, you can download from python.org, macports, or homebrew. You will need python3. 

### [required] Run the code

    Run the code
    > ./run.sh
    
    Everything should be installed and the code will run. If everything goes as planned, a web browser will be opened automatically for you when everything is done. If it doesn't, you can open a web browser and go to http://localhost:5350/.
    
    
## Citation

Bhavana Doppalapudi, Bei Wang, and Paul Rosen. *Untangling Force-Directed Layouts Using Persistent Homology*, under review at IEEE VIS, 2022

Ashley Suh, Mustafa Hajij, Bei Wang, Carlos Scheidegger, and Paul Rosen. *Persistent Homology Guided Force-Directed Graph Layouts*, IEEE Transactions on Visualization and Computer Graphics (Proceedings of InfoVIS), 2019


## Acknowledgements
    
This work was partially supported by the National Science Foundation (IIS-1513616, IIS-1845204, and DBI-1661375), Department of Energy (DOE) DE-SC0021015, CRA-W Collaborative Research Experiences for Undergraduates (CREU) program, DARPA CHESS FA8750-19-C-0002, and an NVIDIA Academic Hardware Grant.
