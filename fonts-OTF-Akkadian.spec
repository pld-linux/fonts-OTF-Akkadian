# TODO:
# - pl description
Summary:	Free UCS font for Cuneiform
Summary(pl.UTF-8):	Wolnodostępny font UCS dla pisma klinowego
Name:		fonts-OTF-Akkadian
Version:	2.52
Release:	1
License:	Freeware
Group:		Fonts
Source0:	http://users.teilar.gr/~g1951d/Akkadian.zip
# Source0-md5:	dec2b1988c44b286199b7f7aed0e4119
URL:		http://users.teilar.gr/~g1951d/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		otffontsdir	%{_fontsdir}/OTF

%description
Akkadian font covers the following scripts and symbols supported by
The Unicode Standard 5.2: Basic Latin, Greek and Coptic, some
Punctuation and other Symbols, Cuneiform, Cuneiform Numbers and
Punctuation.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{otffontsdir}

install *.otf $RPM_BUILD_ROOT%{otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%{otffontsdir}/Akkadian.otf
