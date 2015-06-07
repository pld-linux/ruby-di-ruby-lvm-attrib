%define	pkgname	di-ruby-lvm-attrib
Summary:	A list of attributes for LVM objects
Name:		ruby-%{pkgname}
Version:	0.0.19
Release:	2
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	5723064c4edcbf4c9819dcb607bc3580
Patch0:		https://github.com/gregsymons/di-ruby-lvm-attrib/pull/26.patch
# Patch0-md5:	162fa09f563143f5bc8c97804c5fef0f
URL:		https://github.com/gregsymons/di-ruby-lvm-attrib
BuildRequires:	device-mapper-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
# requires specific lvm2 version, because attributes need to be generated for each version
# https://github.com/gregsymons/di-ruby-lvm-attrib#adding-attributes
%requires_eq_to lvm2 device-mapper-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A list of attributes for LVM objects

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

# as we have strict dep on lvm2 package, we do not need other versions
install -d extra-attributes
mv lib/lvm/attributes/* extra-attributes
ver=$(rpm -q --qf '%{V}' device-mapper-devel)
mv extra-attributes/$ver* lib/lvm/attributes

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{ruby_vendorlibdir}/lvm
%{ruby_vendorlibdir}/lvm/attributes.rb
%{ruby_vendorlibdir}/lvm/attributes
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
