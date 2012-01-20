Name:		cdw
Version:	0.7.0 
Release:	1
Summary:	Front-end for tools used for burning data CD/DVD

Group:		Archiving/Cd burning
License:	GPLv2+
URL:		http://cdw.sourceforge.net/

Source0:	%{name}/%{name}-%{version}.tar.gz 

BuildRequires:	libcdio-devel, ncurses-devel, %{_lib}burn-devel
Requires:	dvd+rw-tools,wodim,genisoimage,xorriso 


%description
cdw is a ncurses based front-end for some command-line tools used for burning
data CD and DVD discs and for related tasks. The tools are: cdrecord/wodim,
mkisofs/genisoimage, growisofs, dvd+rw-mediainfo, dvd+rw-format, xorriso.
cdw is able to rip tracks from your audio CD to raw audio files.
Limited support for copying content of data CD and DVD discs to image files
is also provided. cdw can verify correctness of writing ISO9660 image to
CD or DVD disc using md5sum or some of  programs that verifies SHA hashes.

%prep
%setup -q


%build
%configure2_5x
%make


%install
%makeinstall_std

%check
make check LIBS="-lm"


%files
%{_bindir}/*
%doc COPYING AUTHORS ChangeLog NEWS README THANKS
%{_mandir}/man1/*
