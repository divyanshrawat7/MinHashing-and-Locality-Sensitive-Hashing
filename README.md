# CSL7110 -- Machine Learning with Big Data (Assignment 2)

MinHashing and Locality Sensitive Hashing

## Overview

This repository contains implementations for:

1.  K-gram construction and exact Jaccard similarity
2.  MinHash signature computation and analysis
3.  Locality Sensitive Hashing (LSH) on small documents
4.  MinHash on the MovieLens 100K dataset
5.  LSH on the MovieLens 100K dataset

All programs are written in Python using only standard libraries.

------------------------------------------------------------------------

## Requirements

-   Python 3.8 or above
-   No external libraries required

------------------------------------------------------------------------

## Files Included

Q1_kgrams_minhash.py\
Q2_minhash_basic.py\
Q3_lsh_small_docs.py\
Q4_movielens_minhash.py\
Q5_movielens_lsh.py

README.md

------------------------------------------------------------------------

## Question 1

Construct character and word k-grams, compute exact Jaccard similarities
for all document pairs, and estimate similarity using MinHash.

Run: python Q1_kgrams_minhash.py

------------------------------------------------------------------------

## Question 2

Generate MinHash signatures using different numbers of hash functions (t
= 20, 60, 150, 300, 600).\
Analyze estimation accuracy and runtime tradeoffs.

Run: python Q2_minhash_basic.py

------------------------------------------------------------------------

## Question 3

Implement LSH with t = 160 hash functions.\
Determine suitable banding parameters and compute candidate
probabilities above the similarity threshold.

Run: python Q3_lsh_small_docs.py

------------------------------------------------------------------------

## Question 4

Apply MinHash to the MovieLens 100K dataset.\
Compute exact Jaccard similarities between users and evaluate false
positives and false negatives across multiple runs.

Dataset Setup: Download MovieLens 100K dataset and place 'u.data' in the
same folder as the script.

Run: python Q4_movielens_minhash.py

------------------------------------------------------------------------

## Question 5

Apply LSH banding strategies on MovieLens dataset using specified (r, b)
configurations.\
Evaluate performance for similarity thresholds 0.6 and 0.8 over 5 runs.

Run: python Q5_movielens_lsh.py

------------------------------------------------------------------------

Course: CSL7110 -- Machine Learning on Big Data\
Assignment 2
