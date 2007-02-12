Summary:	Mastering sed scripts
Summary(pl.UTF-8):   Opanowywanie skryptów sed
Name:		sedsed
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://sedsed.sourceforge.net/%{name}-%{version}
# Source0-md5:	14ef0cc49d0ca8b2e1a88bc0aa83ce2d
URL:		http://sedsed.sourceforge.net/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sedsed is a Python script that masters sed scripts. It generates sed
debug files in sed, which lets you debug scripts with your own version
of sed (Linux, DOS, etc.). It's also a script beautifier, doing
indentation and spaces/comments formatting. It can also convert sed
scripts to colorful HTML files.

%description -l pl.UTF-8
sedsed to skrypt w Pythonie panujący nad skryptami seda. Generuje
pliki diagnostyczne seda w sedzie, pozwalające odpluskwiać skrypty
przy użyciu własnej wersji seda (linuksowej, dosowej itp.). Jest także
upiększaczem skryptów, dodającym wcięcia i formatowanie odstępów i
komentarzy. Może także konwertować skrypty seda do kolorowych plików
HTML.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -i -e 's,/usr/bin/env ,,g' $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sedsed
