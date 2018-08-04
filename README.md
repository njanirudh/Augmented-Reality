<img src="https://cdn-images-1.medium.com/max/428/1*5bSooyDhHPPSsarNzBQr1w.png" width="150">    

# Augmented-Reality

Augmented reality application using Opencv and OpenGL in python.


## Introduction

Augmented Reality is a view of of the physical, real world environment that is augmented by synthetic computer-generated elements.

## Architecture



### Classes



### Input JSON  

There are two seperate types of JSON depending on the type of marker that is tracked.
The example parameter JSON files are placed in the data folder.

* __NFT marker__  (nft_params.json)
        
        {    
          "calibration_path" : "data/calibration.yaml",
          
          "marker_type" : "nft",    
          "marker_params" :{      
            "marker_path" : "assets/stones.jpg",    
            "feature_type" : "ORB",         
            "matcher_type" : "flann",      
            "debug_draw" : true    
          },
        
          "3d_object" : {    
            "obj_path" : ""    
          }
        
        }

* __Aruco marker__   (aruco_params.json)

        {   
          "calibration_path" : "data/calibration.yaml",    
          
          "marker_type" : "aruco",    
          "marker_params" :{   
            "debug_draw" : true   
          },
        
          "3d_object" : {   
            "obj_path" : ""   
          }   
    
        }


## Installation / Usage



## References







