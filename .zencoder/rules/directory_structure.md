---
description: Directory structure and file organization standards for course repositories
alwaysApply: true
---

# Directory Structure & File Organization

## Overview
Course repositories follow a standardized directory structure to keep materials organized and easily accessible for students and instructors.

## Standard Directory Layout

```
course-repository/
├── README.md                          # Course overview and quick start
├── syllabus.md                        # Complete course schedule and content map
├── description.txt                    # Brief course description for marketing
├── marketing_document.md              # Marketing/promotional content
│
├── Day1/                              # Day 1 materials
│   ├── README.md                      # Day overview and learning objectives
│   ├── [topic_1].sql                  # SQL example code
│   ├── [topic_2].sql                  # SQL example code
│   ├── [topic]_reference.md           # Reference guides (data types, syntax, etc.)
│   ├── [topic]_guide.md               # Installation/setup guides
│   ├── [topic].sh                     # Bash scripts (installation, setup)
│   ├── exercises/
│   │   ├── exercise_[number].sql      # Student exercises
│   │   ├── exercise_[number]_solution.sql
│   │   └── README.md                  # Exercise instructions
│   └── solutions/
│       └── [exercise_name]_solution.sql
│
├── Day2/                              # Day 2 materials
│   ├── README.md
│   ├── [topic].sql
│   ├── [topic]_guide.md
│   ├── exercises/
│   │   ├── exercise_[number].sql
│   │   ├── exercise_[number]_solution.sql
│   │   └── README.md
│   └── solutions/
│       └── [exercise_name]_solution.sql
│
├── Day3/                              # Day 3 materials
│   ├── README.md
│   ├── [topic].sql
│   ├── [topic]_guide.md
│   ├── exercises/
│   │   ├── exercise_[number].sql
│   │   ├── exercise_[number]_solution.sql
│   │   └── README.md
│   ├── solutions/
│   │   └── [exercise_name]_solution.sql
│   ├── project/                       # Capstone/final project
│   │   ├── README.md
│   │   ├── starter_code/
│   │   ├── solution/
│   │   └── requirements.md
│   └── rest_api_project/              # (if applicable - API project)
│       ├── README.md
│       ├── package.json               # Node.js version
│       ├── server.js
│       ├── db.js
│       ├── routes/
│       ├── python_version/
│       │   ├── server.py
│       │   └── requirements.txt
│       └── .env.example
│
├── Teacher_Guides/                    # Instructor materials
│   ├── Day_1_Teacher_Guide.md
│   ├── Day_2_Teacher_Guide.md
│   ├── Day_3_Teacher_Guide.md
│   ├── answer_keys/
│   │   ├── Day_1_Answer_Key.md
│   │   ├── Day_2_Answer_Key.md
│   │   └── Day_3_Answer_Key.md
│   └── facilitation_notes.md
│
├── Student_Guides/                    # Student resources
│   ├── Getting_Started.md
│   ├── Troubleshooting.md
│   ├── Resource_Links.md
│   └── setup_checklist.md
│
├── resources/                         # Shared resources
│   ├── glossary.md
│   ├── templates/
│   ├── sample_data/
│   └── reference_materials/
│
├── .zencoder/rules/                   # AI assistant rules
│   ├── repo.md
│   ├── directory_structure.md
│   ├── content_guidelines.md
│   ├── content_templates.md
│   └── code_standards.md
│
└── .env.example                       # Environment variables template
```

## Naming Conventions

### File Naming
- **Spaces**: Use underscores or hyphens, not spaces
- **Case**: Use lowercase with underscores
- **SQL Files**: `topic_name.sql` or `day_1_topic.sql`
- **Exercise Files**: `exercise_01.sql`, `exercise_02_solution.sql`
- **Documentation**: `descriptive_name.md`
- **Scripts**: Use `.sh` for shell scripts

### Folder Naming
- **Days**: `Day1`, `Day2`, `Day3` (capitalized, no underscores)
- **Subdirectories**: `lowercase_with_underscores` or `camelCase`
- **Special folders**: `Teacher_Guides`, `Student_Guides` (underscores for multi-word folders)

## File Organization Rules

### By Day
Each day's materials are self-contained in their own directory:
- Related SQL files are grouped together
- Exercises have their own `exercises/` subfolder
- Solutions are in `solutions/` subfolder or paired with exercises

### By Content Type
- **Code files**: Grouped by topic/subject
- **Documentation**: All `.md` files at appropriate level
- **Resources**: Shared resources in top-level `resources/` folder
- **Student vs Teacher**: Separate `Student_Guides/` and `Teacher_Guides/` directories

### By Audience
- **Public materials**: Top level (README, syllabus, student guides)
- **Instructor only**: `Teacher_Guides/` folder
- **Student materials**: Either top-level or in specific day folders

## File Size Guidelines
- SQL files: Keep under 500 lines (break large files into topics)
- Markdown docs: Keep under 1000 lines (consider splitting into multiple files)
- Code examples: Keep focused on single concepts
- Exercises: Provide incremental difficulty (Easy → Medium → Hard)

## Documentation at Each Level

### Root Level
- `README.md`: Course overview and how to navigate materials
- `syllabus.md`: Complete schedule with timing and topics

### Day Folders
- `README.md`: Day objectives, schedule, and quick navigation

### Exercise Folders
- `README.md`: Instructions for all exercises in that section

### Solution Folders
- Clearly labeled with `_solution` suffix
- Include comments explaining key concepts

## Directory Structure Checklist

When creating or updating a course repo, verify:
- [ ] Day folders follow Day1, Day2, Day3 naming
- [ ] Each day has a README.md
- [ ] Exercises and solutions are in separate subfolders
- [ ] Files follow naming conventions (lowercase, underscores)
- [ ] Teacher guides are in Teacher_Guides/ folder
- [ ] Student guides are in Student_Guides/ folder
- [ ] .zencoder/rules/ directory exists with governance files
- [ ] Resources are organized logically
- [ ] No spaces in filenames
- [ ] Related files are grouped in appropriate folders

## Important Notes
- Maintain consistency across all 3 course repositories
- Nested deeply (more than 4 levels) should be avoided
- Use README.md files as navigation aids within folders
- Keep file naming consistent across similar content types