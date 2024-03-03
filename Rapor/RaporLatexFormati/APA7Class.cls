\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{APA7Class}

% \documentclass[stu,12pt,floatsintext]{apa7}
\LoadClass[stu,12pt,floatsintext]{apa7}

\RequirePackage{lipsum}
\RequirePackage{mathtools}
\RequirePackage{array}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{L}[1]{>{\raggedleft\arraybackslash}p{#1}}
\RequirePackage{colortbl}
\RequirePackage{chemfig}
\RequirePackage{fancyhdr}
\RequirePackage{xpatch}
%\RequirePackage[hidelinks]{hyperref}
\RequirePackage{longtable}
\RequirePackage[utf8]{inputenc}
\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage[thinlines]{easytable}
\RequirePackage{pgfplots}
\RequirePackage{pgfplotstable}
\pgfplotsset{width=13cm,compat=1.9}
\RequirePackage{lscape}
\RequirePackage{multirow}
\RequirePackage{footnote}
\RequirePackage{chngcntr}
\RequirePackage{marvosym}
\RequirePackage{siunitx}
\RequirePackage{xcolor}
\RequirePackage{ragged2e} % Metni sağa sola hizala
\RequirePackage{caption}
\captionsetup[table]{name=Tablo}

%\counterwithin{figure}{section}
%\counterwithin{table}{section}

%\renewcommand{\headrulewidth}{1pt}
%\renewcommand{\footrulewidth}{1pt}

%\setlength{\parskip}{1em}

\urlstyle{same}

\RequirePackage[american]{babel}
\RequirePackage{csquotes} 
\RequirePackage[style=apa,sortcites=true,sorting=nyt,backend=biber]{biblatex} % 1. yol biber
\addbibresource{bibliography.bib} % 1. yol biber

\DeclareLanguageMapping{american}{american-apa} 
\RequirePackage[T1]{fontenc} 
\RequirePackage{mathptmx} 

\RequirePackage{enumitem} %
\newlength\docparskip
\parskip=1pt
\setlength{\docparskip}{\parskip}
\setlist{nosep, itemsep=0pt, parsep=0pt, before={\parskip=0pt}, after=\vspace{-\docparskip}}%