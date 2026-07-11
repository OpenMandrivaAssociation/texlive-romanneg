%global tl_name romanneg
%global tl_revision 20087

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Roman page numbers negative
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/romanneg
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanneg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanneg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Causes the page numbers in the DVI file (as defined by \count0) to be
negative when roman pagenumbering is in effect.

