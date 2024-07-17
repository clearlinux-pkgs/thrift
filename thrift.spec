#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v16
# autospec commit: b858a2a
#
Name     : thrift
Version  : 0.20.0
Release  : 63
URL      : https://github.com/apache/thrift/archive/v0.20.0/thrift-0.20.0.tar.gz
Source0  : https://github.com/apache/thrift/archive/v0.20.0/thrift-0.20.0.tar.gz
Summary  : RPC and serialization framework
Group    : Development/Tools
License  : Apache-2.0 FSFAP LGPL-2.1 MIT Zlib
Requires: thrift-bin = %{version}-%{release}
Requires: thrift-lib = %{version}-%{release}
Requires: thrift-license = %{version}-%{release}
Requires: thrift-python = %{version}-%{release}
Requires: thrift-python3 = %{version}-%{release}
BuildRequires : bison
BuildRequires : boost-dev
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : nodejs
BuildRequires : openssl-dev
BuildRequires : otp
BuildRequires : perl(Test::Exception)
BuildRequires : perl-Bit-Vector
BuildRequires : perl-Class-Accessor
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Thrift is a software framework for scalable cross-language services
development. It combines a powerful software stack with a code generation
engine to build services that work efficiently and seamlessly between C++,
Java, C#, Python, Ruby, Perl, PHP, Smalltalk, Erlang, OCaml, Haskell, and
other languages.

%package bin
Summary: bin components for the thrift package.
Group: Binaries
Requires: thrift-license = %{version}-%{release}

%description bin
bin components for the thrift package.


%package dev
Summary: dev components for the thrift package.
Group: Development
Requires: thrift-lib = %{version}-%{release}
Requires: thrift-bin = %{version}-%{release}
Provides: thrift-devel = %{version}-%{release}
Requires: thrift = %{version}-%{release}

%description dev
dev components for the thrift package.


%package lib
Summary: lib components for the thrift package.
Group: Libraries
Requires: thrift-license = %{version}-%{release}

%description lib
lib components for the thrift package.


%package license
Summary: license components for the thrift package.
Group: Default

%description license
license components for the thrift package.


%package python
Summary: python components for the thrift package.
Group: Default
Requires: thrift-python3 = %{version}-%{release}

%description python
python components for the thrift package.


%package python3
Summary: python3 components for the thrift package.
Group: Default
Requires: python3-core
Requires: pypi(six)

%description python3
python3 components for the thrift package.


%prep
%setup -q -n thrift-0.20.0
cd %{_builddir}/thrift-0.20.0
pushd ..
cp -a thrift-0.20.0 buildavx2
popd

%build
## build_prepend content
./bootstrap.sh
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721238821
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --with-csharp=no \
--with-dotnetcore=no \
--with-go=no \
--with-nodejs=no \
--with-perl=yes \
--with-php=no \
--with-python=yes \
--with-qt4=no \
--with-qt5=yes \
--with-rs=no \
--with-ruby=no \
--with-java=no
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
./bootstrap.sh
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --with-csharp=no \
--with-dotnetcore=no \
--with-go=no \
--with-nodejs=no \
--with-perl=yes \
--with-php=no \
--with-python=yes \
--with-qt4=no \
--with-qt5=yes \
--with-rs=no \
--with-ruby=no \
--with-java=no
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1721238821
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/thrift
cp %{_builddir}/thrift-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/thrift/104c027505ef428a77fdbaa2e3713b52c8d3cfc4 || :
cp %{_builddir}/thrift-%{version}/contrib/fb303/LICENSE %{buildroot}/usr/share/package-licenses/thrift/0d359463862b027340624ba0f1e357a316d04931 || :
cp %{_builddir}/thrift-%{version}/doc/licenses/otp-base-license.txt %{buildroot}/usr/share/package-licenses/thrift/ba013932d429012281592d6851de646407c757bf || :
cp %{_builddir}/thrift-%{version}/doc/licenses/otp-base-license.txt %{buildroot}/usr/share/package-licenses/thrift/ba013932d429012281592d6851de646407c757bf || :
cp %{_builddir}/thrift-%{version}/lib/dart/LICENSE %{buildroot}/usr/share/package-licenses/thrift/0d359463862b027340624ba0f1e357a316d04931 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/thrift
/usr/bin/thrift

