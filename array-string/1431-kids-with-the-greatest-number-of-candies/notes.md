# 1431. Kids With the Greatest Number of Candies

| | |
|---|---|
| **Difficulty** | Easy |
| **Pattern** | Array |
| **Link** | [link](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75) |
| **Date solved** | 2026-08-29 |

## Problem summary

Given an array of integers, add the extra candies integer to each index and return true if that index + extra candies is the greatest integer across the array.

Multiple kids can have the greatest amount of candies.

## Scratch Notes (while solving)

> *For loop to check through the array and add the integer to each element, then check if it's greater than or equal to all elements.*
>
> *Actually, just get max of array and check if the new value is greater.*
>
> *Add the result (true or false) to the result array.*
>
> *We can actually just skip the if statement and put it directly into the append with the condition.*
>
> *I'm using append here because it's better than += for the array and it does exactly what's needed.*
>
> *Then just return result.*

## Approach

To solve this problem, I looped through the candies array and, for each kid, calculated what their candy count would be if they received all the extra candies (candies[x] + extraCandies).

I then compared that value against the maximum value already in the array (using max(candies)) — if the kid's new total is greater than or equal to the max, they could have the most candies, so the result is True; otherwise False.

Instead of using an if/else to compute the boolean first and then append it, I put the comparison directly inside append() as the condition, since it evaluates to True or False on its own and skips the extra step. I used append() here rather than += since it's the correct way to add single elements to a list, and it's more direct for building up the result array one boolean at a time.

Finally I returned the result array.

## Complexity

- **Time:** O(n^2)
- **Space:** O(n)

## Solved cold, or needed a hint?

- [x] Solved independently
- [ ] Needed a hint
- [ ] Looked at the editorial/solution

## What I'd do differently next time

Looking at the leaderboard for time, this code has a runtime of 2ms and only beats 16.82% of other submissions. I'd like to try cut down the runtime to 0ms the next time I do this.

## Related problems

Other problems that use the same pattern (fill in as you notice repeats).