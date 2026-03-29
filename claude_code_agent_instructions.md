# Claude Code Agent Instructions: Spelling & Consistency Checker

## Overview
This guide explains how to create a specialized sub-agent in Claude Code that corrects spelling mistakes and identifies inconsistencies in text documents, particularly useful for reviewing interview prep materials, documentation, and problem solutions.

## Creating the Agent

### Option 1: Using Task Tool with Specialized Sub-Agent (Recommended)

Claude Code allows you to launch specialized agents using the `Task` tool. While there isn't a built-in "spelling-checker" agent type, you can use the `general-purpose` agent with specific instructions.

**Example invocation:**

```python
# From within Claude Code, you would call:
Task(
    subagent_type="general-purpose",
    description="Check spelling and consistency",
    prompt="""Please review the following file for spelling mistakes and consistency issues:

File: {file_path}

Tasks:
1. Identify and correct all spelling mistakes
2. Check for consistency in:
   - Technical terminology (e.g., "LeetCode" vs "Leetcode")
   - Capitalization patterns
   - Hyphenation (e.g., "sub-agent" vs "subagent")
   - Number formatting (e.g., "8-week" vs "eight week")
   - Code formatting in markdown (backticks usage)

3. Look for common issues:
   - Repeated words ("the the")
   - Missing punctuation
   - Inconsistent tense usage
   - Subject-verb agreement
   - Missing articles (a, an, the)

4. Return a detailed report with:
   - List of spelling errors with corrections
   - List of inconsistencies with suggested fixes
   - Line numbers for each issue
   - Severity level (critical/minor)

Do NOT make changes directly. Only provide the report for human review.
"""
)
```

### Option 2: Creating a Custom Slash Command

Create a reusable slash command for spell checking by adding a file to `.claude/commands/`:

**File: `.claude/commands/spell-check.md`**

```markdown
Review the currently open file (or file specified as argument) for:

1. **Spelling Mistakes**
   - Use context-aware spell checking
   - Recognize technical terms and proper nouns
   - Flag potential typos

2. **Consistency Issues**
   - Terminology consistency across the document
   - Capitalization patterns
   - Formatting consistency (markdown, code blocks)
   - Number and date formatting
   - Hyphenation and compound words

3. **Grammar & Style**
   - Subject-verb agreement
   - Tense consistency
   - Article usage (a/an/the)
   - Repeated words or phrases

**Output Format:**
Present findings in a structured markdown report:

## Spelling Errors
- Line {X}: "{incorrect}" → "{correct}" (Reason)

## Consistency Issues
- Line {X}: Issue description with suggestion

## Grammar Issues
- Line {X}: Issue description with correction

**Important:**
- Recognize domain-specific terms (LeetCode, FAANG, NeetCode, etc.)
- Consider markdown formatting as intentional
- Don't flag code blocks or technical syntax
- Group related issues together
- Prioritize critical issues over minor style preferences
```

**Usage:** `/spell-check path/to/file.md`

### Option 3: Interactive Review Workflow

For reviewing multiple files, create a workflow slash command:

**File: `.claude/commands/review-docs.md`**

```markdown
Perform a comprehensive documentation review of files matching the pattern provided as argument (default: **/*.md in current directory).

For each file:
1. Read the file content
2. Check for spelling and consistency issues
3. Present findings file-by-file
4. Ask user if they want to apply corrections or skip to next file
5. If approved, apply corrections using Edit tool
6. Track progress with TodoWrite

Focus areas:
- Spelling mistakes
- Technical term consistency
- Markdown formatting consistency
- Grammar and style
- Code block formatting

Present each file's issues before making changes and wait for approval.
```

## Best Practices for Spelling & Consistency Checking

### 1. Context-Aware Checking

**Recognize domain-specific vocabulary:**
- LeetCode, NeetCode (not Leetcode, leetcode)
- FAANG (Facebook/Meta, Apple, Amazon, Netflix, Google)
- ML/AI terms: "hyperparameter", "backpropagation", "overfitting"
- Technical patterns: "O(n)", "two-pointer", "DFS/BFS"

### 2. Consistency Rules for This Repository

Based on the codebase style:

**Terminology:**
- "LeetCode" (not "Leetcode" or "leetcode")
- "FAANG" (all caps)
- "ML" or "Machine Learning" (be consistent within document)
- "two-pointer" (hyphenated)
- "time complexity" (lowercase unless starting sentence)

**Formatting:**
- Use code backticks for: variable names, function names, file paths
- Use "**bold**" for emphasis, not ALL CAPS
- Use numbered lists for sequential steps
- Use bullet points for non-sequential items

