---
description: Guidelines for creating and formatting different content types (syllabus, teacher guides, student guides, code examples)
alwaysApply: true
---

# Content Guidelines

## Content Types

This course repository includes four primary content types, each with specific purposes and formatting requirements:

1. **Syllabus** - The course map and schedule
2. **Teacher Guide** - Instructor-focused detailed guidance
3. **Student Guide** - Student-focused learning materials
4. **Example Code** - SQL scripts, reference code, and exercises

---

## 1. SYLLABUS

### Purpose
The syllabus is the master schedule and roadmap for the entire course. It shows what will be taught, when, and how long each session lasts.

### File Location
- `syllabus.md` (root level)

### Structure & Format

```markdown
# [Course Name]: [Duration] Syllabus

## Overview
- Brief description of course
- Target audience
- What students will learn (high level)
- Prerequisites (if any)

## Course Schedule

### Day 1: [Title]

#### Morning Session ([Start] - [End])
- **Topic Name** ([Time] - [Time])
  - Subtopic 1
  - Subtopic 2
  - Subtopic 3
- **Break** ([Time] - [Time])

#### Afternoon Session ([Start] - [End])
- **Topic Name** ([Time] - [Time])
- **Break** ([Time] - [Time])
- **Topic Name** ([Time] - [Time])

### Day 2: [Title]
[Same structure as Day 1]

### Day 3: [Title]
[Same structure as Day 1]

## Materials and Requirements
- List of materials
- Software requirements
- Hardware requirements
- Prerequisite knowledge

## Pre-course Setup (Optional)
- Pre-installation steps
- Pre-reading materials
```

### Content Guidelines
- **Timing**: Always include specific times (e.g., 9:00 - 10:30)
- **Break schedules**: Include breaks every 60-90 minutes
- **Topics in order**: List topics in presentation order
- **Granularity**: Break down into 30-60 minute chunks
- **Subtopics**: Use bullet points for main concepts within each topic
- **Total course hours**: Should add up correctly (e.g., 3 days × 7.5 hours)

### Required Sections
- ✓ Overview
- ✓ Schedule (by day and session)
- ✓ Materials and Requirements
- ✓ Pre-course Setup

---

## 2. TEACHER GUIDE

### Purpose
Teacher guides provide instructors with detailed content, teaching strategies, timings, facilitation notes, and answers. These are NOT given to students.

### File Location
- `Teacher_Guides/Day_[1/2/3]_Teacher_Guide.md`

### Structure & Format

```markdown
# Day [1/2/3] Teacher Guide: [Topic]

## Overview
- Learning objectives (specific)
- What students should be able to do by end of day
- Prerequisites students should have

## Day Schedule
- Topic breakdown with times
- Suggested break times
- Transitions between topics

## [Topic Name] - [Time allocation]

### Learning Objectives
- Specific learning outcome 1
- Specific learning outcome 2
- Specific learning outcome 3

### Content Delivery
- Key concepts to cover
- Common misconceptions students have
- Tips for explaining effectively
- Real-world examples to use

### Hands-On Exercise: [Exercise Name]
- Exercise number and name
- Objectives for exercise
- How long it should take
- Setup instructions
- Common student mistakes and how to help
- Success criteria

### Facilitation Notes
- What students typically struggle with
- Pacing tips
- Questions to engage students
- When to pause for questions

## Troubleshooting Guide

### "Students struggle with [concept]"
**Why it's hard**: Explanation
**How to help**: Teaching strategy
**Alternative approach**: Different way to explain

## Answer Key / Solutions

### Exercise [Number]: [Name]
[Complete solution with explanations]

### Quiz/Assessment Questions
[Question 1]: [Answer with explanation]
[Question 2]: [Answer with explanation]

## Timing Summary
- Total day time: X hours
- Instruction: X hours
- Exercises: X hours
- Breaks: X hours
- Contingency: X hours

## Materials Needed
- Equipment/software
- Files to have open
- Projector/screen setup
- Student handouts
```

### Content Guidelines
- **Detailed**: More detailed than student materials
- **Answers included**: Full solutions and explanations
- **Teaching strategies**: Practical tips for instructors
- **Timing estimates**: How long each section actually takes
- **Contingency**: Notes on what to cut if behind schedule
- **Q&A**: Common student questions and answers
- **Troubleshooting**: Common problems and solutions

### Required Sections
- ✓ Overview with objectives
- ✓ Day schedule/timing
- ✓ Content breakdown by topic
- ✓ Exercises with facilitation notes
- ✓ Answer keys/solutions
- ✓ Troubleshooting guide
- ✓ Timing summary

---

## 3. STUDENT GUIDE

### Purpose
Student guides help learners navigate the course, understand how to approach learning, access resources, and troubleshoot common issues.

### File Locations
- `Student_Guides/Getting_Started.md` - How to set up and begin
- `Student_Guides/[Topic]_Guide.md` - Topic-specific guidance (e.g., Installation_Guide.md)
- `Day[1/2/3]/README.md` - Day overview (student-facing)

### Structure & Format

```markdown
# [Topic] Guide for Students

## Overview
- What you'll learn
- Why this matters
- How this fits into the course

## Getting Started
- Prerequisites
- What you need before starting
- Setup steps (numbered)

## Learning Path
- Concepts in order
- How they build on each other

## Step-by-Step: [Main Topic]
### Step 1: [Concept/Action]
- Explanation
- Why this matters
- Example or code snippet
- Try it yourself

### Step 2: [Concept/Action]
[Same format]

## Hands-On Exercises
- Exercise 1: [Name] - What you'll learn
- Exercise 2: [Name] - What you'll learn
- Exercises are in the `exercises/` folder
- Solutions are available after you try

## Common Questions

**Q: [Student question]?**
A: [Clear answer]

**Q: [Student question]?**
A: [Clear answer]

## Troubleshooting

### Problem: [Common issue]
**Error you might see**: [Error message]
**Solution**: [Step by step fix]

## Next Steps
- What to do after completing this topic
- How this leads into next topic
- Resources for going deeper

## Helpful Resources
- Links to reference materials
- External tutorials
- Community forums/help
```

