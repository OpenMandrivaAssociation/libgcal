%define name	libgcal
%define version	0.9.5
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
