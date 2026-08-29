# 1071. Greatest Common Divisor of Strings

|---|---|
| **Difficulty:** Easy |
| **Pattern:** String / Math |
| **Link:** | [Greatest Common Divisor](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75) |
| **Date solved:** | 2026-08-29 |

## Problem summary

Find the greatest common divisor across two strings and return the result.

## Scratch Notes (while solving)

> *Using the `/` operand doesn't work on strings.*
> *So maybe we can use the same thing we did before where we get the elements and then compare them.*
> *Then we check if the answer = t + t. If not, continue with the loop.*
>
> *I think I'm thinking of this in the wrong way — I need to get the common divisor between them, rather than have them divide each other.*
>
> *So I need to get the result and check between both:*
> ```
> result = ''
> for x in range(len(str1)):
>     result += str1[x]
>     if result == str2:
>         if str1 == str2 + str2:
>             print(result)
>             return result
> ```
> *This worked for test case 1, but stops working because it doesn't grab the greatest common divisor.*
>
> *Moving to change `result * 2` and checking it against str1 OR str2 to ensure we get the greatest common divisor, then creating an elif statement to return "" if the check resulted in nothing.*
>
> *Submitted but failed on test case 25/129 — simply because `result * 2` didn't equal either string. Maybe I need a for loop to check through possible combinations, but this would increase time complexity.*
>
> *Used a hint — problem is I'm only checking for str1 prefix and not str2 prefix as well. If at any point str1 and str2 prefixes don't match and the GCD has not been found, then we should return "".*
>
> *My main trouble is finding out how to ensure that the GCD checks through the strings reliably.*
>
> *Asked Claude for an explanation (not to generate code). It led me toward checking `str1 + str2` against `str2 + str1` — if they aren't the same, a GCD doesn't exist between them. After confirming a GCD exists, I need to find the largest and lowest length, which lets me use `math.gcd()` and return `str1[:math.gcd(maxLength, minLength)]`. If no GCD exists, return "".*
>
> *Turns out I was overcomplicating this and didn't need a for loop at all.*

## Approach

To solve this problem, I first needed to figure out if a common divisor even exists between str1 and str2. I checked this by comparing str1 + str2 against str2 + str1 — if concatenating them in either order doesn't produce the same result, there's no shared repeating block between them, so no GCD exists and I return "".

Once I confirmed a GCD exists, I used len() to find which string was longer and which was shorter, storing those as maxLength and minLength.

Then I used math.gcd(maxLength, minLength) to get the length of the greatest common divisor string — this treats the problem as finding the GCD of the two string lengths as integers, rather than trying to build or compare candidate strings manually.

Finally, I sliced str1 from the start up to that GCD length (str1[:math.gcd(maxLength, minLength)]) to get the actual answer string, since the GCD string will always be the prefix of both str1 and str2 once you know a common divisor exists.

The key realization was that this wasn't a string-comparison problem so much as a number-theory problem in disguise — once I knew a common divisor existed, finding its length was just the GCD of two integers (len(str1) and len(str2)), not something I needed a loop to search for.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Solved cold, or needed a hint?

- [ ] Solved independently
- [x] Needed a hint
- [ ] Looked at the editorial/solution

## What I'd do differently next time

I struggled a lot with this one in the sense of working on the right thing. I spent a little bit of time away from the code and actually wrote what I needed to do on paper which helped out a lot. So for my next tasks I'll give myself some time to write down what I need to do on paper and hopefully that'll help me out later. I'd also look more into python libraries as I used the math library for this problem and it is likely that libraries would be used in real world production programs.

## Related problems

Other problems that use the same pattern (fill in as you notice repeats).