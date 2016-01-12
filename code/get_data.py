import numpy as np
import requests
import shutil
from scipy import misc
import matplotlib.pyplot as plt


def read_galaxy_table(filename):
	'''read in table containing galaxy positions'''

	gal_id = np.genfromtxt(filename, delimiter=',', dtype=int, usecols=[0])    # loadtxt doesn't read in large number correctly 
	f = np.loadtxt(filename, delimiter=',')
	ra = f[:,1]
	dec = f[:,2]
	return gal_id, ra, dec


def create_url(ra, dec):
	'''create url string given ra and dec of galaxy'''

	url = "http://skyservice.pha.jhu.edu/DR7/ImgCutout/getjpeg.aspx?ra={0}&dec={1}&width=200&height=200".format(ra, dec)
	return url


def create_outfile(gal_id):
	'''create name of outfile to save image to'''

	outfile = "../images/img_{0}.png".format(gal_id)
	return outfile


def get_img(url, outfile):
	'''get img from url'''

	response = requests.get(url, stream=True)
	with open(outfile, 'wb') as outfile:
		shutil.copyfileobj(response.raw, outfile)
	

def plot_img(img):
	'''plot one image'''

	g = misc.imread(img)
	plt.imshow(g)
	plt.show()



if __name__ == '__main__':
	gal_id, ra, dec = read_galaxy_table('gal_pos_label.txt')
	# get images in the range 32000 to 35000 -- can make this an argument
	for i in range(32000, 35000):
		url = create_url(ra[i], dec[i])
		outfile = create_outfile(gal_id[i])
		get_img(url, outfile)
		#plot_img(outfile)
