#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pbr
Version  : 3.1.1
Release  : 45
URL      : https://pypi.debian.net/pbr/pbr-3.1.1.tar.gz
Source0  : https://pypi.debian.net/pbr/pbr-3.1.1.tar.gz
Summary  : Python Build Reasonableness
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pbr-bin
Requires: pbr-legacypython
Requires: pbr-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
============

%package bin
Summary: bin components for the pbr package.
Group: Binaries

%description bin
bin components for the pbr package.


%package legacypython
Summary: legacypython components for the pbr package.
Group: Default

%description legacypython
legacypython components for the pbr package.


%package python
Summary: python components for the pbr package.
Group: Default
Requires: pbr-legacypython

%description python
python components for the pbr package.


%prep
%setup -q -n pbr-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505055312
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
export SOURCE_DATE_EPOCH=1505055312
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pbr

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
