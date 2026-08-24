# OSU Coursework

Coursework from Oregon State University's Computer Science M.Eng program (AI minor). Organized by course, then by assignment.

## Courses

| Course | Topic | Folder |
|---|---|---|
| AI 534 | Machine Learning | [ai534-machine-learning/](ai534-machine-learning/) |
| AI 531 | Agents, Search, and Reasoning | [ai531-agents-search-reasoning/](ai531-agents-search-reasoning/) |

## Structure convention

```
osu-coursework/
├── course-name/
│   ├── README.md              # course-level index of assignments
│   └── assignment-name/
│       ├── README.md          # problem statement, approach, results
│       ├── data/               # input data (where license/size permits)
│       ├── src/                 # all code (or flat, if the assignment's grading depends on it)
│       └── requirements.txt
```

Some assignments are kept flat (no `src/` subfolder) rather than split, when the provided test files import modules directly by name and are meant to be run from a single directory. This preserves the exact layout the assignment is graded in.
