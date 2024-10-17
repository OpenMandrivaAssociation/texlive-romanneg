Name:		texlive-romanneg
Version:	20087
Release:	2
Summary:	Roman page numbers negative
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/romanneg
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanneg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanneg.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
