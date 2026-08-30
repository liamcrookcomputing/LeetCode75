# 151. Reverse Words in a String

|---|---|
| **Difficulty:** | Medium |
| **Pattern:** | Two Pointers / String |
| **Link:** | [link](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75) |
| **Date solved:** | 2026-08-30 |

## Problem summary

Reverse the order in which words are outputted with only a single space to separate them.

## Scratch Notes (while solving)

> *thinking about using the sentinel value trick from Can Place Flowers, padding the string somehow so I don't have to special case the start/end.*
>
> *actually don't want to do that here, feels like it's adding complexity instead of removing it for this problem, going to try tracking left/right manually instead.*
>
> *set left and right both starting at len(s) - 1, scanning backwards since I want the reversed word order.*
>
> *got a syntax error trying to slice with s[left]:s[right], forgot slice needs to be inside one set of brackets, s[left:right+1] not s[left]:s[right]. also needed the +1 since slicing is exclusive on the end.*
>
> *words weren't appending right, last word in the string kept getting dropped.*
>
> *messing around with where left -= 1 goes, tried moving it inside the if block first, then also having it outside, wasn't sure if I needed it twice.*
>
> *realized the while condition was the actual problem, I had while left > 0 originally, which stops the loop before left ever reaches 0, so the very last word (the one starting at index 0) never gets a chance to be checked. changed to while left >= 0 and that fixed it.*
>
> *works now but only beats 5% of submissions, feels like the double left -= 1 and repeated s[left+1] checks are doing more work than needed, want to look into a cleaner way to do this.*

## Approach

To solve this problem, I used two pointers, left and right, both starting at the last index of the string, and scanned backward toward the front.

The idea was to find the boundaries of each word by checking: is the current character (s[left] and s[right]) not a space, is the character just before left a space (or left is at index 0, meaning the start of the string), and is the character just after right a space (or right is at the last index, meaning the end of the string). When all of those are true, s[left] and s[right] mark the start and end of a word, so I slice it out with s[left:right+1] (the +1 is needed since slicing is exclusive on the end) and append it to reverseWords.

After checking (and possibly appending) at a position, I move left backward by one. Then I check if s[left+1] is a space — if it is, that means right needs to jump back to line up with the new left, ready to find the next word.

Since I'm scanning from the end of the string toward the front and appending each word as I find it, the words naturally end up in reverseWords in reversed order without needing an extra reversal step at the end.

Finally, I joined reverseWords with " ".join(reverseWords) and returned it.

One bug I hit along the way: my original while left > 0 condition stopped the loop one iteration too early, so the very first word in the string (the one starting at index 0) never got checked or appended. Changing it to while left >= 0 fixed it, since it allowed left to actually reach and process index 0 before the loop ended.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Solved cold, or needed a hint?

- [X] Solved independently
- [ ] Needed a hint
- [ ] Looked at the editorial/solution

## What I'd do differently next time

Looking at the other solutions, there is a .split() function that takes the words and removes the whitespace automatically. Worth trying to remember for the next time I do this problem as it seems to be incredibly efficient compared to what I wrote.

## Related problems

Other problems that use the same pattern (fill in as you notice repeats).