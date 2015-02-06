%define upstream_name	 Event-XML-Sync
%define upstream_version 1.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	12

Summary:	A Perl module to run synchronized XML stream
License:	GPL
Group:		Development/Perl
Url:		ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/
Source0:	ftp://ftp.inria.fr/INRIA/Atoll/Eric.Clergerie/TAG/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-9mdv2010.1
+ Revision: 504814
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2010.0
+ Revision: 430428
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.0-7mdv2009.0
+ Revision: 256815
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.0-5mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-5mdv2008.0
+ Revision: 86357
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-4mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdk
- spec cleanup
- %%mkrel

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-2mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-1mdk 
- new version
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1-2mdk
- fixed dir ownership (distlint)

* Thu Jan 08 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1-1mdk
- first mdk release

