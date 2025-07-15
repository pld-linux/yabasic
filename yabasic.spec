Summary:	Small basic interpreter with printing and graphics
Summary(pl.UTF-8):	Niewielki interpretator basica z obsługą grafiki
Name:		yabasic
Version:	2.751
Release:	3
License:	Public Domain
Group:		Development/Languages
Source0:	http://www.yabasic.de/download/%{name}-%{version}.tar.gz
# Source0-md5:	89b4ae8f01e04ad5417bc5d91601d822
Patch0:		%{name}-make.patch
URL:		http://www.yabasic.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yabasic implements the most common and simple elements of the basic
langugage; It comes with for-loops and goto with while-loops and
procedures. Yabasic does monochrome line grafics, printing comes with
no extra effort. Yabasic runs under Unix and Windows; it is small
(less than 200KB) and free.

%description -l pl.UTF-8
Yabasic implementuje najbardziej popularne i proste elementy języka
basic. Yabasic obsługuje pętle-for, instrukcje goto z pętlami-while
oraz procedurami. Yabasic obsługuje monochromatyczną liniową grafikę
oraz drukowanie.

%prep
%setup  -q
%patch -P0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake} -i
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/pl/man1,%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README *.htm
%attr(755,root,root) %{_bindir}/*
