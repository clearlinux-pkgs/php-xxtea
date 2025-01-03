#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-xxtea
Version  : 1.0.11
Release  : 68
URL      : https://pecl.php.net//get/xxtea-1.0.11.tgz
Source0  : https://pecl.php.net//get/xxtea-1.0.11.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-xxtea-lib = %{version}-%{release}
Requires: php-xxtea-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: PHP-8.patch

%description
# XXTEA 加密算法的 PHP 扩展实现
<a href="https://github.com/xxtea/">
<img src="https://avatars1.githubusercontent.com/u/6683159?v=3&s=86" alt="XXTEA logo" title="XXTEA" align="right" />
</a>

%package lib
Summary: lib components for the php-xxtea package.
Group: Libraries
Requires: php-xxtea-license = %{version}-%{release}

%description lib
lib components for the php-xxtea package.


%package license
Summary: license components for the php-xxtea package.
Group: Default

%description license
license components for the php-xxtea package.


%prep
%setup -q -n xxtea-1.0.11
cd %{_builddir}/xxtea-1.0.11
%patch -P 1 -p1
pushd ..
cp -a xxtea-1.0.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-xxtea
cp %{_builddir}/xxtea-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/php-xxtea/92c9278302c949af80357a0b6da18e1f13c1b1dc || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/xxtea.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-xxtea/92c9278302c949af80357a0b6da18e1f13c1b1dc
