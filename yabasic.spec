Summary:	Small basic interpreter with printing and graphics
Summary(pl):	Niewielki interpretator basica z obs³ug± grafiki
Name:		yabasic
Version:	2.671
Release:	16
License:	Public Domain
Group:		Development/Languages
Source0:	http://www.yabasic.de/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.yabasic.de/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yabasic implements the most common and simple elements of the basic
langugage; It comes with for-loops and goto with while-loops and
procedures. Yabasic does monochrome line grafics, printing comes with
no extra effort. Yabasic runs under Unix and Windows; it is small
(less than 200KB) and free.

%description -l pl
Yabasic implementuje najbardziej popularne i proste elementy jêzyka
basic. Yabasic obs³uguje pêtle-for, instrukcje goto z pêtlami-while
oraz procedurami. Yabasic obs³uguje monochromatyczn± liniow± grafikê
oraz drukowanie.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoheader
%{__autoconf}
automake -a -c -i
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/pl/man1,%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.htm
%attr(755,root,root) %{_bindir}/*
