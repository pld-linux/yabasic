Summary: Small basic interpreter with simple graphics and printing
Name: yabasic
Version: 2.63
Release: 1
Copyright: GPL
Group: Development/Languages
Vendor: Marc-Oliver Ihm
Source: yab.tar.Z
%description
Yabasic implements the most common and simple elements of the basic
langugage; It comes with for-loops and goto with while-loops and procedures. 
Yabasic does monochrome line grafics, printing comes with no extra effort. 
Yabasic runs under Unix and Windows; it is small (less than 200KB) and free. 
Support and the latest version is available at www.yabasic.de
%prep
%setup
%build
./runme
%install
make install
%files
/usr/bin/yabasic
/usr/doc/yabasic/yabasic.htm
