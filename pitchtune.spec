Summary:	Instrument tuner
Summary(pl):	Stroik do instrumentów
Name:		pitchtune
Version:	0.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Vendor:		Haakon Andre Hjortland <hahjortland@tande.com>
Source0:	http://dl.sourceforge.net/pitchtune/%{name}-%{version}.tar.gz
# Source0-md5:	6373234902851950bd73ea4eac6cc2f4
URL:		http://pitchtune.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pitchtune -- Precise Instrument Tweaking for Crispy Harmony - tuner.
A GPL'ed GTK+ oscilloscope-style musical instrument tuning program.
It can also be used to find the frequency of sounds.

%description -l pl
Pitchtune -- Precise Instrument Tweaking for Crispy Harmony - tuner.
ZGPL-izowany program w stylu oscyloskopu GTK+ do strojenia
instrumentów. Mo¿e byæ równie¿ u¿ywany do znajdowania czêstotliwo¶ci
d¼wiêków.

%prep
%setup  -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.htm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
