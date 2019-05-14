# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:01:00 2019

@author: Shivam Chourey
"""
import os
import argparse
import numpy as np
import cv2
from skimage import measure

from scipy import sum, average


def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def compare_images(imageset1, imageset2, dir1, dir2, outputdir):
    
    print(len(imageset1))
    print(len(imageset2))
     
    if(len(imageset1) == len(imageset2)):
        print('Yay')
        f1 = open(outputdir+'mse.txt', 'w')
        f2 = open(outputdir+'z_norm.txt', 'w')
        f3 = open(outputdir+'s_norm.txt', 'w')

        NumImages = len(imageset1)
        for index in range(NumImages):
            
            imageA = to_grayscale(cv2.imread(dir1+'/'+imageset1[index]).astype("float"))
            imageB = to_grayscale(cv2.imread(dir2+'/'+imageset2[index]).astype("float"))
            
            size = (48, 36)
            imageB = cv2.resize(imageB, size)
            
            imageA = normalize(imageA)
            imageB = normalize(imageB)
            
            err = np.sum((imageA-imageB)**2)
            err /= float(imageA.shape[0] * imageA.shape[1])

            diff = imageA - imageB
            m_norm = sum(abs(diff)) 
            z_norm = np.linalg.norm(diff.ravel(), 0)/imageA.size
            
            ssim = measure.compare_ssim(imageA, imageB)
            
            f1.write('%.2f'%err)
            f1.write("\n")
            f2.write('%.2f'%z_norm)
            f2.write("\n")
            f3.write('%.2f'%ssim)
            f3.write("\n")
            
        f1.close()
        f2.close()
        f3.close()
            
            
parser = argparse.ArgumentParser()
parser.add_argument('--dir1',default=None, type=str, help='Dir1')
parser.add_argument('--dir2', default=None, type=str, help='Dir2')
parser.add_argument('--outputdir', default=None, type=str, help='outputdir')

args = parser.parse_args()

dir1 = args.dir1
dir2 = args.dir2
odir = args.outputdir

imageset1 = os.listdir(dir1)
imageset2 = os.listdir(dir2)

compare_images(imageset1, imageset2, dir1, dir2, odir)


            
            
        
    