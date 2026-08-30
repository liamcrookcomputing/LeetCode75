# 345. Reverse Vowels of a String

|---|---|
| **Difficulty:** | Easy |
| **Pattern:** | Two Pointer / String |
| **Link:** | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75) |
| **Date solved:** | 2026-08-30 |

## Problem summary

Take the vowels in a string and reverse their placement, return the same sring with the new placement of the vowels.

## Scratch Notes (while solving)

> *Need to reverse just the vowels in a string, so first thought is grab the vowels somehow and then place them back reversed.*
>
> *tried vowels.find(s[i]) != 1 to check for vowels, this was wrong. find() returns the index or -1, not True/False, so checking != 1 doesn't actually catch non-vowels properly.*
>
> *tried s[i] = reverseStr, this doesn't work either, way too broad, was trying to assign the whole reversed string into one index.*
>
> *also got TypeError: str object does not support item assignment. strings are immutable, cant assign into them by index at all.*
>
> *fixed by collecting vowels into a list first, then looping through s again and using reverseStr[-1] + .pop() to place them back in reverse order. this worked but two full passes plus a list feels like more than necessary.*
>
> *43ms runtime, felt slow. this is actually a two pointers problem (LC75 category), not something I need two full passes for.*
>
> *rewrote with left/right pointers. first attempt had swap logic wrong:*
> ```
> tempStr = s[right]
> s[left] = s[right]
> s[left] = tempStr
> ```
> *this never actually writes into s[right], just overwrites s[left] twice. need proper 3-line swap order.*
>
> *also missed the elif branches for when only one side is a vowel, loop would never move left/right in that case, infinite loop risk.*
>
> *also hit the same string mutability issue again, s[left] = s[right] doesn't work on a string. converted to result = list(s), do the swaps on result instead of s, then "".join(result) at the end.*
>
> *final version passes. checking s[left]/s[right] instead of result[left]/result[right] for the vowel check works because s never gets modified, only result does, so reading from s stays accurate the whole time.*
>
> *runtime is now 15ms and I'm much happier with that result.*

## Approach

To solve this problem, I used the two pointer technique — one pointer (left) starting at the beginning of the string and one (right) starting at the end, moving toward each other.

Since strings are immutable in Python, I first converted s into result = list(s) so I'd be able to modify individual characters by index.

Inside a while left < right loop, I check three cases:

If both s[left] and s[right] are vowels, I swap them into result (result[left] = s[right], result[right] = s[left]), then move both pointers inward.
If s[left] is not a vowel, I move left forward without swapping.
If s[right] is not a vowel, I move right backward without swapping.

This way each pointer only advances past consonants and pauses on vowels, so a swap only happens when both sides are lined up on vowels. I used vowels = "aeiouAEIOU" and the in keyword to check membership in O(1), instead of a long chain of or comparisons.

I checked the vowel membership against s (the original, untouched string) rather than result, which is safe here since s itself is never modified — only result is written to — so reading from s throughout the loop stays accurate.

Finally, I joined result back into a string with "".join(result) and returned it.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Solved cold, or needed a hint?

- [ ] Solved independently
- [X] Needed a hint
- [ ] Looked at the editorial/solution

## What I'd do differently next time

I seem to struggle more with two pointer and string based problems, so I'll look more into these topics and practice them to better identify how to solve them.

## Related problems

Other problems that use the same pattern (fill in as you notice repeats).