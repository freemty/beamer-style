---
name: beamer-style
description: >
  Use when setting up Beamer slide themes, switching slide color themes,
  or ensuring visual consistency between papers and presentations.
  Triggers: /beamer-style, slide theme, 幻灯片配色, beamer配色, 演示风格.
  If paper-style is installed, shares the same 5-theme color system for unified paper + slides identity.
---

# Beamer Style — Academic Slide Theme System

5 low-saturation themes (red/blue/gold/green/purple) × 4 layouts for unified Beamer visual identity.
Pairs well with `paper-style` for a consistent visual identity across papers and slides.

## Subcommands

| Command | Guide | What it does |
|---------|-------|-------------|
| `/beamer-style init [--theme NAME] [--layout NAME]` | `guides/init.md` | Scaffold slides project with theme + layout |
| `/beamer-style` or `/beamer-style guard` | `guides/guard.md` | Detect theme, assist with slides |

**Arguments for init:**
- `--theme NAME`: red, blue (default), gold, green, purple
- `--layout NAME`: metropolis (default), minimal, classic, focus

**Read and execute the corresponding guide file.**

## Themes (shared with paper-style)

| Name | Primary | Style |
|------|---------|-------|
| `red` | `#5E3545` | Warm burgundy |
| `blue` | `#3C4A57` | Desaturated slate |
| `gold` | `#564D3D` | Warm beige |
| `green` | `#2A4438` | Deep forest |
| `purple` | `#3E2548` | Deep plum |

## Layouts

| Name | Style | Best for |
|------|-------|----------|
| `metropolis` | Modern minimal, progress bar, left-aligned | Conference talks, seminars |
| `minimal` | Zero decoration, maximum content | Dense technical presentations |
| `classic` | Madrid-inspired, full footline, nav dots | Journal clubs, lectures |
| `focus` | Large titles, thick rules, focus frames | Lightning talks, defenses |

## Templates

| File | Purpose |
|------|---------|
| `templates/beamer-colors.tex` | 5-theme Beamer color slot mapping |
| `templates/layout-metropolis.tex` | Metropolis-style layout preamble |
| `templates/layout-minimal.tex` | Ultra-clean zero-decoration layout |
| `templates/layout-classic.tex` | Traditional academic layout |
| `templates/layout-focus.tex` | High-contrast emphasis layout |

## Quick Reference — Guard Mode

**Theme colors in LaTeX:**
```latex
\usebeamercolor[fg]{structure}      % themePrimary
{\color{themePrimary} text}         % direct color access
{\color{themeLight} highlight}      % light variant
```

**Semantic commands (colorblind-safe):**
```latex
\pos{correct}     % blue — positive
\con{limitation}   % orange — negative
\HL{key finding}   % green — emphasis
```

**Blocks auto-follow theme:**
```latex
\begin{block}{Title}         % themePrimary header
\begin{alertblock}{Warning}  % themeAlert header
\begin{exampleblock}{Demo}   % themeExample header
```

**TikZ with theme colors:**
```latex
\draw[themePrimary,thick] (0,0) -- (1,1);
\fill[themeLight] (0,0) circle (0.5);
```

**Theme switch** (guard mode): update `\beamerthemename` in `beamer-colors.tex`.
**Layout switch** (guard mode): swap `\input{layout-*}` line in main `.tex`.
