#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pbr
Version  : 5.2.0
Release  : 80
URL      : https://files.pythonhosted.org/packages/11/3d/3b5bbf398535d78a8cd7cf01441a745dedda5ca69f82658f2c7672bcdcce/pbr-5.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/3d/3b5bbf398535d78a8cd7cf01441a745dedda5ca69f82658f2c7672bcdcce/pbr-5.2.0.tar.gz
Summary  : Python Build Reasonableness
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pbr-bin = %{version}-%{release}
Requires: pbr-license = %{version}-%{release}
Requires: pbr-python = %{version}-%{release}
Requires: pbr-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Introduction
============
.. image:: https://img.shields.io/pypi/v/pbr.svg
:target: https://pypi.python.org/pypi/pbr/
:alt: Latest Version

%package bin
Summary: bin components for the pbr package.
Group: Binaries
Requires: pbr-license = %{version}-%{release}

%description bin
bin components for the pbr package.


%package license
Summary: license components for the pbr package.
Group: Default

%description license
license components for the pbr package.


%package python
Summary: python components for the pbr package.
Group: Default
Requires: pbr-python3 = %{version}-%{release}

%description python
python components for the pbr package.


%package python3
Summary: python3 components for the pbr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pbr package.


%prep
%setup -q -n pbr-5.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556300615
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pbr
cp LICENSE %{buildroot}/usr/share/package-licenses/pbr/LICENSE
cp pbr/tests/testpackage/LICENSE.txt %{buildroot}/usr/share/package-licenses/pbr/pbr_tests_testpackage_LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pbr

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pbr/LICENSE
/usr/share/package-licenses/pbr/pbr_tests_testpackage_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
