# Importing necessary library 
import Augmentor 
# Passing the path of the image directory 
p = Augmentor.Pipeline("data")
  
# Defining augmentation parameters and generating 5 samples 
p.flip_left_right(0.2) 
p.black_and_white(0.3) 
p.rotate(0.3, 10, 10) 
p.skew(0.4, 0.5) 
p.zoom(probability = 0.2, min_factor = 1.1, max_factor = 1.5) 
p.sample(100000) 
