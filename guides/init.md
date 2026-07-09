# Init Guide — Scaffold Beamer Project with Theme

## Instructions for Claude

You are setting up a Beamer slides project with the Beamer Style theme system.

### Arguments

- `--theme NAME`: one of red, blue, gold, green, purple. Default: blue.
- `--layout NAME`: one of metropolis, minimal, classic, focus, research. Default: metropolis.

### Steps

1. **Detect target directory.** If the project has a `slides/` directory, use it.
   Otherwise ask: "Should I create a `slides/` directory, or place files in the project root?"

2. **Check for existing files.** Look for `beamer-colors.tex`, `layout-*.tex` in the target.
   - If any exist, ask: "Found existing {files}. Overwrite, backup (.bak), or abort?"
   - Respect the user's choice.

3. **Copy color template.** From this skill's `templates/` directory, copy to the target:
   - `beamer-colors.tex`

4. **Set the theme.** In the copied `beamer-colors.tex`, change the
   `\newcommand{\beamerthemename}{...}` line to the requested theme name.

5. **Copy layout template.** From this skill's `templates/` directory, copy:
   - `layout-{layout}.tex` → target directory (keep the original filename)

6. **Create a starter main.tex** (only if no `.tex` file exists in target). Use this template:

   ```latex
   \documentclass[aspectratio=169,10pt]{beamer}

   \usepackage{amsmath,amssymb,booktabs,mathtools}
   \usepackage{graphicx,hyperref}
   \usepackage{tikz}
   \usetikzlibrary{arrows.meta,positioning}

   % Theme colors (switch theme in beamer-colors.tex)
   \input{beamer-colors}

   % Layout (swap layout-*.tex file to change layout)
   \input{layout-{layout}}

   \title{Title}
   \subtitle{Subtitle}
   \author{Presenter: [Name]}
   \institute{Shanghai Jiao Tong University}
   \date{\today}

   \begin{document}

   \begin{frame}[plain]
     \titlepage
   \end{frame}

   \begin{frame}{Outline}
     \tableofcontents
   \end{frame}

   \section{Introduction}

   \begin{frame}{Introduction}
     Content here.
   \end{frame}

   \begin{frame}[plain,noframenumbering]
     \vfill
     \begin{center}
       {\Large\bfseries\usebeamercolor[fg]{title} Thank You}\\[8pt]
       {\usebeamercolor[fg]{subtitle} Questions?}
     \end{center}
     \vfill
   \end{frame}

   \end{document}
   ```

   Replace `{layout}` with the actual layout filename (e.g., `layout-metropolis`).

7. **Check paper-style sibling.** If a `colors.tex` from paper-style exists in the project
   (search `paper/`, then root), compare `\themename` with `\beamerthemename`.
   - If they differ, warn: "Paper uses {X} theme but slides use {Y}. Match them?"
   - If user agrees, update `\beamerthemename` to match.

8. **Report success.** Print:
   ```
   Beamer Style initialized: {theme} theme + {layout} layout.

   LaTeX: \input{beamer-colors} and \input{layout-{layout}} in your main.tex
   Switch theme:  edit \beamerthemename in beamer-colors.tex
   Switch layout: swap \input{layout-*} line

   Compile: xelatex main.tex
   Guard mode: /beamer-style guard
   ```
