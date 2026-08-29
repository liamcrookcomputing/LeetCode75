# 1768. Merge Strings Alternately

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [Merge String Alternately](https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75)
**Date solved:** 2026-08-28

## Problem summary

Take two strings and merge them together by alternating the letters starting from the first word. If a string is longer than the other, the extra letters are placed at the end.

## Scratch Notes (while solving)

> *I need to take two strings and get the index of the letters and return that into a merged string.*
> *`len(str)` would return an int of how many elements in the word*
> *something like `for(x in range(len(word1)))`*
> *index doesn't match string size*
> *find string size then apply*
> *for loop needs largest int count*

## Approach

To solve this problem, I needed to take in two strings and get the index of the letters to then return that into a merged string.
I used len() to find the length of a string and then used an if statement to find which string had the max length.
Then I used a for loop to increment the x variable to grab the element of a string at index x and apply that to the merged string.
In the for loops are two if statement that checks if the x variable is less than the length of the string before applying the element to the merged string.

## Complexity

- **Time:** O(n^2)
- **Space:** O(n)

## Solved cold, or needed a hint?

- [x] Solved independently
- [ ] Needed a hint
- [ ] Looked at the editorial/solution

## What I'd do differently next time

Next time I try this task, I'd like to get time complexity to O(n). This could be done by cleaner code or more deliberate loop functions. Something worth noting is .append() or ''.join() instead of +=, since string concatenation is what is causing O(n^2)

## Related problems

Other problems that use the same pattern (fill in as you notice repeats).