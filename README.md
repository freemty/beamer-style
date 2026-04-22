# beamer-style

5 low-saturation color themes x 4 layout variants for academic Beamer slides.

A [Claude Code](https://claude.ai/claude-code) skill that gives your presentations a polished, consistent visual identity -- from title slide to final backup.

## Preview

See [`examples/all_previews/`](examples/all_previews/) for all 20 theme-layout combinations (5 themes x 4 layouts).

### Themes

| Theme | Accent | Style |
|-------|--------|-------|
| **Red** (Burgundy) | `#5E3545` | Warm, authoritative |
| **Blue** (Slate) | `#3C4A57` | Cool, academic tone |
| **Gold** (Beige) | `#564D3D` | Warm, understated |
| **Green** (Forest) | `#2A4438` | Deep, natural feel |
| **Purple** (Plum) | `#3E2548` | Rich, distinctive |

### Layouts

| Layout | Best for |
|--------|----------|
| **metropolis** | Conference talks, seminars |
| **minimal** | Dense technical presentations |
| **classic** | Journal clubs, lectures |
| **focus** | Lightning talks, defenses |

## Install

### Via skills.sh (recommended)

```bash
npx skills add freemty/beamer-style -g
```

Works with Claude Code, Cursor, Codex, Windsurf, and [15+ other agents](https://skills.sh).

### Manual

```bash
git clone https://github.com/freemty/beamer-style.git ~/.claude/skills/beamer-style
```

## Usage

```
/beamer-style init --theme blue              # scaffold slides with blue theme + metropolis layout
/beamer-style init --theme red --layout focus # red theme, focus layout
/beamer-style guard                          # detect theme, assist with slides
```

## How It Works

1. **Init** scaffolds a Beamer project with the chosen theme and layout -- drops `beamer-colors.tex` and the layout preamble into your working directory.
2. **Guard mode** detects the active theme from your `.tex` files and provides contextual help: theme switches, color usage, semantic commands (`\pos`, `\con`, `\HL`), and TikZ integration.
3. All 5 themes share the same low-saturation palette designed for projected slides and print.

## What's Included

```
templates/
  beamer-colors.tex       5-theme Beamer color slot mapping
  layout-metropolis.tex   Modern minimal, progress bar
  layout-minimal.tex      Zero decoration, maximum content
  layout-classic.tex      Madrid-inspired, full footline
  layout-focus.tex        High-contrast emphasis layout

examples/
  all_previews/           20 compiled PDFs (5 themes x 4 layouts)
  preview.tex             Source for generating previews
```

## Companion

Pairs with [paper-style](https://github.com/freemty/paper-style) for unified paper + slides visual identity.

## License

MIT
