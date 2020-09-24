#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : idle-python3.7-assets
Version  : 1.0.1
Release  : 4
URL      : https://gitlab.com/BobyMCbobs/idle-python3.7-assets/-/archive/1.0.1/idle-python3.7-assets-1.0.1.tar.gz
Source0  : https://gitlab.com/BobyMCbobs/idle-python3.7-assets/-/archive/1.0.1/idle-python3.7-assets-1.0.1.tar.gz
Summary  : Python's Intergrated Development and Learning Environment
Group    : Development/Tools
License  : GPL-3.0 Python-2.0
Requires: idle-python3.7-assets-data = %{version}-%{release}
Requires: idle-python3.7-assets-license = %{version}-%{release}

%description
An intergrated development environment for Python. Written in TkInter.

%package data
Summary: data components for the idle-python3.7-assets package.
Group: Data

%description data
data components for the idle-python3.7-assets package.


%package license
Summary: license components for the idle-python3.7-assets package.
Group: Default

%description license
license components for the idle-python3.7-assets package.


%prep
%setup -q -n idle-python3.7-assets-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569434735
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1569434735
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/idle-python3.7-assets
cp LICENSE %{buildroot}/usr/share/package-licenses/idle-python3.7-assets/LICENSE
%make_install DISTRO=openSUSE

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/idle-python3.7.desktop
/usr/share/pixmaps/python3.7.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/idle-python3.7-assets/LICENSE
