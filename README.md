## Sentence classification playground

### Problem statement

Given an input sentence like `Where can I find good sushi` classify the query to a category `sushi`. The input sentences
and categories are given in the `dataset/`.

**Installation** see `requirements.txt` (also, it's assumed that python `virtualenv` is [installed](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)):

```buildoutcfg
# create environment
virtualenv tmppy

# activate environment
source tmppy/bin/activate

# install requirements
pip install -r requirements.txt
```

**NOTE:** One sentence can fit into multiple categories.

### Approaches

This project is very interesting and instead of a single solution, I ended up playing and testing several approaches: 
 - **naive** approach (searching through the lists), `method/naive.py`
 - **trie data structure** `method/trie.py`
 - **multinomial naive Bayes** or better said, statistical approach, `method/multinomial_nb.py`
 - **CNN** ANN ML approach, `method/mlcnn.py`

#### Assumptions and considerations

During this exercise, each solution evolved from the previous one, and from the curiosity of how do things scale. Unfortunately, given the time budget, and personal time that can be allocated to this project assumptions had to be made to simplify the task:
 - categories weren't grouped (e.g. pub, bby could be a group `type`, while the rest labels could be associated to foods by `region`)
 - complete preprocessing (that uses stems of words etc.)
 - target device type and the platform (whether this is a phone or a computer)
 - cool new approaches, transformer or federated learning
 - on CNN (multiple classes for a single sentence)
 - code pre-commit checkups and comments
 - the original dataset was extended (however just with the original words and sentences)
 - generated additional data with 100k sentences 

Failed attempts:
 - created a json file with multiple classes and categories and generated many synthetic classes
 - synthetic annotated dataset 
 - LSTM approach
Most of the failed attempts were to either a mistake in embedding or due to synthetic sentences and categories. Which, produced a lot of data for training, however, not useful in terms of new information. 


### Results

It's interesting to see that the naive approach was the fastest. Which stemmed the idea to extend the dataset and make it larger, with the idea that it will not scale as well as learned methods. 
However, it seems that for the current data it was the fastest. 

With additional optimization CNN could likely perform better, also, a simple i5 laptop CPU was used, without any ML accelerators. 

```buildoutcfg
(Naive) run id (139662498091504) 0.28014183044433594 ms

(Trie) run id (139662498092656) 0.4973411560058594 ms

(MultinomialNB) run id (139662034268016) 6.383180618286133 ms

(cnn) inference id (139660957743136) 1656.2750339508057 ms
```
