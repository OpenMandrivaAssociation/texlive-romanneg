# revision 20087
# category Package
# catalog-ctan /macros/latex/contrib/romanneg
# catalog-date 2010-10-13 12:13:38 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-romanneg
Version:	20101013
Release:	2
Summary:	Roman page numbers negative
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/romanneg
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanneg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanneg.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Causes the page numbers in the DVI file (as defined by \count0)
to be negative when roman pagenumbering is in effect.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/romanneg/romanneg.sty
%doc %{_texmfdistdir}/doc/latex/romanneg/romanneg.ltx
%doc %{_texmfdistdir}/doc/latex/romanneg/romanneg.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
