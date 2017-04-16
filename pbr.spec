#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pbr
Version  : 2.1.0
Release  : 36
URL      : https://pypi.debian.net/pbr/pbr-2.1.0.tar.gz
Source0  : https://pypi.debian.net/pbr/pbr-2.1.0.tar.gz
Summary  : Python Build Reasonableness
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pbr-bin
Requires: pbr-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Introduction
============
.. image:: https://img.shields.io/pypi/v/pbr.svg
:target: https://pypi.python.org/pypi/pbr/
:alt: Latest Version

%package bin
Summary: bin components for the pbr package.
Group: Binaries

%description bin
bin components for the pbr package.


%package python
Summary: python components for the pbr package.
Group: Default

%description python
python components for the pbr package.


%prep
%setup -q -n pbr-2.1.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492372475
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
export SOURCE_DATE_EPOCH=1492372475
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

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
