Name:		cdw
Version:	0.8.1
Release:	2
Summary:	Front-end for tools used for burning data CD/DVD
Group:		Archiving/Cd burning
License:	GPLv2+
URL:		https://cdw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/cdw/cdw/cdw%200.8.1/%{name}-%{version}.tar.gz
BuildSystem:	autotools
BuildRequires:	pkgconfig(libcdio), pkgconfig(ncurses), pkgconfig(libburn-1)
Requires:	dvd+rw-tools genisoimage xorriso 

%patchlist
cdw-0.8.1-formatstrings.patch

%description
cdw is a ncurses based front-end for some command-line tools used for burning
data CD and DVD discs and for related tasks. The tools are: cdrecord/wodim,
mkisofs/genisoimage, growisofs, dvd+rw-mediainfo, dvd+rw-format, xorriso.
cdw is able to rip tracks from your audio CD to raw audio files.
Limited support for copying content of data CD and DVD discs to image files
is also provided. cdw can verify correctness of writing ISO9660 image to
CD or DVD disc using md5sum or some of  programs that verifies SHA hashes.

%files
%{_bindir}/*
%doc COPYING AUTHORS ChangeLog NEWS README THANKS
%{_mandir}/man1/*
