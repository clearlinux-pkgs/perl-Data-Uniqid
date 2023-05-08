#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Uniqid
Version  : 0.12
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/M/MW/MWX/Data-Uniqid-0.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MW/MWX/Data-Uniqid-0.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-uniqid-perl/libdata-uniqid-perl_0.12-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Data-Uniqid-license = %{version}-%{release}
Requires: perl-Data-Uniqid-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Data/Uniqid Readme
Data::Uniqid provides three simple routines for generating unique ids.
These ids are coded with a Base62 systen to make them short and handy
(e.g. to use it as part of a URL).

%package dev
Summary: dev components for the perl-Data-Uniqid package.
Group: Development
Provides: perl-Data-Uniqid-devel = %{version}-%{release}
Requires: perl-Data-Uniqid = %{version}-%{release}

%description dev
dev components for the perl-Data-Uniqid package.


%package license
Summary: license components for the perl-Data-Uniqid package.
Group: Default

%description license
license components for the perl-Data-Uniqid package.


%package perl
Summary: perl components for the perl-Data-Uniqid package.
Group: Default
Requires: perl-Data-Uniqid = %{version}-%{release}

%description perl
perl components for the perl-Data-Uniqid package.


%prep
%setup -q -n Data-Uniqid-0.12
cd %{_builddir}
tar xf %{_sourcedir}/libdata-uniqid-perl_0.12-1.debian.tar.xz
cd %{_builddir}/Data-Uniqid-0.12
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Uniqid-0.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Uniqid
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Uniqid/4bd9ea40fd8cfbb3b81112e5e86007d83ceb1b00
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Uniqid.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Uniqid/4bd9ea40fd8cfbb3b81112e5e86007d83ceb1b00

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
