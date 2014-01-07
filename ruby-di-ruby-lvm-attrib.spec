%define	pkgname	di-ruby-lvm-attrib
Summary:	A list of attributes for LVM objects
Name:		ruby-%{pkgname}
Version:	0.0.12
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	6f9a5ef1ed9c9006898ce12f6132913f
URL:		https://github.com/DrillingInfo/di-ruby-lvm-attrib
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A list of attributes for LVM objects

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/generate_field_data
%dir %{ruby_vendorlibdir}/lvm
%{ruby_vendorlibdir}/lvm/attributes.rb
%{ruby_vendorlibdir}/lvm/attributes
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