%files dev
%defattr(-,root,root,-)
/usr/include/thrift/TApplicationException.h
/usr/include/thrift/TBase.h
/usr/include/thrift/TConfiguration.h
/usr/include/thrift/TDispatchProcessor.h
/usr/include/thrift/TLogging.h
/usr/include/thrift/TNonCopyable.h
/usr/include/thrift/TOutput.h
/usr/include/thrift/TProcessor.h
/usr/include/thrift/TToString.h
/usr/include/thrift/Thrift.h
/usr/include/thrift/async/TAsyncBufferProcessor.h
/usr/include/thrift/async/TAsyncChannel.h
/usr/include/thrift/async/TAsyncDispatchProcessor.h
/usr/include/thrift/async/TAsyncProcessor.h
/usr/include/thrift/async/TAsyncProtocolProcessor.h
/usr/include/thrift/async/TConcurrentClientSyncInfo.h
/usr/include/thrift/async/TEvhttpClientChannel.h
/usr/include/thrift/async/TEvhttpServer.h
/usr/include/thrift/c_glib/config.h
/usr/include/thrift/c_glib/processor/thrift_dispatch_processor.h
/usr/include/thrift/c_glib/processor/thrift_multiplexed_processor.h
/usr/include/thrift/c_glib/processor/thrift_processor.h
/usr/include/thrift/c_glib/protocol/thrift_binary_protocol.h
/usr/include/thrift/c_glib/protocol/thrift_binary_protocol_factory.h
/usr/include/thrift/c_glib/protocol/thrift_compact_protocol.h
/usr/include/thrift/c_glib/protocol/thrift_compact_protocol_factory.h
/usr/include/thrift/c_glib/protocol/thrift_multiplexed_protocol.h
/usr/include/thrift/c_glib/protocol/thrift_protocol.h
/usr/include/thrift/c_glib/protocol/thrift_protocol_decorator.h
/usr/include/thrift/c_glib/protocol/thrift_protocol_factory.h
/usr/include/thrift/c_glib/protocol/thrift_stored_message_protocol.h
/usr/include/thrift/c_glib/server/thrift_server.h
/usr/include/thrift/c_glib/server/thrift_simple_server.h
/usr/include/thrift/c_glib/thrift.h
/usr/include/thrift/c_glib/thrift_application_exception.h
/usr/include/thrift/c_glib/thrift_configuration.h
/usr/include/thrift/c_glib/thrift_struct.h
/usr/include/thrift/c_glib/transport/thrift_buffered_transport.h
/usr/include/thrift/c_glib/transport/thrift_buffered_transport_factory.h
/usr/include/thrift/c_glib/transport/thrift_fd_transport.h
/usr/include/thrift/c_glib/transport/thrift_framed_transport.h
/usr/include/thrift/c_glib/transport/thrift_framed_transport_factory.h
/usr/include/thrift/c_glib/transport/thrift_memory_buffer.h
/usr/include/thrift/c_glib/transport/thrift_platform_socket.h
/usr/include/thrift/c_glib/transport/thrift_server_socket.h
/usr/include/thrift/c_glib/transport/thrift_server_transport.h
/usr/include/thrift/c_glib/transport/thrift_socket.h
/usr/include/thrift/c_glib/transport/thrift_ssl_socket.h
/usr/include/thrift/c_glib/transport/thrift_transport.h
/usr/include/thrift/c_glib/transport/thrift_transport_factory.h
/usr/include/thrift/c_glib/transport/thrift_zlib_transport.h
/usr/include/thrift/c_glib/transport/thrift_zlib_transport_factory.h
/usr/include/thrift/concurrency/Exception.h
/usr/include/thrift/concurrency/FunctionRunner.h
/usr/include/thrift/concurrency/Monitor.h
/usr/include/thrift/concurrency/Mutex.h
/usr/include/thrift/concurrency/Thread.h
/usr/include/thrift/concurrency/ThreadFactory.h
/usr/include/thrift/concurrency/ThreadManager.h
/usr/include/thrift/concurrency/TimerManager.h
/usr/include/thrift/config.h
/usr/include/thrift/processor/PeekProcessor.h
/usr/include/thrift/processor/StatsProcessor.h
/usr/include/thrift/processor/TMultiplexedProcessor.h
/usr/include/thrift/protocol/TBase64Utils.h
/usr/include/thrift/protocol/TBinaryProtocol.h
/usr/include/thrift/protocol/TBinaryProtocol.tcc
/usr/include/thrift/protocol/TCompactProtocol.h
/usr/include/thrift/protocol/TCompactProtocol.tcc
/usr/include/thrift/protocol/TDebugProtocol.h
/usr/include/thrift/protocol/TEnum.h
/usr/include/thrift/protocol/THeaderProtocol.h
/usr/include/thrift/protocol/TJSONProtocol.h
/usr/include/thrift/protocol/TList.h
/usr/include/thrift/protocol/TMap.h
/usr/include/thrift/protocol/TMultiplexedProtocol.h
/usr/include/thrift/protocol/TProtocol.h
/usr/include/thrift/protocol/TProtocolDecorator.h
/usr/include/thrift/protocol/TProtocolException.h
/usr/include/thrift/protocol/TProtocolTap.h
/usr/include/thrift/protocol/TProtocolTypes.h
/usr/include/thrift/protocol/TSet.h
/usr/include/thrift/protocol/TVirtualProtocol.h
/usr/include/thrift/qt/TQIODeviceTransport.h
/usr/include/thrift/qt/TQTcpServer.h
/usr/include/thrift/server/TConnectedClient.h
/usr/include/thrift/server/TNonblockingServer.h
/usr/include/thrift/server/TServer.h
/usr/include/thrift/server/TServerFramework.h
/usr/include/thrift/server/TSimpleServer.h
/usr/include/thrift/server/TThreadPoolServer.h
/usr/include/thrift/server/TThreadedServer.h
/usr/include/thrift/thrift-config.h
/usr/include/thrift/thrift_export.h
/usr/include/thrift/transport/PlatformSocket.h
/usr/include/thrift/transport/SocketCommon.h
/usr/include/thrift/transport/TBufferTransports.h
/usr/include/thrift/transport/TFDTransport.h
/usr/include/thrift/transport/TFileTransport.h
/usr/include/thrift/transport/THeaderTransport.h
/usr/include/thrift/transport/THttpClient.h
/usr/include/thrift/transport/THttpServer.h
/usr/include/thrift/transport/THttpTransport.h
/usr/include/thrift/transport/TNonblockingSSLServerSocket.h
/usr/include/thrift/transport/TNonblockingServerSocket.h
/usr/include/thrift/transport/TNonblockingServerTransport.h
/usr/include/thrift/transport/TPipe.h
/usr/include/thrift/transport/TPipeServer.h
/usr/include/thrift/transport/TSSLServerSocket.h
/usr/include/thrift/transport/TSSLSocket.h
/usr/include/thrift/transport/TServerSocket.h
/usr/include/thrift/transport/TServerTransport.h
/usr/include/thrift/transport/TShortReadTransport.h
/usr/include/thrift/transport/TSimpleFileTransport.h
/usr/include/thrift/transport/TSocket.h
/usr/include/thrift/transport/TSocketPool.h
/usr/include/thrift/transport/TSocketUtils.h
/usr/include/thrift/transport/TTransport.h
/usr/include/thrift/transport/TTransportException.h
/usr/include/thrift/transport/TTransportUtils.h
/usr/include/thrift/transport/TVirtualTransport.h
/usr/include/thrift/transport/TWebSocketServer.h
/usr/include/thrift/transport/TZlibTransport.h
/usr/lib64/pkgconfig/thrift-z.pc
/usr/lib64/pkgconfig/thrift.pc
/usr/lib64/pkgconfig/thrift_c_glib.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libthrift-0.20.0.so
/V3/usr/lib64/libthrift_c_glib.so.0.0.0
/V3/usr/lib64/libthriftz-0.20.0.so
/usr/lib64/libthrift-0.20.0.so
/usr/lib64/libthrift.so
/usr/lib64/libthrift_c_glib.so
/usr/lib64/libthrift_c_glib.so.0
/usr/lib64/libthrift_c_glib.so.0.0.0
/usr/lib64/libthriftz-0.20.0.so
/usr/lib64/libthriftz.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/thrift/0d359463862b027340624ba0f1e357a316d04931
/usr/share/package-licenses/thrift/104c027505ef428a77fdbaa2e3713b52c8d3cfc4
/usr/share/package-licenses/thrift/ba013932d429012281592d6851de646407c757bf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