**File naming:**
- Use underscores: `problem_name.py`, `system_design.md`
- Numbers first: `242_valid_anagram.py`
- Lowercase for files, proper case in documentation

### 3. Common Pitfalls to Avoid

**Don't flag as errors:**
- Technical syntax: `O(n log n)`, `nums[i]`
- Code in markdown: `` `class Solution:` ``
- Intentional capitalization: "STAR method", "README"
- Domain acronyms: BFS, DFS, DP, etc.

**Do flag:**
- Inconsistent capitalization of same term within document
- Actual misspellings: "algoritm" → "algorithm"
- Grammar errors: "problems requires" → "problem requires"
- Repeated words: "the the solution"

## Example Agent Workflow

Here's how you might use an agent to check a specific file:

```markdown
User: "Check the behavioral prep file for spelling mistakes"

Claude: I'll launch a general-purpose agent to review the behavioral prep file for spelling and consistency issues.

[Uses Task tool with detailed prompt]

Agent returns:
---
## Spelling & Consistency Report: google_behavioral_prep.md

### Spelling Errors (2)
- Line 45: "acomplish" → "accomplish"
- Line 112: "colaboration" → "collaboration"

### Consistency Issues (4)
- Lines 23, 56, 89: Inconsistent use of "Google" vs "GOOGLE" (recommend: "Google")
- Line 34, 67: Mix of "ML" and "Machine Learning" (recommend: pick one)
- Line 78: "2 weeks" vs Line 90: "two weeks" (recommend: "2 weeks" for consistency)

### Grammar Issues (1)
- Line 101: "The team were" → "The team was" (collective noun)

### Total Issues: 7 (3 critical, 4 minor)
---

Claude: I found 7 issues in the file. Would you like me to apply these corrections, or would you prefer to review them individually first?
```

## Advanced: Batch Processing

For checking multiple files at once:

```markdown
# In your prompt to Claude:
"Use an agent to check all markdown files in one_last_mile/behavioral_prep/
for spelling and consistency issues. Create a summary report showing issues
per file, then let me decide which files to fix."

# Claude would:
1. Use TodoWrite to plan the task
2. Launch agent with glob pattern for all .md files
3. Agent processes each file
4. Returns consolidated report
5. Claude presents findings and awaits instructions
```

## Integration with Your Workflow

### Pre-commit Check
You could create a slash command that checks modified files:

```bash
# .claude/commands/pre-commit-check.md
Run spell and consistency checks on all modified files (git diff --name-only).

For each modified file:
1. Check spelling and consistency
2. Report issues found
3. Ask if user wants to fix before committing

This helps catch errors before they're committed to the repository.
```

### Documentation Review Process
When completing ML prep problems:

1. Write solution and documentation
2. Run `/spell-check` on the new markdown file
3. Review and apply suggested corrections
4. Commit with clean documentation

## Custom Dictionary

Maintain a list of project-specific terms that should NOT be flagged:

**Technical Terms:**
- LeetCode, NeetCode, HackerRank
- FAANG, MANGA
- HashMap, TreeSet, LinkedList (as single words)
- backtracking, memoization
- subarray, substring, subsequence

**Problem Patterns:**
- two-pointer, sliding-window
- top-k, k-way
- in-place, in-order

**ML Terms:**
- hyperparameter, gradient descent
- overfitting, underfitting
- precision-recall
- train-test split

## Measuring Success

A good spelling & consistency checker should:
- ✅ Catch actual spelling mistakes
- ✅ Identify inconsistent terminology usage
- ✅ Respect technical/domain-specific terms
- ✅ Provide clear, actionable suggestions
- ✅ Include line numbers for easy navigation
- ✅ NOT flag code syntax or intentional formatting
- ✅ Distinguish between critical and minor issues

## Limitations

**What Claude Code agents CAN do:**
- Read and analyze text files
- Identify patterns and inconsistencies
- Provide detailed reports with suggestions
- Apply corrections with Edit tool when approved

**What they CANNOT do:**
- Run external spell-check libraries
- Access user dictionaries from OS
- Perform real-time checking as you type
- Auto-fix without human approval (by design)

## Conclusion

Creating a spelling and consistency checker in Claude Code is best accomplished using:
1. **Task tool** for one-off reviews with custom instructions
2. **Slash commands** for reusable workflows
3. **General-purpose agents** with detailed prompting

The key is providing clear, context-aware instructions that respect the technical nature of your documentation while catching genuine errors and inconsistencies.

---

**Next Steps:**
1. Create a `/spell-check` slash command using the template above
2. Test it on a sample file from your repository
3. Refine the custom dictionary based on false positives
4. Integrate into your documentation workflow
