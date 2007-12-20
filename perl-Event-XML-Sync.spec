%define module	Event-XML-Sync
%define name	perl-%{module}
%define version 1.0
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Perl module to run synchronized XML stream
License:	GPL
Group:		Development/Perl
Source:		ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/%{module}-%{version}.tar.bz2
Url:		ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module may be used to developp application wrappers to be
installed in XML pipelines.

The wrapper expects some XML input. It sends some bits of
information to the wrapped application and information the
returned information (when arriving) in the input XML stream
(by adding, modifying or deleting XML elements). Output XML is
produced for the next wrapper in the pipeline.

The key point is that wrappers are non-blocking, i.e. a
wrapper do not stop waiting for information to be returned by
the wrapped application. To achieve that, the wrapper needs
some kind of synchronization to correlate the returned
information with the input XML stream.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Event
%{_mandir}/*/*

