# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is "Coding-Conquest" - a comprehensive collection of programming solutions and interview preparation materials with two main focus areas:

1. **LeetCode Problem Solutions** (`/leet_code/`) - 150+ algorithmic problems with Python implementations and detailed documentation
2. **FAANG ML Engineering Interview Prep** (`/one_last_mile/`) - Systematic preparation materials for Machine Learning Engineer positions

## Development Commands

**No build system or dependencies** - This is a pure Python repository without external dependencies.

**Git workflow:**
- Use conventional commit format: `[Type]: Description`  
- Common types: `[Feat]`, `[Docs]`, `[Refactor]`
- Include problem numbers and context in commit descriptions
- Never include Claude Code attribution in commits (user preference)

## Code Architecture

### LeetCode Solutions (`/leet_code/`)
- **Pattern**: Each problem has both `.py` implementation and `.md` documentation
- **Naming**: `{problem_number}_{problem_name}.py` and corresponding `.md`
- **Structure**: `scripts/` for code, `docs/` for documentation
- **Approach**: Show multiple solutions (brute force → optimized) with complexity analysis

### ML Interview Prep (`/one_last_mile/`)
- **Organized by interview type**: `coding_problems/`, `system_design/`, `behavioral_prep/`, `ml_fundamentals/`
- **Template-driven**: Standardized templates for system design, behavioral interviews, and problem documentation
- **Progress tracking**: `problem_categories.md` tracks completion status
- **Personal note style**: Documentation written in first person as study notes

### Code Conventions
```python
class Solution:
    def problemName(self, params) -> return_type:
        # Approach explanation
        # Implementation with detailed comments
```

## Key Files for ML Interview Prep

- `one_last_mile/README.md` - Complete 8-week interview prep timeline
- `one_last_mile/coding_problems/problem_categories.md` - Problem progress tracker  
- `one_last_mile/system_design/ml_systems_template.md` - ML system design framework
- `one_last_mile/behavioral_prep/star_template.md` - STAR method and company principles

## Documentation Standards

**For LeetCode problems:**
- Include intuition, approach, complexity analysis (with LaTeX notation: `$$O(n)$$`)
- Show code with extensive comments
- Multiple solution approaches when applicable

**For ML prep problems:**
- Write in first person ("My approach", "What I learned")
- Include working code solutions
- Explain key insights and problem-solving thought process
- Organize by NeetCode 150 categories in subdirectories

## Special Patterns

1. **Problem categorization**: ML coding problems organized into subdirectories like `arrays_and_hashing/`
2. **Constraint optimization**: When problems specify limited character sets (e.g., "lowercase English letters"), use fixed-size arrays for O(1) space
3. **Multiple approaches**: Always consider brute force, then optimize (document both)
4. **Progress tracking**: Update category checklists when completing problems

## Working with this Repository

- **Adding LeetCode solutions**: Create both `.py` and `.md` files following naming conventions
- **ML prep problems**: Organize into appropriate category subdirectories, update progress tracker
- **System design**: Use provided templates and frameworks
- **Testing**: No formal test framework - include examples and test cases in code comments