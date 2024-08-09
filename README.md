# DEPICT: Diffusion-Enabled Permutation Importance for Image Classification Tasks

This is the official code release for "DEPICT: Diffusion-Enabled Permutation Importance for Image Classification Tasks" (ECCV 2024). 

Explanation methods for image classifiers have historically been limited to the pixel space. On the contrary, tabular-based models can be explained using [permutation importance](https://scikit-learn.org/stable/modules/permutation_importance.html). We propose extending permutation importance to generate concept-based explanations for Image-based classifiers. Rather than trying to figure out which pixels in a real image to manipulate, we propose using text-conditioned diffusion models to permute concepts in text-space, and then map such concepts to the image space. 

## Demo 

We first provide a full demo of the method. 


### Dataset 

Before running the demo, you should download the test images from 

```
https://huggingface.co/datasets/sjabbour/depict_demo
```

### Sript 

You can run the following jupyter notebook to recreate on of the rankings that DEPICT generates: 

```
/demo/demo_run.ipynb
```

[8/9/2024]: We will be updating the entire codebase to recreate all experiments in the following months. Thanks for your patience!  


## Contact 

Please reach out to `sjabbour` at `umich` dot `edu` or file a Github issue if you have any questions about our work. Thank you! 