# Image_Comparison_Metrics

The python program contains implementation of calculating the MSE, SSIM, and Z-norm errors per pixel for comparison of images from two directories.
The program was created for batch image comparison.

This python program takes three directories as inputs: 
1. Dir-1 : contains original gaze-map image
2. Dir-2 : contains predicted gaze-map images
3. OuputDir : results should be generated here

**Important** 
1. The restriction is that both the directories must contain equal number of files.
   The comparison is done in order. [first file from dir1 to first file from dir2] 

2. Two images can be compared when they are of same size.
   Hence, it also contains code to resize images (currently applied on images from one of the directories) 
   It can be modified suit as per the specific needs or removed.  

Three output files are created - mse.txt, z_norm.txt, and ssim.txt
The output files will have error values, one per image, written in text file.

Contributors 
1. Shivam Chourey : https://www.linkedin.com/in/shivamchourey/  \
2. Ashin Marin Thomas : https://www.linkedin.com/in/ashin-marin-thomas-16a46650/