### Content Guidelines
- **Student-friendly**: Written for learners, not experts
- **Encouraging**: Positive, supportive tone
- **Practical**: Focus on "how to do" not just "why"
- **Examples**: Include working examples students can reference
- **Troubleshooting**: Anticipate student problems
- **No answers**: Exercise solutions are separate, not in guide
- **Clear instructions**: Step-by-step without assuming knowledge

### Required Sections
- ✓ Overview
- ✓ Getting Started / Prerequisites
- ✓ Step-by-step content
- ✓ Hands-on exercises (referenced, not solved)
- ✓ Common questions
- ✓ Troubleshooting
- ✓ Next steps

---

## 4. EXAMPLE CODE (SQL, Scripts, etc.)

### Purpose
Example code demonstrates concepts, serves as reference material, and provides working templates for students to learn from and modify.

### File Types
- `[topic].sql` - SQL examples and reference code
- `[topic]_exercise.sql` - Starter code for exercises
- `[topic]_solution.sql` - Complete solutions
- `[topic].sh` - Shell scripts (bash)

### Structure & Format

```sql
-- ========================================
-- [Topic Name]
-- Course: [Course Name]
-- Day [X]
-- ========================================
-- Description: What this file demonstrates
-- Learning objectives:
--   - Objective 1
--   - Objective 2
-- ========================================

-- Section 1: [Concept Name]
-- Explanation of what you're about to see
-- Why this pattern is useful

-- Example 1.1: [Specific example]
SELECT column1, column2 
FROM table_name
WHERE condition = true;

-- Example 1.2: [Another variation]
SELECT column1, column2 
FROM table_name
WHERE condition = false;

-- Section 2: [Next concept]
-- More explanation...

-- Example 2.1: [Specific example]
-- Your code here
```

### Code Guidelines

#### Comments
- **Header comment**: At the top, explains the file's purpose
- **Section comments**: Explain each major section
- **Example comments**: Describe what each query demonstrates
- **Inline comments**: Explain non-obvious code (but keep code readable!)

#### Organization
- **Logical flow**: Build from simple to complex
- **Related examples**: Group similar patterns
- **Clear sections**: Use comments to separate topics
- **Example numbering**: Number examples (1.1, 1.2, 2.1, etc.)

#### Content
- **Explain concepts**: Brief explanation of what/why before the code
- **Real examples**: Use realistic data/scenarios
- **Best practices**: Show recommended patterns
- **Variations**: Show multiple ways to solve the same problem
- **Errors to avoid**: Show common mistakes
- **Variable naming**: Use clear, descriptive names

#### Files Organization
- **One topic per file** (e.g., joins.sql, aggregates.sql)
- **Keep under 500 lines** (split larger topics)
- **Runnable code**: Code should execute without errors
- **Sample data**: If needed, include sample data creation

### Required Elements for Each Code File
- ✓ Header comment with purpose
- ✓ Learning objectives
- ✓ Section organization with comments
- ✓ Multiple examples per concept
- ✓ Explanation before code
- ✓ Clear variable/table names
- ✓ Comments for non-obvious logic

### Exercise File Format

```sql
-- ========================================
-- [Topic] Exercise
-- Course: [Course Name]
-- Day [X]
-- ========================================
-- Instructions: What to do
-- Expected outcome: What success looks like
-- Difficulty: Easy / Medium / Hard
-- Time estimate: X minutes
-- ========================================

-- [Background/context if needed]

-- [Partial code or questions to guide student]
-- Your code here:

-- Hint (uncomment if needed):
-- -- Use a JOIN to combine tables

-- When you're done:
-- - Verify your code runs without errors
-- - Check that results match expected output
-- - Compare with solution when ready
```

### Solution File Format

```sql
-- ========================================
-- [Topic] Exercise - SOLUTION
-- Course: [Course Name]
-- Day [X]
-- ========================================

-- Solution explanation (commented):
-- This solution uses [approach] because [reason]
-- Alternative approach: [brief mention]

-- Complete solution:
[Full code]

-- Explanation of key parts:
-- [Optional: explain tricky sections]

-- Common mistakes to avoid:
-- - Mistake 1: What goes wrong and why
-- - Mistake 2: What goes wrong and why
```

---

## Quality Standards Across All Content

### Writing Quality
- ✓ Clear, concise language
- ✓ Consistent terminology
- ✓ Proper grammar and spelling
- ✓ Appropriate tone for audience (teacher vs student)

### Completeness
- ✓ All required sections included
- ✓ No dead links or references
- ✓ All code examples are tested/working
- ✓ All exercises have solutions

### Consistency
- ✓ Naming conventions followed
- ✓ File structure matches standards
- ✓ Formatting is consistent with other days/topics
- ✓ Learning objectives align with syllabus

### Accessibility
- ✓ Clear headings and structure
- ✓ Accessible language (avoid jargon without explanation)
- ✓ Code is readable and not overly complex
- ✓ Multiple examples for difficult concepts

---

## Cross-Content References

When creating materials, reference other content appropriately:

- **Syllabus → Teacher Guide**: "See Day 2 morning session in syllabus"
- **Teacher Guide → Student Guide**: "Students can find more details in Student_Guides/"
- **Guides → Code Examples**: "See Day1/joins.sql for examples"
- **Exercises → Solutions**: "Solutions are in Day1/solutions/"

Maintain these references in both directions when content changes.