#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Uniqid
Version  : 0.12
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/M/MW/MWX/Data-Uniqid-0.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MW/MWX/Data-Uniqid-0.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-uniqid-perl/libdata-uniqid-perl_0.12-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Data-Uniqid-license = %{version}-%{release}
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

%description dev
dev components for the perl-Data-Uniqid package.


%package license
Summary: license components for the perl-Data-Uniqid package.
Group: Default

%description license
license components for the perl-Data-Uniqid package.


%prep
%setup -q -n Data-Uniqid-0.12
cd ..
%setup -q -T -D -n Data-Uniqid-0.12 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Data-Uniqid-0.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Uniqid
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Uniqid/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/Data/Uniqid.pm
/usr/lib/perl5/vendor_perl/5.28.2/auto/Data/Uniqid/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Uniqid.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Uniqid/deblicense_copyright
