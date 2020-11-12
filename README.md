<img src="https://cdn-images-1.medium.com/max/428/1*5bSooyDhHPPSsarNzBQr1w.png" width="150">    

# Augmented-Reality

This repository contains a prototype Augmented reality application using OpenCV and OpenGL python. Aim of this project is to make a modular AR framework using python which works on wide variety of markers and on which we can place wide variety of graphical elements.
The application takes a <config>.json file as an input and uses that to find apropriate type of marker.  

## Installation / Usage

* Clone the git repo
* Install the modules    
        __pip install -r requirements.txt__
* Run __main.py__ (Default values)

## Architecture

* Basic application process blocks
<img src="https://github.com/njanirudh/Augmented-Reality/blob/master/assets/process.png" width="1000">    

Depending on the JSON parameters the application will be able to detect 'Aruco' or 'NFT' markers.

* Marker detection process
<img src="https://github.com/njanirudh/Augmented-Reality/blob/master/assets/architecture.png" width="1000">    


### Input JSON  

There are two seperate types of JSON depending on the type of marker tracked.
The default parameter JSON files are placed in the data folder.

The paths to the calibration file and marker can be changed  

* __NFT marker__  (nft_params.json)
        
        {    
          "calibration_path" : "data/calibration.yaml",
          
          "marker_type" : "nft",    
          "marker_params" :{      
            "marker_path" : "assets/stones.jpg",    
            "feature_type" : "ORB",                  // ORB , AKAZE
            "matcher_type" : "flann",                // flann , bfm
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


## Authors

* **N J Anirudh** - *Initial work* - [njanirudh](https://github.com/njanirudh)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details







