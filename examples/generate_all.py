#!/usr/bin/env python3
"""Generate all 5 themes × 4 layouts preview PDFs."""

import os
import shutil
import subprocess
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = SCRIPT_DIR.parent / "templates"
OUT_DIR = SCRIPT_DIR / "all_previews"

THEMES = {
    "red": "Warm Burgundy",
    "blue": "Desaturated Slate",
    "gold": "Warm Beige",
    "green": "Deep Forest",
    "purple": "Deep Plum",
}

LAYOUTS = {
    "metropolis": "Modern Minimal",
    "minimal": "Ultra-Clean",
    "classic": "Traditional Academic",
    "focus": "High-Contrast",
}

TEX_TEMPLATE = r"""\documentclass[aspectratio=169,10pt]{beamer}

\usepackage{amsmath,amssymb,booktabs,mathtools}
\usepackage{graphicx,hyperref}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning}

\input{beamer-colors}
\input{LAYOUT_FILE}

\title{THEME_CAP Theme + LAYOUT_CAP Layout}
\subtitle{THEME_LABEL \textperiodcentered{} LAYOUT_LABEL}
\author{Presenter: Demo}
\institute{Shanghai Jiao Tong University}
\date{\today}

\begin{document}

\begin{frame}[plain]
  \titlepage
\end{frame}

\section{Color Palette}

\begin{frame}{Theme Colors}
  \begin{columns}[T]
    \column{0.48\textwidth}
    \begin{block}{Primary Block}
      Structure color follows \texttt{themePrimary}.
      Block body uses \texttt{themeSilver} tint.
    \end{block}

    \begin{alertblock}{Alert Block}
      Alert uses \texttt{themeAlert} --- warm contrast.
    \end{alertblock}

    \column{0.48\textwidth}
    \begin{exampleblock}{Example Block}
      Example uses \texttt{themeExample} --- complementary.
    \end{exampleblock}

    \vskip8pt
    Semantic commands:
    \begin{itemize}
      \item \pos{Positive} (blue)
      \item \con{Negative} (orange)
      \item \HL{Emphasis} (green)
      \item \textcolor{neutral}{Neutral} (gray)
    \end{itemize}
  \end{columns}
\end{frame}

\section{Content}

\begin{frame}{Lists and Mathematics}
  \begin{columns}[T]
    \column{0.48\textwidth}
    \begin{itemize}
      \item First-level with \textbf{bold phrase}
      \begin{itemize}
        \item Second-level detail
        \begin{itemize}
          \item Third-level note
        \end{itemize}
      \end{itemize}
      \item Another point
    \end{itemize}

    \column{0.48\textwidth}
    \begin{theorem}[Sample]
      For all $n \geq 1$:
      \[
        \sum_{k=1}^{n} k = \frac{n(n+1)}{2}
      \]
    \end{theorem}
  \end{columns}
\end{frame}

\section{Diagrams}

\begin{frame}{TikZ with Theme Colors}
  \centering
  \begin{tikzpicture}[
    node distance=2.5cm,
    box/.style={draw=themePrimary,fill=themeLight!30,rounded corners,
                minimum width=2cm,minimum height=0.8cm,font=\small},
    arr/.style={-{Stealth},thick,themePrimary}
  ]
    \node[box] (a) {Input};
    \node[box,right of=a] (b) {Process};
    \node[box,right of=b] (c) {Output};
    \draw[arr] (a) -- (b);
    \draw[arr] (b) -- (c);
  \end{tikzpicture}
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
"""


def build_one(args):
    theme, theme_label, layout, layout_label, colors_src = args
    fname = f"{theme}-{layout}"

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        colors_tex = colors_src.replace(
            r"\providecommand{\beamerthemename}{red}",
            rf"\providecommand{{\beamerthemename}}{{{theme}}}",
        )
        (tmp / "beamer-colors.tex").write_text(colors_tex)

        layout_file = f"layout-{layout}"
        shutil.copy(TEMPLATE_DIR / f"{layout_file}.tex", tmp)

        tex = (
            TEX_TEMPLATE
            .replace("LAYOUT_FILE", layout_file)
            .replace("THEME_CAP", theme.capitalize())
            .replace("LAYOUT_CAP", layout.capitalize())
            .replace("THEME_LABEL", theme_label)
            .replace("LAYOUT_LABEL", layout_label)
        )
        (tmp / f"{fname}.tex").write_text(tex)

        for _ in range(2):
            result = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", f"{fname}.tex"],
                cwd=tmp,
                capture_output=True,
            )

        pdf = tmp / f"{fname}.pdf"
        if pdf.exists():
            shutil.copy(pdf, OUT_DIR / f"{fname}.pdf")
            return fname, True, result.returncode
        return fname, False, result.returncode


def main():
    OUT_DIR.mkdir(exist_ok=True)
    colors_src = (TEMPLATE_DIR / "beamer-colors.tex").read_text()

    jobs = [
        (theme, theme_label, layout, layout_label, colors_src)
        for theme, theme_label in THEMES.items()
        for layout, layout_label in LAYOUTS.items()
    ]

    workers = min(os.cpu_count() or 4, len(jobs))
    print(f"Building {len(jobs)} PDFs with {workers} workers...", flush=True)

    with ProcessPoolExecutor(max_workers=workers) as pool:
        for fname, ok, rc in pool.map(build_one, jobs):
            status = "OK" if ok else f"FAILED (exit {rc})"
            print(f"  {fname}.pdf {status}")

    pdfs = sorted(OUT_DIR.glob("*.pdf"))
    print(f"\n=== Done: {len(pdfs)} PDFs ===")
    for p in pdfs:
        print(f"  {p.name}  ({p.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    main()
