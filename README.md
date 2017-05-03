# Collaborative-recommendation-engine
This is a basic recommendation engine which gives movie recommendations.

I have made the recommendation engine using a variation of the Jaccard index.

It works on the principle that the more the number of movies which two users like or dislike, the more similar two users are. Contrapositively, the more the number of movies which two users disagree upon, the less similar they are.

The similarity of two users can be quantified by taking the ratio of the difference of the number of movies the two users agree and disagree upon and the sum of the movies which were agreed and disagreed on.

More information on the math behind this method can be found at:
https://www.toptal.com/algorithms/predicting-likes-inside-a-simple-recommendation-engine