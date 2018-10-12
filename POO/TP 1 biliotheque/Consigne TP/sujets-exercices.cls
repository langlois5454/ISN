\ProvidesClass{sujets-exercices} %inspired by iut45-exercices.cls
\newif\if@votre@nom \@votre@nomfalse
\DeclareOption{nom}{\@votre@nomtrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[a4paper,12pt]{article}
\RequirePackage{a4wide}
\RequirePackage{pgfkeys}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{paralist}
\RequirePackage[english,french]{babel}
%\StandardLayout
\RequirePackage{amstext,amsmath,amssymb}
\RequirePackage{paralist}
\RequirePackage{oldstyle}
%\RequirePackage{charter}
\RequirePackage{txfonts}
\RequirePackage{listings}
\RequirePackage{color}

\RequirePackage{tikz}
\newcommand{\banner}[1]{%
  \par\noindent\begin{tikzpicture}%
  \node[fill=lightgray,rounded corners=5pt,text width=\linewidth-8pt,align=center]{%
    \footnotesize\sf#1};\end{tikzpicture}\nopagebreak\ignorespaces}

\inputencoding{utf8}

\pgfkeys{/iut45/.is family}
\newcommand{\iutset}{\pgfqkeys{/iut45}}
\newcommand{\iutval}[1]{\pgfkeysvalueof{/iut45/#1}}

\pgfkeyssetvalue{/iut45/cours}{*COURS*}
\pgfkeyssetvalue{/iut45/annee}{*ANNEE*}
\pgfkeyssetvalue{/iut45/type}{*TYPE*}
\pgfkeyssetvalue{/iut45/numero}{*NUMERO*}
\pgfkeyssetvalue{/iut45/titre}{*TITRE*}
\pgfkeyssetvalue{/iut45/lieu}{*LIEU*}

\pgfkeyssetvalue{/iut45/cours style}{\bf}
\pgfkeyssetvalue{/iut45/annee style}{\bf}
\pgfkeyssetvalue{/iut45/typenum style}{\large}
\pgfkeyssetvalue{/iut45/type style}{\sc\Large}
\pgfkeyssetvalue{/iut45/numero style}{\oldstyle}
\pgfkeyssetvalue{/iut45/titre style}{\sl\large}
\pgfkeyssetvalue{/iut45/lieu style}{\small}
\pgfkeyssetvalue{/iut45/nom style}{\bf}

\newcommand{\iut@votre@nom}{\if@votre@nom{\iutval{nom style}Votre nom:\ \vrule height 0.05pt depth 0pt width 5cm\relax}\fi}

\newcommand{\ps@iutfirst}{%
  \let\@mkboth\@gobbletwo
  \def\@oddhead{\reset@font
    {{\iutval{cours style}\iutval{cours}}}\hfill\iut@votre@nom\hfill{\iutval{annee style}\iutval{annee}}}%
  \let\@evenhead\@oddhead
  \def\@oddfoot{\reset@font
    {\iutval{lieu style}\iutval{lieu}}\hfill{\thepage}}%
  \let\@evenfoot\@oddfoot
}

\newcommand{\iut@typenum}{\iutval{typenum style}{\iutval{type style}\iutval{type}} n$^\circ${\iutval{numero style}\iutval{numero}}}

\newcommand{\ps@iutother}{%
  \let\@mkboth\@gobbletwo
  \def\@oddhead{\reset@font
    {{\iutval{cours style}\iutval{cours}} (\iut@typenum)}\hfill{\iutval{annee style}\iutval{annee}}}%
  \let\@evenhead\@oddhead
  \def\@oddfoot{\reset@font
    {\iutval{lieu style}\iutval{lieu}}\hfill{\thepage}}%
  \let\@evenfoot\@oddfoot
}

\AtBeginDocument{\pagestyle{iutother}\thispagestyle{iutfirst}}

\newlength{\iut@lena}
\newdimen\iut@dima

\newcommand{\iut@banniere}{%
  \settowidth{\iut@lena}{\iut@typenum}%
  \iut@dima\linewidth
  \advance\iut@dima -2\iut@lena
  \advance\iut@dima -4pt\relax% remove a bit more
  \noindent
  \begin{tabular*}{\linewidth}{@{}l@{\extracolsep{\fill}}p{\iut@dima}@{\extracolsep{0pt}}l@{}}\hline
    \iut@typenum&\centering\iutval{titre style}\strut\iutval{titre}&\hspace*{\iut@lena}\\\hline\end{tabular*}\par\vspace{1cm}}

\AtBeginDocument{\iut@banniere}

\setlength{\parindent}{0pt}
\setlength{\parskip}{\bigskipamount}

\newcommand{\iut@exercice@label}{%
  \iflanguage{english}{Exercise}{Exercice}}

\newcounter{iut@exercice}

% \exercice
% \exercice{TITLE}
% \exercice[note={...}]
% \exercice[note={...}]{TITLE}
\newcommand{\exercice}[1][]{%
  \@ifnextchar\bgroup{\@exercice{#1}}{\@exercice{#1}{}}}

\pgfkeyssetvalue{/iut45/note}{}
\pgfkeyssetvalue{/iut45/note style}{\small\sf}

\newcommand{\@exercice}[2]{%
  \ifvmode\else\par\fi
  \iutset{note={}}%
  \iutset{#1}%
  \edef\@tempe{\iutval{note}}%
  \ifx\@tempe\@empty\else\def\@tempe{\llap{\reset@font\iutval{note style}\iutval{note}\quad}}\fi
  \refstepcounter{iut@exercice}%
  \def\@tempd{#2}%
  \ifx\@tempd\@empty\else\def\@tempd{\quad #2}\fi
  \paragraph{\@tempe\iut@exercice@label\ \arabic{iut@exercice}.\@tempd}%
  \leavevmode\ignorespaces
}

\newcounter{iut@question}[iut@exercice]

% \question
% \question{TITLE}
% \question[note={...}]
% \question[note={...}]{TITLE}
\newcommand{\question}[1][]{%
  \@ifnextchar\bgroup{\@question{#1}}{\@question{#1}{}}}

\pgfkeyssetvalue{/iut45/question skip}{0mm}
\pgfkeyssetvalue{/iut45/note substyle}{\footnotesize\sf}

\newcommand{\@question}[2]{%
  \ifvmode\else\par\fi
  \iutset{note={}}%
  \iutset{#1}%
  \edef\@tempe{\iutval{note}}%
  \ifx\@tempe\@empty\else\def\@tempe{\llap{\reset@font\iutval{note substyle}\iutval{note}\quad}}\fi
  \refstepcounter{iut@question}%
  \def\@tempd{#2}%
  \ifx\@tempd\@empty\else\def\@tempd{\quad #2}\fi
  \vspace{\iutval{question skip}}%
  \noindent\textbf{\@tempe\arabic{iut@exercice}.\arabic{iut@question}\quad}%
  \ignorespaces
}

\newcommand{\iut@reponse@label}{%
  \iflanguage{english}{Answer}{Réponse}}

\newcommand{\reponse}[2][\iut@reponse@label:]{%
  \par\noindent
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}\relax}|ll|}\hline
    \textbf{#1}&\\
    \vrule width 0pt height #2 depth 0pt&\\\hline
  \end{tabular*}}

%==============================================================================
% support for programming languages
%==============================================================================
\definecolor{lightgray}{gray}{0.7}

\lstset{basicstyle=\ttfamily,language=C}%,inputencoding=utf8,extendedchars=true}

\lstnewenvironment{C}{%
  \lstset{language=C,%
    frame=l,%
    xleftmargin=1cm,%
    framexleftmargin=0.5cm,%
    framerule=0.5mm,%
    rulecolor=\color{lightgray}}}{}
\newcommand{\icc}{\lstinline[language=C]}

\lstnewenvironment{CXX}{%
  \lstset{language=C++,
    frame=l,xleftmargin=1cm,%
    framexleftmargin=0.5cm,%
    framerule=0.5mm,%
    rulecolor=\color{lightgray}}}{}

\newcommand{\icxx}{\lstinline[language=C++]}

\lstnewenvironment{bash}{%
  \lstset{language=bash,%
    frame=l,xleftmargin=1cm,%
    framexleftmargin=0.5cm,%
    framerule=0.5mm,%
    rulecolor=\color{lightgray}}}{}

\lstnewenvironment{sbash}{%
  \lstset{language=bash,%
    basicstyle={\ttfamily\fontsize{9pt}{9pt}\selectfont},%
    frame=l,xleftmargin=1cm,framexleftmargin=0.5cm,%
    framerule=0.5mm,rulecolor=\color{lightgray}}}{}

\newcommand{\ibash}{\lstinline[language=bash]}

\lstnewenvironment{sql}{%
  \lstset{language=SQL,frame=l,%
    xleftmargin=1cm,framexleftmargin=0.5cm,%
    framerule=0.5mm,rulecolor=\color{lightgray}}}{}

\lstnewenvironment{SQL}{%
  \lstset{language=SQL,frame=l,%
    xleftmargin=1cm,framexleftmargin=0.5cm,%
    framerule=0.5mm,rulecolor=\color{lightgray}}}{}

\newcommand{\isql}{\lstinline[language=SQL]}

\lstnewenvironment{python}{%
  \lstset{language=python,frame=l,%
    xleftmargin=1cm,framexleftmargin=0.5cm,%
    framerule=0.5mm,rulecolor=\color{lightgray},%
    morekeywords={with}}}{}

\newcommand{\ipython}{\lstinline[language=python,morekeywords={with}]}

\lstnewenvironment{cmake}{%
  \lstset{language=,frame=l,xleftmargin=1cm,%
    framexleftmargin=0.5cm,framerule=0.5mm,%
    rulecolor=\color{lightgray}}}{}

\newcommand{\icmake}{\lstinline[language=cmake]}

\lstnewenvironment{NONE}{%
  \lstset{language=,frame=l,xleftmargin=1cm,%
    framexleftmargin=0.5cm,framerule=0.5mm,%
    rulecolor=\color{lightgray}}}{}

\lstnewenvironment{make}{%
  \lstset{language=make,frame=l,xleftmargin=1cm,%
    framexleftmargin=0.5cm,framerule=0.5mm,%
    rulecolor=\color{lightgray}}}{}

\newcommand{\imake}{\lstinline[language=make]}
