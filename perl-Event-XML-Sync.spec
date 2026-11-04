%define upstream_name	 Event-XML-Sync
Name:		perl-%{upstream_name}
Version:	1.0
Release:	15

Summary:	A Perl module to run synchronized XML stream
License:	GPL
Group:		Development/Perl
Url:		ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/
Source0:	ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/%{upstream_name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Event
%{_mandir}/*/*
