# Guard Guide — Beamer Style Guardian Mode

## Instructions for Claude

You are acting as a style guardian for an existing Beamer slides project.

### On Entry

1. **Find project theme.** Read `beamer-colors.tex` (search slides/, then root). Extract
   the `\beamerthemename` value. If not found, suggest running `/beamer-style init` first.

2. **Find layout.** Grep for `\input{layout-` in the main `.tex` file to identify
   which layout is active. Report it.

3. **Check paper-style sibling.** If `colors.tex` (paper-style) exists in the project,
   compare themes. Warn on mismatch.

4. **Confirm.** Print: "Active: {theme} theme + {layout} layout. Ready to assist."

### Theme Switch

When user says "switch to {name}" or "change theme to {name}":
1. Update `\beamerthemename` in `beamer-colors.tex`
2. If paper-style `colors.tex` exists, ask: "Also update paper theme to match?"
3. Report: "Switched to {name} theme."

### Layout Switch

When user says "switch layout to {name}" or "change to {layout}":
1. Copy the new `layout-{name}.tex` from skill templates if not already present
2. Update the `\input{layout-*}` line in the main `.tex` file
3. Compile and verify
4. Report: "Switched to {name} layout."

### Ongoing Assistance

When the user asks for help with slides:

- **Colors:** Always use the semantic commands from `beamer-colors.tex`:
  - `\pos{}` for positive/correct (blue)
  - `\con{}` for negative/limitation (orange)
  - `\HL{}` for emphasis/key finding (green)
  - `\textcolor{neutral}{}` for de-emphasized
  - `themePrimary`, `themeSecondary`, `themeLight`, `themeSilver` for theme-consistent accents

- **Blocks:** Use beamer's `block`, `alertblock`, `exampleblock` — colors auto-follow theme.

- **TikZ:** Use `themePrimary`, `themeSecondary`, `themeLight` in diagrams for consistency.

- **Compile:** Always use XeLaTeX: `xelatex -interaction=nonstopmode FILE.tex`

### Color Quick Reference

Do not hardcode colors — always reference theme colors via the named commands.
The beamer-colors.tex provides:
- `themePrimary` — main accent (titles, structure)
- `themeSecondary` — secondary accent (subtitles, links)
- `themeTertiary` — dark variant (deep contrast)
- `themeLight` — light tint (highlights)
- `themeSilver` — very light (backgrounds)
- `themeBg` — page background tint
- `themeBorder` — borders, rules
- `themeAlert` — warnings, alerts (warm tone)
- `themeExample` — examples (contrasting hue)
