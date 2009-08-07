%define git     %nil
%define major 0

Name:           libgcal
Version:        0.9.2
Release:        %mkrel 1
Summary:        Implements Google Data Protocol 2.0
License:        BSD
Group:          Communications
URL:            http://code.google.com/p/libgcal/
Source:         http://libgcal.googlecode.com/files/%name-%version.tar.gz
BuildRoot:      %_tmppath/%name-%version-%release-root
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  libxml2-devel
BuildRequires:  check-devel

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

%files
%defattr(-,root,root,-)
%{_libdir}/libgcal.so.%{major}*

#--------------------------------------------------------------------

%package   devel
Summary:   Development files for %{name}
Group:     Development/Other 
Requires:  %{name} = %{version}-%{release}

%description devel
Devel files needed to build applications based on %name.

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libgcal.so
%{_libdir}/pkgconfig/libgcal.pc
%{_datadir}/cmake/Modules/FindLibGCal.cmake

#--------------------------------------------------------------------
%prep
%setup -q


%build
%cmake
%make

%install
cd build/
%makeinstall_std
%clean
rm -rf $RPM_BUILD_ROOT
