# Search for pairs giving the maximum product #

The goal of this algorithm is to search in a given list of numbers **all pairs** of numbers whose the **product** gives the **maximum value**.
Algorithm adapted from the exercise found at [techiedelight.com](http://www.techiedelight.com/find-maximum-product-two-integers-array/)

## functions used in the algorithm ##

###  research_pairs(givenList, maximum=0)###
This function will first calculate the **maximum product** obtained from each **pairs** of numbers. It will then call the fonction **search_the_max_index** and it will show to terminal all the potential solutions.

### search_the_max_index(productList) ###
This function will search for the **indexes** of all pairs of numbers giving the **maximum product**. The first for loop in the **research_pairs** function might have added product which are not the maximum. It will return a list made by those indexes.
