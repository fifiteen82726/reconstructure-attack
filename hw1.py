#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# Programming exercise.

# The goal of this exercise is writing a program implementing the (exponential time) reconstruction attack we saw in class which you can find described in Chapter 8 of the book DR linked from the course webpage - you can also look at the original paper linked here:
# http://www.wisdom.weizmann.ac.il/%7Edinuri/mypapers/db_privacy.pdf
# The goal of the exercise is to define a function "attack" which takes in input a dataset D consisting of n records with 1 binary attribute and generate a database D’ which is at hamming distance less than 4E from D. The function attack can access the database D only using queries that are protected via uniform noise with perturbation E=sqrt(n).

# Here some steps I suggest you to follow:
# 1 - Define a function which allows you to create datasets consisting of n records with 1 binary attribute - you can use this function to create the database D and also to create candidate datasets during the attack.
# 2 - Define a function implementing sum queries. It may be convenient to have the function running multiple sum queries and returning the results for all of them.
# 3 - Define a function implementing noisy sum queries: sum queries whose result is perturbed using uniform noise in the interval [0,E]. Also in this case it may be convenient to have the function running multiple noisy sum queries and returning the results for all of them
# 4 - Define a function attack(D) which takes in input a dataset D and generate a database D’ following the three phases of the reconstruction attack presented in class: query phase, rule out phase, output phase. In the query phase and in the rule out phase you may want to use the functions that you have defined at the previous steps.
# 5 - Test your function attack by defining a function which checks that the dataset that the function attack outputs is at most at hamming distance 4E from D (by printing the hamming distance on the screen or by any other method that I can also check). I suggest that you repeat this test on several datasets D. To make it feasible I suggest you to use very small values of n, for example n=10 and n=12.

# return datasets consisting of n records with 1 binary attribute
def create_data_set(n):
  return np.random.choice([0, 1], size=(n))

def sum_query(dataset):
  return sum(dataset)


dataset = create_data_set(10)
print dataset
print sum_query(dataset)
