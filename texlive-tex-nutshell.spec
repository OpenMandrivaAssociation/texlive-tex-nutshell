%global tl_name tex-nutshell
%global tl_revision 70375

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.10
Release:	%{tl_revision}.1
Summary:	A short document about TeX principles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tex-nutshell
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-nutshell.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-nutshell.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This document is meant for users who are looking for information about
the basics of TeX. Its main goal is its brevity. The pure TeX features
are described, no features provided by macro extensions. Only the last
section gives a summary of plain TeX macros.

