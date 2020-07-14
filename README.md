# simplicial-paulversion
This is a copy of the rollout_2simp jupyter notebook. As i am still getting acquainted with git, I feel more comfortable storing my materials here. 

* Clone from  - follow the set up instructions. 
* To make it a smoother experience install tensorflow 1.14 and keras 2.2.5 with python 3.6 ! 
* copy this notebook into the /simplicialtransformer/notebooks directory
* The weights of interest are stored in

The key issue faced right now is that I am trying to generate agent rollouts in parallel using packages such as multiprocessing and concurrent.futures. However, I am facing a deadlock somewhere that I can not identify. I am worried it might be something under the hood with rllib perhaps Daniel can say more about this.  


