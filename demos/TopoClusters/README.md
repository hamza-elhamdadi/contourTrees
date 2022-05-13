# TopoCluster: Modeling the Influence of Visual Density on Cluster Perception in Scatterplots Using Topology


## Abstract

Scatterplots are used for a variety of visual analytics tasks, including cluster identification, and the visual encodings used on a scatterplot play a deciding role on the level of visual separation of clusters. For visualization designers, optimizing the visual encodings is crucial to maximizing the clarity of data. This requires accurately modeling human perception of cluster separation, which remains challenging. We present a multi-stage user study focusing on four factors---distribution size of clusters, number of points, size of points, and opacity of points---that influence cluster identification in scatterplots. From these parameters, we have constructed two models, a distance-based model, and a density-based model, using the merge tree data structure from Topological Data Analysis. Our analysis demonstrates that these factors play an important role in the number of clusters perceived, and it verifies that the distance-based and density-based models can reasonably estimate the number of clusters a user observes. Finally, we demonstrate how these models can be used to optimize visual encodings on real-world data.

       
## To run the demo:

We have tested this setup on Mac and Linux distributions. 

### [required] Install python3, python3-virtualenv, and git

    On Debian linux, such as Ubuntu
    > sudo apt install python3 python3-virtualenv git

    On Mac, you can download from python.org, macports, or homebrew. You will need python3, python3-virtualenv, pip, git, ... maybe others 

### [required] Run the code

    Run the code
    > ./run.sh
    
    Everything should be installed and the code will run. If everything goes as planned, a web browser will be opened automatically for you when everything is done. If it doesn't, you can open a web browser and go to http://localhost:5250/.
    
    
## Citation

Ghulam Jilani Quadri and Paul Rosen. *Modeling the Influence of Visual Density on Cluster Perception in Scatterplots Using Topology*, Transactions on Visualization and Computer Graphics (Proceedings of InfoVis), 2020


## Acknowledgements
    
This work was partially supported by the National Science Foundation (IIS-1845204).
