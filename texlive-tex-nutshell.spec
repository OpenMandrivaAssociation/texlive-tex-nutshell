Name:		texlive-tex-nutshell
Version:	70375
Release:	1
Summary:	A short document about TeX principles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tex-nutshell
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-nutshell.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-nutshell.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This document is meant for users who are looking for
information about the basics of TeX. Its main goal is its
brevity. The pure TeX features are described, no features
provided by macro extensions. Only the last section gives a
summary of plain TeX macros.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/plain/tex-nutshell

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
