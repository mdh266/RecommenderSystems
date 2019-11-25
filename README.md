# Recommender Systems & Collaborative Filtering

## Introduction

Recommendation systems are an important application of data science in industry. They are used almost everywhere; examples being recommending items to sell to users on Amazon, songs on Pandora and movies/shows on Netflix. There are two general approaches to recommender systems:

1. <a href="https://en.wikipedia.org/wiki/Collaborative_filtering">Collaborative filtering</a>

2. <a href="https://en.wikipedia.org/wiki/Recommender_system#Content-based_filtering">Content based filtering</a>

Collaborative filtering is a method of recommending products to customers using their past behavoirs or ratings as well as similar decisions by other customers to predict which items might be appealing to the original customers. Content-based filtering suggests products to customers by using the characteristics of an item in order to recommend additional items with similar properties. I'll just be touching on collaborative filtering in this blog post since it is very popular and has the ability to accurately recommend complex items without the need to understand the item itself.  Collaborative filtering is also much more popular for web-based recommendations where the data is sparse, i.e., where there is a limited number of reviews by each user or for a particular product.  

## Data
The data we will use comes from <a href="https:amazon.com">Amazon</a> and can be found <a href="http://jmcauley.ucsd.edu/data/amazon/">here</a>.  I chose the Amazon Instant Video 5 core file. The 5 core implies that each video/item has atleast 5 ratings and each users has rated atleast 5 videos/items.

## Requirements
1. <a href="https://www.python.org/"> Python</a> (3.X)
2. <a href="http://jupyter.org/">Jupyter Notebook</a>
3. <a href="http://www.numpy.org/">NumPy</a>
4. <a href="http://www.scipy.org/">SciPy</a>
5. <a href="http://matplotlib.org/">matplotlib</a>
6. <a href="http://pandas.pydata.org">Pandas</a>
7. <a href="http://scikit-learn.org/stable/">scikit learn</a>
8. <a href="http://seaborn.pydata.org/">Seaborn</a>

To install the requirements with pip (except for Python and Jupyter notebooks), type in the main directory:

	pip install -r requirements.txt 

Alternatively you can install the dependencies and access the notebook using <a href="https://www.docker.com/">Docker</a> by building the Docker image with the following:


	docker build -t recommend .

Followed by running the command container:

	docker run -p 8888:8888 -t recommend
