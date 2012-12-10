%define name	libgcal
%define version	0.9.6
%define major	0
%define libname %mklibname gcal %{major}
%define develname %mklibname gcal -d


Name:		%name
Version:	%version
Release:	%mkrel 1
Summary:	Implements Google Data Protocol 2.0
License:	BSD
Group:		Communications
URL:		http://code.google.com/p/libgcal/
Source:		http://libgcal.googlecode.com/files/%name-%version.tar.bz2
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	check-devel

%description
Implements Google Data Protocol 2.0. 
It does allow communication with google calendar and contacts, 
implements already:
- authentication
- get all events/contacts
- atom stream parsing
- access to individual events/contacts
- add/delete/edit events/contacts
- query for updated events/contacts
- add/edit/delete contacts with photo
- download your contact's photos
- proxy is supported
- timezones
- use only xml to add/edit/delete entries
- great doxygen documentation 

#-------------------------------------------------------------------

%package -n	%{libname}
Summary:	Library implementing Google Data Protocol Data 2.0
Group:		System/Libraries
Obsoletes:	libgcal <= 0.9.3-1
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This library implements Google Data Protocol 2.0
It does allow communication with google calendar and contacts, 
implements already:
- authentication
- get all events/contacts
- atom stream parsing
- access to individual events/contacts
- add/delete/edit events/contacts
- query for updated events/contacts
- add/edit/delete contacts with photo
- download your contact's photos
- proxy is supported
- timezones
- use only xml to add/edit/delete entries
- great doxygen documentation 

%files -n	%{libname}
%defattr(-,root,root)
%{_libdir}/libgcal.so.%{major}*

#--------------------------------------------------------------------


%package -n	%{develname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	libgcal-devel <= 0.9.3-1
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n	%{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libgcal.so
%{_libdir}/pkgconfig/libgcal.pc
%{_libdir}/LibGCal/cmake/LibGCalConfig.cmake

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%clean
%__rm -rf %buildroot


%changelog
* Wed Sep 08 2010 John Balcaen <mikala@mandriva.org> 0.9.6-1mdv2011.0
+ Revision: 576737
- Update to 0.9.6

* Wed Jul 21 2010 John Balcaen <mikala@mandriva.org> 0.9.5-1mdv2011.0
+ Revision: 556486
- Update to 0.9.5

* Sat Apr 24 2010 John Balcaen <mikala@mandriva.org> 0.9.3-2mdv2010.1
+ Revision: 538458
- Fix Group
- Use of %%mklibname

* Fri Apr 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.9.3-1mdv2010.1
+ Revision: 538300
- update to new version: 0.9.3

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.2-2mdv2010.0
+ Revision: 455886
- rebuild for new curl SSL backend

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.2-1mdv2010.0
+ Revision: 411512
- Update to new version 0.9.2

* Sun May 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.1-0.git090517.2mdv2010.0
+ Revision: 376613
- Fix groups
- Fix groups
  Fix License
- import libgcal


