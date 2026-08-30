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

To solve this problem, I looped through the flowerbed array once with an index x, checking at each position whether a flower could be planted there — meaning the current spot is empty (0) and both of its neighbors are also empty.

Since checking neighbors risks going out of bounds at the start and end of the array, I split the logic into three cases:

If x == 0 (the first index), there's no x - 1 to check, so I only looked at flowerbed[x] and flowerbed[x + 1]. I also handled the edge case where the array has only one element, since in that case there's no x + 1 either.
If x == flowerbedLength - 1 (the last index), there's no x + 1 to check, so I only looked at flowerbed[x] and flowerbed[x - 1].
Otherwise (anywhere in the middle), I checked all three: flowerbed[x], flowerbed[x - 1], and flowerbed[x + 1].

Whenever a spot passed its check, I set flowerbed[x] = 1 (planting the flower directly in the array, so future neighbor-checks see the update) and incremented totalCanPlace.

Finally, I returned whether totalCanPlace >= n, since the question only asks if at least n flowers can be planted, not exactly n.

One thing I noted afterward: this ended up as a fairly long chain of if/elif statements to handle the start/end/middle cases separately, which felt messy — worth looking into a cleaner way to handle array boundaries (like a sentinel/padding approach) next time this kind of edge case comes up.

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