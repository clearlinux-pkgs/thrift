#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thrift
Version  : 0.11.0
Release  : 26
URL      : http://pypi.debian.net/thrift/thrift-0.11.0.tar.gz
Source0  : http://pypi.debian.net/thrift/thrift-0.11.0.tar.gz
Summary  : Python bindings for the Apache Thrift RPC system
Group    : Development/Tools
License  : Apache-2.0
Requires: thrift-python3
Requires: thrift-python
Requires: backports.ssl_match_hostname
Requires: ipaddress
Requires: six
Requires: tornado
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
No detailed description available

%package python
Summary: python components for the thrift package.
Group: Default
Requires: thrift-python3

%description python
python components for the thrift package.


%package python3
Summary: python3 components for the thrift package.
Group: Default
Requires: python3-core

%description python3
python3 components for the thrift package.


%prep
%setup -q -n thrift-0.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536181236
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
