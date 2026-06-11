---
name: format-problem-set
description: Use when given raw copy-pasted problem set text (from CodePath, LeetCode, HackerRank, etc.) and asked to create a structured markdown file. Triggers on phrases like "make a problem set", "format this into markdown", "create a problem file", or when raw problem text is pasted alongside a request to save/format it.
---

# Format Problem Set

## Overview

Convert raw copy-pasted problem text into a clean, structured markdown file formatted like a HackerRank/CodePath problem set. One problem per `##` section, consistent structure throughout.

## Output File Location

Save to the most relevant path in the project. Default:
```
week-XX/day-XX/prob-set-XX/problem-set.md
```
Ask user if path is unclear.

## Markdown Template

```markdown
# Problem Set: [Topic] — Week X, Day X

---

## Problem N: [Title]

**Difficulty:** Easy / Medium / Hard

### Description

[Problem description written in second-person, present tense. Clean prose, no raw formatting artifacts from the source.]

**A solution is considered valid if:**
- Condition 1
- Condition 2

### Function Signature

```python
def function_name(param: type) -> return_type:
    pass
```

### Examples

**Example 1:**
```
Input:  ...
Output: ...
```

**Example 2:**
```
Input:  ...
Output: ...
```

### Constraints

- Constraint 1 (if stated)

---
```

## Rules

1. **Strip noise** — remove emoji, hints, raw `print()` calls used as examples, duplicate blank lines, broken formatting from copy-paste
2. **No hints section** — drop all `💡 Hint` and `✨ AI Hint` content entirely
3. **Normalize examples** — convert `print(func(args))` → `Output: result` format
4. **One file, all problems** — don't split into separate files unless user asks
5. **Infer difficulty** if not stated — Easy for direct lookups, Medium for two-pointer/stack, Hard for complex logic
6. **Keep function signature** exactly as given — don't rename params or change types
7. **Starter code** — if a problem asks to "add comments to existing code", include the full code block under a `### Starter Code` section

## Common Mistakes

- Leaving raw `print(func(...))` calls instead of formatting as Input/Output examples
- Including hints — drop them always
- Forgetting the `---` horizontal rule between problems
- Writing file to wrong week/day directory — confirm with user if unsure
