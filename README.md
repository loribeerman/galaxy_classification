# Classifying Galaxies in the Sloan Digital Sky Survey


Spiral Galaxy             |  Elliptical Galaxy
:-------------------------:|:-------------------------:
![](./images/img_587724649793716359.png)  |  ![](./images/img_587730848498712762.png)


##Contents



##Motivation
Galaxy classification has long been vital to understanding of how galaxies form and evolve. Spiral galaxies are disk-shaped, and are the site of active star formation.  Many of these galaxies will eventually merge together to form massive elliptical galaxies. In addition to these major types of galaxies, there are irregular galaxies which are not disk or spherical and are often the result of the merger of two or more galaxies, and lenticular galaxies which have some characteristics of both spirals and ellipticals. With the advent of large imaging surveys such as the Sloan Digital Sky Survey (SDSS), the amount of astronomical data generated has grown exponentially. In the past, astronomers would classify galaxies based on a by-eye viewing of the image. This is simply not possible today when astronomers have hundreds of millions of galaxies to classify.
Crowd sourcing through sites such as GalaxyZoo is a viable means of obtaining classifications for the SDSS galaxies.  However, automatic classification of galaxies will enable astronomers to devote their time and energy into understanding the physical processes that created these galaxies and that in turn shaped the universe in which we live.


##Data
I classified 20,000 of the brightest and largest galaxies from SDSS (Alam et al. 2015) and compared them to the classifications that were generated from GalaxyZoo (Lintott et al. 2011). I will write SQL queries using the SDSS skyserver site (http://skyserver.sdss.org/) which will give me the position on the sky and object id for these objects, along with the GalaxyZoo label classification. Using these sky positions, I will be scraping the sky server site for the images of each galaxy, with which I can specify the image size (http://skyservice.pha.jhu.edu/DR10/ImgCutout/getjpeg.aspx). Initial testing shows a size of 200x200 pixels gives a nice centered image of most of the galaxies in my target sample. The scraping will save these images as .png files, which I will then convert to numpy arrays using scipy. The resulting size of each RGB image is (200, 200, 3). See Figure 2 below for two example images.
I plan on initially classifying the images according to the top level of the Galaxy Zoo decision tree (Figure 3), which is: smooth, features or disk, and star or artifact. I can then add increasingly more complex classifications if this performs well, such as elliptical, clockwise spiral, anti-clockwise spiral, edge-on, star/don’t know, or merger. The next step after this would be to incorporate more galactic features such as bars and dust lanes, and add in smaller and fainter galaxies.


##Model
Neural networks are often used for image classification. theano (http://deeplearning.net/software/theano/) is a neural network implementation in Python which can be used for image classification. I used this neural network implementation to classify SDSS galaxies. I trained the neural network using the GalaxyZoo classifications, while leaving out a fraction of the data as the test set. I then tested the accuracy of the neural network predictions based on the results from the GalaxyZoo classifications. Since the time to train the neural network can become lengthy, I trained this network using an AWS GPU instance, which is better suited to training neural networks on images.

![](./images/neural_network_model.png)

##Results



##Future Work
I can then add increasingly more complex classifications if this performs well, such as elliptical, clockwise spiral, anti-clockwise spiral, edge-on, star/don’t know, or merger. The next step after this would be to incorporate more galactic features such as bars and dust lanes, and add in smaller and fainter galaxies.







