#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thrift
Version  : 0.10.0
Release  : 21
URL      : http://pypi.debian.net/thrift/thrift-0.10.0.zip
Source0  : http://pypi.debian.net/thrift/thrift-0.10.0.zip
Summary  : Python bindings for the Apache Thrift RPC system
Group    : Development/Tools
License  : Apache-2.0
Requires: thrift-python
Requires: backports.ssl_match_hostname
Requires: ipaddress
Requires: six
Requires: tornado
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
No detailed description available

%package python
Summary: python components for the thrift package.
Group: Default

%description python
python components for the thrift package.


%prep
%setup -q -n thrift-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503082181
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1503082181
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
