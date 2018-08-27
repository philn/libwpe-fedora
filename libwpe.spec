Name:           libwpe
Version:        1.0.0
Release:        1%{?dist}
Summary:        General-purpose library for the WPE-flavored port of WebKit

License:        BSD
URL:            https://github.com/WebPlatformForEmbedded/%{name}
Source0:        https://github.com/WebPlatformForEmbedded/libwpe/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mesa-libEGL-devel
BuildRequires:  libxkbcommon-devel

Provides: wpebackend = %{version}-%{release}
Obsoletes: wpebackend < 0.2.0-2

%description
General-purpose library developed for the WPE-flavored port of WebKit

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -p1 -n libwpe-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  ..
popd

%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files
%license COPYING
%doc NEWS
%{_libdir}/libwpe-0.2.so.1.*
%{_libdir}/libwpe-0.2.so.1

%files devel
%{_includedir}/wpe-0.2/
%{_libdir}/libwpe-0.2.so
%{_libdir}/pkgconfig/wpe-0.2.pc

%changelog
* Mon Aug 27 2018 Chris King <bunnyapocalypse@protonmail.org> - 1.0.0-1
- Initial RPM package
