# Classifying Galaxies in the Sloan Digital Sky Survey


Spiral Galaxy             |  Elliptical Galaxy
:-------------------------:|:-------------------------:
![](./images/img_587724649793716359.png)  |  ![](./images/img_587730848498712762.png)


##Contents



##Motivation
Galaxy classification has long been vital to understanding of how galaxies form and evolve. Spiral galaxies are disk-shaped, and are the site of active star formation.  Many of these galaxies will eventually merge together to form massive elliptical galaxies. In addition to these major types of galaxies, there are irregular galaxies which are not disk or spherical and are often the result of the merger of two or more galaxies, and lenticular galaxies which have some characteristics of both spirals and ellipticals. With the advent of large imaging surveys such as the Sloan Digital Sky Survey (SDSS), the amount of astronomical data generated has grown exponentially. In the past, astronomers would classify galaxies based on a by-eye viewing of the image. This is simply not possible today when astronomers have hundreds of millions of galaxies to classify.
Crowd sourcing through sites such as GalaxyZoo is a viable means of obtaining classifications for the SDSS galaxies.  However, automatic classification of galaxies will enable astronomers to devote their time and energy into understanding the physical processes that created these galaxies and that in turn shaped the universe in which we live.


##Data
I classified 20,000 of the brightest and largest galaxies from SDSS (Alam et al. 2015) and compared them to the classifications that were generated from GalaxyZoo (Lintott et al. 2011). I scraped the SDSS skyserver website to obtain these images, which were 200 x 200 x 200 pixels.


##Model
Neural networks are often used for image classification. theano (http://deeplearning.net/software/theano/) is a neural network implementation in Python which can be used for image classification. I used this neural network implementation to classify SDSS galaxies. I trained the neural network using the GalaxyZoo classifications, while leaving out a fraction of the data as the test set. I then tested the accuracy of the neural network predictions based on the results from the GalaxyZoo classifications. Since the time to train the neural network can become lengthy, I trained this network using an AWS GPU instance, which is better suited to training neural networks on images.

![](./images/neural_network_model.png)

##Results

Can look at several metrics to determine performance of model.  
overall accuracy on test data is 66%, while random guessing among the 3 categories would give 33% accuracy.
The confusion matrix shows predicted label vs true label, and is darker where more classifications are, we can see it usually does a good job, and that the model does especially well at separating spirals and ellipticals.

![](./images/confusion_matrix.png)

This ROC curve is made by treating each classifier as binary:  e.g. is it spiral or not spiral.  The AUC is largest for the elliptical classification at 0.92, the next highest is for spiral, and uncertain is lowest.

![](./images/roc_curve.png)


The model also gives a probability for each galaxy that it is in each classification.  This visualization shows typical galaxies for various probabilities from the model.  This shows that high prob galaxies have very distinct morphologies and look like classic ell and spirals, the typical uncertain galaxy appears smaller on the image, likely due to distance, and appears similar to lenticular galaxies. this area is where most of the misclassifications come from, and even visually, it is harder to tell what type of galaxy it is, some are transitioning from spiral to elliptical.  some of the labels may be wrong
We see that I can likely get even better accuracies by looking at only the galaxies with high probabilities.
When I restrict the sample to only high prob spirals, the accuracy of correctly identifying spiral galaxies is 77%, ell is…

![](./images/galaxy_triangle.png)


##Future Work
I can then add increasingly more complex classifications if this performs well, such as elliptical, clockwise spiral, anti-clockwise spiral, edge-on, star/don’t know, or merger. The next step after this would be to incorporate more galactic features such as bars and dust lanes, and add in smaller and fainter galaxies.







