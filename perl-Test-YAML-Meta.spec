%define upstream_name    Test-YAML-Meta
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.20
Release:	1

Summary:	Validation of the META.yml file in a distribution
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-YAML-Meta-0.20.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::CPAN::Meta::YAML)
BuildRequires:	perl(Test::YAML::Valid)
BuildArch:	noarch

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that slowly
being introduced to module uploads, via the use of ExtUtils::MakeMaker,
Module::Build and Module::Install.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Tue May 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 675485
- new version

* Wed Apr 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 534936
- new version

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 480738
- update to 0.15

* Sun Dec 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 478060
- update to 0.14

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 474755
- update to 0.13

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 405603
- rebuild using %%perl_convert_version

* Mon May 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2010.0
+ Revision: 379578
- update to new version 0.12

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 230282
- update to new version 0.11

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.0
+ Revision: 214529
- update to new version 0.10

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 194862
- update to new version 0.09
- update to new version 0.09

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.06-2mdv2008.1
+ Revision: 109350
- rebuild

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.1
+ Revision: 106560
- update to new version 0.06
- update to new version 0.06

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2008.1
+ Revision: 105898
- update to new version 0.05

* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
+ Revision: 65286
- import perl-Test-YAML-Meta


* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
- first mdv release

