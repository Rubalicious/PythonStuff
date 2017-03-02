# 
# 	Author: Ruby Abrams
# 	Description:
# 			This script will do analysis and image visualization
# 			on the movie_metadata.csv file.
# 			Hope fully I can start using machine learning algorithms
# 			on the data set too.
# 			
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

if __name__ == '__main__':
	movies = pd.read_csv('movie_metadata.csv')
	print(movies.columns)
	plt.hist(movies.imdb_score)
	plt.show()