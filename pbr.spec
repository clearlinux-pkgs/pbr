#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pbr
Version  : 5.5.0
Release  : 96
URL      : https://files.pythonhosted.org/packages/f1/6b/25479e6b27c7fdf2550b97611c55e58245fc6c1ee8fb297056e1168832ff/pbr-5.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f1/6b/25479e6b27c7fdf2550b97611c55e58245fc6c1ee8fb297056e1168832ff/pbr-5.5.0.tar.gz
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
============

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
Provides: pypi(pbr)

%description python3
python3 components for the pbr package.


%prep
%setup -q -n pbr-5.5.0
cd %{_builddir}/pbr-5.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598995823
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
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
cp %{_builddir}/pbr-5.5.0/LICENSE %{buildroot}/usr/share/package-licenses/pbr/294b43b2cec9919063be1a3b49e8722648424779
cp %{_builddir}/pbr-5.5.0/pbr/tests/testpackage/LICENSE.txt %{buildroot}/usr/share/package-licenses/pbr/18184784896860da31dc6210e80eafa871d7a253
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
/usr/share/package-licenses/pbr/18184784896860da31dc6210e80eafa871d7a253
/usr/share/package-licenses/pbr/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
