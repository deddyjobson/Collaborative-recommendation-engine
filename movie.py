from __future__ import division
from numpy import *
from csv import *
from sys import exit
from numpy.random import randint
THE_USER = 100#The user-id for whom you want to give a recommendation

#To fet the entire spreadsheet as a 2-D list,
with open('rating.csv', 'rb') as f:
    values = list(reader(f))

values = map(list,zip(*values))
d = {}
for i in range(len(values)):
    d[values[i][0]] = array([int(float(a)) for a in values[i][1:]])

userid = d[values[0][0]] - 1
movieid = d[values[1][0]] - 1
rating = d[values[2][0]]#from 1 to 5
like = rating>=3#True if like, false if not

with open('movies.csv', 'rb') as f:
    value = list(reader(f))
title = [value[i][1] for i in range(1,len(value))]
mvid = [int(value[i][0])-1 for i in range(1,len(value))]


class User:
    """
    ML -> movies the user likes
    MH -> movies the user hates

    S()
    similarity between 2 users

    """
    def __init__(self):
        self.ML = set()
        self.MH = set()

    def S(self,user2):
        num = len(self.ML.intersection(user2.ML))+len(self.MH.intersection(user2.MH))
        num -= len(self.ML.intersection(user2.MH))+len(self.MH.intersection(user2.ML))
        den = len(self.ML.union(user2.ML.union(user2.MH.union(self.MH))))
        return num / den

class Movie:
    """
    UL -> users who like the movie
    UH -> users who hate the movie
    """
    def __init__(self):
        self.UL = set()
        self.UH = set()


#to iterate over all users or movies
user = [User() for _ in range(int(max(userid))+1)]
movie = [Movie() for _ in range(int(max(movieid))+1)]

for i,u,m in zip(range(len(userid)),userid,movieid):
    if like[i]:
        user[u].ML.add(m)
        movie[m].UL.add(u)
    else:
        user[u].MH.add(m)
        movie[m].UH.add(u)


#To calculate the probability of a user liking a movie
def P(U,M):
    """probability of U liking P   
    Arguments:
        U {User}
        M {Movie}

    Returns:
        Float between -1.0 and 1.0
    """   
    if len(M.UL)+len(M.UH) == 0:
        return 0
    ZL = sum([U.S(user[i]) for i in M.UL])
    ZH = sum([U.S(user[i]) for i in M.UH])
    return (ZL - ZH)/(len(M.UL)+len(M.UH))


#To make recommendation for a person in the dataset.
if(False):
    pmax = -1
    ind = 0
    for i,m in enumerate(movie):
        if i not in user[THE_USER].ML:#so that you don't recommend a movie that is watched
            if P(user[THE_USER],m) > pmax:
                pmax = P(user[THE_USER],m)
                ind = i

    print 'Best movie recommended is:', title[mvid.index(ind)]


#To make recommendation for the user.
master = User()
films = randint(0,len(title),5)
print 'Answer 1 (True) or 0 (False).'
for i,f in enumerate(films):
    print 'Do you like ', title[f], '?'
    if int(input()) == 1:
        master.ML.add(mvid[f])
    else:
        master.MH.add(mvid[f])

pmax = -1
ind = 0
for i,m in enumerate(movie):
    if i not in master.ML:#so that you don't recommend a movie that is watched
        if P(master,m) > pmax:
            pmax = P(master,m)
            ind = i

print 'Best movie recommended is:', title[mvid.index(ind)]

