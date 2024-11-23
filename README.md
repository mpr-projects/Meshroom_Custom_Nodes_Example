This is an example of adding custom nodes to Meshroom (in response to a question on [YouTube](https://youtu.be/XUKu1apUuVE)). You first need to create a directory containing a file called ```__init__.py``` (to indicate that it's a Python module). If you take this repository as an example then the directory would be called ```Meshroom_Custom_Nodes_Example```. Then you place your custom nodes inside a subfolder, in this repo the subfolder is called ```mpr```. To tell Meshroom to use your custom nodes you have to set the environment variable ```MESHROOM_NODES_PATH``` to the location of your main folder, e.g. add ```export Meshroom_Custom_Nodes_Example=/home/mpr/Meshroom_Custom_Nodes_Example``` to your .bashrc file.

The nodes themselves are Python classes that can either be command line nodes, where you specify a command to run that's available on your OS (that's in your PATH), or 'regular' nodes, where the code in member function ```processChunk``` is run. I've added two of my nodes to this repository. A full description of how they work takes a bit (a lot) more time than I have available right now but they should contain sufficient information for you to get started with nodes -- although you probably have to do some more testing and digging in Meshroom's source code.

A few more notes: If you use a very recent version of meshroom then it will probably complain about the lines about uid's, e.g. ```uid=[]```. Those were recently removed from Meshroom so you'll have to remove them for the code to work with newer versions of Meshroom. Also, the command ```aliceVision_landmarkBounding``` that's referenced in the command line node is a cpp file that I wrote myself so it won't exist on your system.

If you want to create command line nodes yourself then you can look at any of the relevant files in the AliceVision repo (e.g. [this one](https://github.com/alicevision/AliceVision/blob/develop/src/software/pipeline/main_featureExtraction.cpp) which is called by [this one](https://github.com/alicevision/Meshroom/blob/develop/meshroom/nodes/aliceVision/FeatureExtraction.py)) to see how they process the command line parameters. You can mostly copy-paste that code from existing the files (picking the parts that you need). However, if you do that then you'll probably have to spend some time looking through AliceVision's source code to be able to use it properly -- and you'll have to include your files in AliceVision's build system (CMake) which may not be so much fun if you're not used to CMake :-)

Good luck!