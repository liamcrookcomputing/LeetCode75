# 605. Can Place Flowers

|---|---|
| **Difficulty:** | Easy |
| **Pattern:** | Array / Greedy |
| **Link:** | [link](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75) |
| **Date solved:** | 2026-08-30 |

## Problem summary

In an array check if the element before or after the index is a viable place to put a flower (0 = empty, 1 = flower). If conditions are met, check if the input n is less than or equal to the amount of flowers able to be put in the array. Return true or false.

## Scratch Notes (while solving)

> *In an array, check if index ± 1 == 0, if true then return true.*
> *Actually I need more than that — I need to find if n == how many flowers can be placed.*
> *So I created a variable totalCanPlace and increment it when the conditions are met.*
>
> *What happens if I check the first index? x - 1 is out of bounds, so check if we are at the start of the array.*
> *What happens if it's at the end? x + 1 is out of bounds, so check if we are at the end too.*
>
> *Array size == 1 — need to add something to check that.*
>
> *This is starting to become a mess of if/elif statements, there must be a better way to do this.*
>
> *New test case shows n < totalCanPlace, so changing the return to allow for >= n.*
>
> *Code works but doesn't feel or look great.*

## Approach

What did you do to solve the problem? 

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Solved cold, or needed a hint?

- [X] Solved independently
- [ ] Needed a hint
- [ ] Looked at the editorial/solution

## What I'd do differently next time

The code is functional but clearly a mess. I will look into how to better solve this problem for the next time I attempt this, some things I've seen so far to help with this problem is sentinel values / padding, which I assume is adding an element to the front and end of an array - I have not actually checked it out yet, but I can see that if this is the correct way to implement it, then this would be a perfect problem case. Adding 0 to the start and end of the array would solve all the edge case conditions I have of the size being too small, checking only x + 1 or x - 1, checking if we're at the start or at the end.

I will start reviewing how other people solved the problem code and try to understand why they did it that way.

## Related problems

Other problems that use the same pattern (fill in as you notice repeats).