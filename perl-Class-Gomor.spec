#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Class
%define	pnam	Gomor
Summary:	Class::Gomor - another class and object builder
Summary(pl.UTF-8):	Class:Gomor - kolejny builder klas i obiektów
Name:		perl-Class-Gomor
Version:	1.03
Release:	1
License:	artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	701c0d407574cd5bb1c52537a63ac276
URL:		http://search.cpan.org/dist/Class-Gomor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is yet another class builder. This one adds parameter
checking in new constructor, that is to check for attributes
existence, and definedness.

%description -l pl.UTF-8
Ten moduł jest jeszcze kolejnym builderem klas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/*.pm
%{perl_vendorlib}/Class/Gomor
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
