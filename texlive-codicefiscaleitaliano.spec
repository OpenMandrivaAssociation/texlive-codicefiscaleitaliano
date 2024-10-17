Name:		texlive-codicefiscaleitaliano
Version:	29803
Release:	2
Summary:	Test the consistency of the Italian personal Fiscal Code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/codicefiscaleitaliano
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codicefiscaleitaliano.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codicefiscaleitaliano.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codicefiscaleitaliano.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The alphanumeric string that forms the Italian personal Fiscal
Code is prone to be misspelled thus rendering a legal document
invalid. The package quickly verifies the consistency of the
fiscal code string, and can therefore be useful for lawyers and
accountants that use fiscal codes very frequently.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/codicefiscaleitaliano/codicefiscaleitaliano.sty
%doc %{_texmfdistdir}/doc/latex/codicefiscaleitaliano/README
%doc %{_texmfdistdir}/doc/latex/codicefiscaleitaliano/codicefiscaleitaliano.pdf
#- source
%doc %{_texmfdistdir}/source/latex/codicefiscaleitaliano/codicefiscaleitaliano.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
