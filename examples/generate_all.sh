#!/bin/bash
# Generate all 5 themes × 4 layouts preview PDFs
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE_DIR="$SCRIPT_DIR/../templates"
OUT_DIR="$SCRIPT_DIR/all_previews"
mkdir -p "$OUT_DIR"

THEMES=(red blue gold green purple)
LAYOUTS=(metropolis minimal classic focus)

THEME_LABELS=("Warm Burgundy" "Desaturated Slate" "Warm Beige" "Deep Forest" "Deep Plum")
LAYOUT_LABELS=("Modern Minimal" "Ultra-Clean" "Traditional Academic" "High-Contrast")

for ti in "${!THEMES[@]}"; do
  theme="${THEMES[$ti]}"
  theme_label="${THEME_LABELS[$ti]}"
  for li in "${!LAYOUTS[@]}"; do
    layout="${LAYOUTS[$li]}"
    layout_label="${LAYOUT_LABELS[$li]}"
    fname="${theme}-${layout}"
    echo "=== Generating $fname ==="

    # Create temp .tex with correct theme + layout
    WORK="$OUT_DIR/$fname"
    mkdir -p "$WORK"

    # Copy templates with theme override
    sed "s/\\\\providecommand{\\\\beamerthemename}{red}/\\\\providecommand{\\\\beamerthemename}{${theme}}/" \
      "$TEMPLATE_DIR/beamer-colors.tex" > "$WORK/beamer-colors.tex"
    cp "$TEMPLATE_DIR/layout-${layout}.tex" "$WORK/"

    cat > "$WORK/${fname}.tex" << 'TEXEOF'
\documentclass[aspectratio=169,10pt]{beamer}

\usepackage{amsmath,amssymb,booktabs,mathtools}
\usepackage{graphicx,hyperref}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning}

\input{beamer-colors}
TEXEOF

    echo "\\input{layout-${layout}}" >> "$WORK/${fname}.tex"

    cat >> "$WORK/${fname}.tex" << TEXEOF2

\\title{${theme^} Theme + ${layout^} Layout}
\\subtitle{${theme_label} · ${layout_label}}
\\author{Presenter: Demo}
\\institute{Shanghai Jiao Tong University}
\\date{\\today}

\\begin{document}

\\begin{frame}[plain]
  \\titlepage
\\end{frame}

\\section{Color Palette}

\\begin{frame}{Theme Colors}
  \\begin{columns}[T]
    \\column{0.48\\textwidth}
    \\begin{block}{Primary Block}
      Structure color follows \\texttt{themePrimary}.
      Block body uses \\texttt{themeSilver} tint.
    \\end{block}

    \\begin{alertblock}{Alert Block}
      Alert uses \\texttt{themeAlert} --- warm contrast.
    \\end{alertblock}

    \\column{0.48\\textwidth}
    \\begin{exampleblock}{Example Block}
      Example uses \\texttt{themeExample} --- complementary.
    \\end{exampleblock}

    \\vskip8pt
    Semantic commands:
    \\begin{itemize}
      \\item \\pos{Positive} (blue)
      \\item \\con{Negative} (orange)
      \\item \\HL{Emphasis} (green)
      \\item \\textcolor{neutral}{Neutral} (gray)
    \\end{itemize}
  \\end{columns}
\\end{frame}

\\section{Content}

\\begin{frame}{Lists and Mathematics}
  \\begin{columns}[T]
    \\column{0.48\\textwidth}
    \\begin{itemize}
      \\item First-level with \\textbf{bold phrase}
      \\begin{itemize}
        \\item Second-level detail
        \\begin{itemize}
          \\item Third-level note
        \\end{itemize}
      \\end{itemize}
      \\item Another point
    \\end{itemize}

    \\column{0.48\\textwidth}
    \\begin{theorem}[Sample]
      For all \\\$n \\geq 1\\\$:
      \\[
        \\sum_{k=1}^{n} k = \\frac{n(n+1)}{2}
      \\]
    \\end{theorem}
  \\end{columns}
\\end{frame}

\\section{Diagrams}

\\begin{frame}{TikZ with Theme Colors}
  \\centering
  \\begin{tikzpicture}[
    node distance=2.5cm,
    box/.style={draw=themePrimary,fill=themeLight!30,rounded corners,
                minimum width=2cm,minimum height=0.8cm,font=\\small},
    arr/.style={-{Stealth},thick,themePrimary}
  ]
    \\node[box] (a) {Input};
    \\node[box,right of=a] (b) {Process};
    \\node[box,right of=b] (c) {Output};
    \\draw[arr] (a) -- (b);
    \\draw[arr] (b) -- (c);
  \\end{tikzpicture}
\\end{frame}

\\begin{frame}[plain,noframenumbering]
  \\vfill
  \\begin{center}
    {\\Large\\bfseries\\usebeamercolor[fg]{title} Thank You}\\\\[8pt]
    {\\usebeamercolor[fg]{subtitle} Questions?}
  \\end{center}
  \\vfill
\\end{frame}

\\end{document}
TEXEOF2

    # Compile twice for page numbers
    cd "$WORK"
    xelatex -interaction=nonstopmode "${fname}.tex" > /dev/null 2>&1
    xelatex -interaction=nonstopmode "${fname}.tex" > /dev/null 2>&1

    # Move PDF out, clean up
    mv "${fname}.pdf" "$OUT_DIR/"
    cd "$OUT_DIR"
    rm -rf "$WORK"

    echo "  -> $fname.pdf done"
  done
done

echo ""
echo "=== All done! ==="
ls -la "$OUT_DIR"/*.pdf
