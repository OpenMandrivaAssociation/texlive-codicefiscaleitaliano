# revision 26234
# category Package
# catalog-ctan /macros/latex/contrib/codicefiscaleitaliano
# catalog-date 2012-05-05 09:37:49 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-codicefiscaleitaliano
Version:	1.1
Release:	3
Summary:	Test the consistency of the Italian personal Fiscal Code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/codicefiscaleitaliano
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codicefiscaleitaliano.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codicefiscaleitaliano.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codicefiscaleitaliano.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 813456
- Update to latest release.
- Import texlive-codicefiscaleitaliano
- Import texlive-codicefiscaleitaliano

