#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import math
import random
from itertools import combinations

class Reconstruction:
  def __init__(self, n, e):
    self.real_dataset = self.create_data_set(n)
    self.e = int(e)
    self.n = n
    self.all_combination = []
    self.attacked_comination_hash_table = {}

    for r in range(1, n):
      self.all_combination.append(self.rSubset(range(1, n + 1), r))

    print "Real Dataset:          " + str(self.real_dataset)

  # recursive to return all combination
  def rSubset(self, arr, r):
    return list(combinations(arr, r))

  def create_data_set(self, n):
    return list(np.random.choice([0, 1], size=(n)))

  def sum_queries(self, query_index, dataset = None):
    sum_result = 0
    target_dataset = dataset or self.real_dataset

    for i in query_index:
      sum_result += target_dataset[i - 1]
    return sum_result

  def noise_sum_queries(self, query_index):
    num = self.sum_queries(query_index)
    # add some noise (between 0 to e)
    random_noise = random.choice(range(int(self.e) + 1))
    return num + random_noise

  def attack(self):
    # loop to get noise_sum_queries
    guess_dataset = [0] * self.n
    for combine in self.all_combination:
      for el in combine:
        noise_sum_queries_num = self.noise_sum_queries(el)

        # these number must be one
        if (len(el) == 1 and noise_sum_queries_num > self.e):
          guess_dataset[el[0] - 1] = 1
        else:
          if(noise_sum_queries_num - len(el) == self.e):
            for i in el:
              guess_dataset[i - 1] = 1

      if(self.authenticate(guess_dataset)):
        print "Reconstrcture Dataset: " + str(guess_dataset)
        return guess_dataset

    print "Fail Attack!"
    return False

  def authenticate(self, attacked_dataset):
    a = 0
    for combine in self.all_combination:
      for el in combine:
        query_sum = self.sum_queries(el)
        attack_sum = self.sum_queries(el, attacked_dataset)
        if(abs(query_sum - attack_sum) > e):
          return False # Rule out
    return True

  def compute_hamming_distance(self, guess_dataset):
    result = 0
    for i in range(n):
      if(guess_dataset[i] != self.real_dataset[i]):
        result += 1
    return result

n = 10
e = math.sqrt(n)

print "n = " + str(n)
print "E = " + str(e)

for i in range(10):
  print "======================= Test " + str(i+1) + " ============================"
  reconstruction1 = Reconstruction(n, e)
  guess_dataset = reconstruction1.attack()
  if(guess_dataset):
    print "Successfully attack, the hamming distance is " + str(reconstruction1.compute_hamming_distance(guess_dataset))
  print "\n"