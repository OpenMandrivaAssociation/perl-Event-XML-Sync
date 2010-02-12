%define upstream_name	 Event-XML-Sync
%define upstream_version 1.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 9

Summary:	A Perl module to run synchronized XML stream
License:	GPL
Group:		Development/Perl
Url:		ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/
Source0:	ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
