#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pbr
Version  : 1.10.0
Release  : 27
URL      : http://pypi.debian.net/pbr/pbr-1.10.0.tar.gz
Source0  : http://pypi.debian.net/pbr/pbr-1.10.0.tar.gz
Summary  : Python Build Reasonableness
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pbr-bin
Requires: pbr-python
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Sphinx
BuildRequires : coverage
BuildRequires : discover
BuildRequires : docutils
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : flake8
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : imagesize-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : subunit
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : virtualenv-python
BuildRequires : wheel

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
%setup -q -n pbr-1.10.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pbr

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
