# 238. Product of Array Except Self

|---|---|
| **Difficulty:** | Medium |
| **Pattern:** | Array / Prefix Sum |
| **Link:** | [link](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75) |
| **Date solved:** | 2026-08-31 |

## Problem summary

Return the product of an array that does not include array[i], it must run in O(n) and not use the division operation.

## Scratch Notes (while solving)

> *loop through nums, temporarily pop out the current index, use math.prod on the rest, then insert it back. worked and felt clean but turned out to be O(n^2) since pop, insert, and math.prod are all O(n) each, and they're all happening inside a loop that runs n times.*
>
> *reframed it as prefix/suffix products instead. prefix[i] = product of everything before i, suffix[i] = product of everything after i, answer[i] = prefix[i] * suffix[i]. idea is build each with one pass instead of recomputing the whole product every iteration.*
>
> *first attempt tried building prefix, suffix, and answer all in the same loop, but prefix and suffix were still empty when i tried to read from them. needed to be three separate passes, not one merged loop.*
>
> *got stuck on what prefix[0] should be. Needed the multiplication identity — 1 — as a fixed starting value before the loop even runs.*
>
> *same identity idea for suffix[0] (well, the first value appended).*
>
> *suffix loop kept hitting IndexError, tried a few different index formulas (len(nums)-i, len(nums)-i-1, len(nums)-i-2) before landing on one that actually lined up. realized suffix[-1] (just "the last thing appended so far") would've avoided all the index math entirely, since suffix builds right to left and the previous value is always just the most recent append.*
>
> *also had a range() off-by-one, range(len(nums)-2, 0, -1) skipped i=0 entirely because range's stop bound is exclusive. changed stop to -1 so it actually includes 0.*
>
> *answer loop also had a bug, was doing prefix[1] * suffix[i], a fixed index instead of prefix[i]. once prefix and suffix were both aligned to nums' index order, needed prefix[i] * suffix[i] at matching positions.*
>
> *finally got [24,12,8,6] on nums=[1,2,3,4], matches expected output.*
>
> *afterward looked at a faster submission that uses total product // nums[i] instead of prefix/suffix arrays at all. only issue is division breaks with zeros in the array, so it needs a separate branch: if exactly one zero, product of everything else goes at that index and everything else is 0; if two+ zeros, everything is 0. no zeros, just divide the total by each element.*
>
> *issue with this approach is that the problem asks to not use division, but the submissions use floor division. I'm unsure as to if this is because the problem writers forgot to add floor division or if floor division is allowed, but I have decided not to use it in future solutions of this problem as I'm using this to learn.*

## Approach

My first attempt looped through nums, and for each index, temporarily removed that element with .pop(i), used math.prod() on the remaining elements, then put the element back with .insert(i, tempValue). This worked but turned out to be O(n²), since pop, insert, and math.prod are each O(n) on their own, and all three were happening inside a loop that runs n times.

To fix this, I switched to a prefix/suffix product approach. The idea is that the product of everything except nums[i] is the same as (product of everything before i) × (product of everything after i) — so instead of recomputing a fresh product from scratch at every index, I built two arrays once, each with a single pass.

I built prefix left to right, where prefix[i] holds the product of everything in nums before index i. I started prefix with [1] (the multiplication identity, representing "the product of nothing" for the very first position), then looped from index 1 onward, appending prefix[i-1] * nums[i-1] — building each new value off the one just computed, rather than recalculating the whole product again.

I built suffix the mirror way, right to left, starting from [1] and looping from the second-to-last index down to 0, appending suffix[len(nums) - i - 2] * nums[i+1] (multiplying the most recently computed suffix value by the next nums element moving inward). I reversed the list at the end so its indices lined up with nums' original order.

Finally, I looped through once more and built answer[i] = prefix[i] * suffix[i] for each index, since combining the product of everything before i with the product of everything after i gives exactly the product of everything except nums[i] itself.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Solved cold, or needed a hint?

- [ ] Solved independently
- [X] Needed a hint
- [ ] Looked at the editorial/solution

## What I'd do differently next time

I would like to work on catching O(n) patterns faster, I felt very stuck at the start due to my code working but it being O(n^2). I'd also like to work on using array[-1] indices when I want "the most recent thing added". I think I could do better in solving code on paper by using different concepts and then cutting down the list by which is solved in O(n).

## Related problems

Other problems that use the same pattern (fill in as you notice repeats).