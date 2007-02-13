Summary:	Instrument tuner
Summary(pl.UTF-8):	Stroik do instrumentów
Name:		pitchtune
Version:	0.0.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Vendor:		Haakon Andre Hjortland <hahjortland@tande.com>
Source0:	http://dl.sourceforge.net/pitchtune/%{name}-%{version}.tar.bz2
# Source0-md5:	7b2535c9a70a262838c2d149fbff31e7
URL:		http://pitchtune.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	alsa-lib-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pitchtune -- Precise Instrument Tweaking for Crispy Harmony - tuner.
A GPL'ed GTK+ oscilloscope-style musical instrument tuning program.
It can also be used to find the frequency of sounds.

%description -l pl.UTF-8
Pitchtune -- Precise Instrument Tweaking for Crispy Harmony - tuner.
ZGPL-izowany program w stylu oscyloskopu GTK+ do strojenia
instrumentów. Może być również używany do znajdowania częstotliwości
dźwięków.

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

make install \
	DESTDIR=$RPM_BUILD_ROOT

# will install manually what is useful
rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/*.htm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
