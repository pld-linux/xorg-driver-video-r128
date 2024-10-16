Summary:	X.org video drivers for ATI Rage128 adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych ATI Rage128
Name:		xorg-driver-video-r128
Version:	6.13.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-r128-%{version}.tar.xz
# Source0-md5:	48b0a043ed79282e6b7c76ca187caa70
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.2
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.18
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.2
Requires:	xorg-xserver-libglx >= 1.18
Requires:	xorg-xserver-server >= 1.18
Provides:	xorg-driver-video
Obsoletes:	X11-driver-r128 < 1:7.0.0
Obsoletes:	XFree86-Rage128 < 4
Obsoletes:	XFree86-driver-r128 < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for ATI r128 adapters; supports all ATI Rage 128
based video cards including the Rage Fury AGP 32MB, the XPERT 128 AGP
16MB and the XPERT 99 AGP 8MB.

%description -l pl.UTF-8
Sterownik obrazu X.org do kart graficznych ATI r128; obsługuje
wszystkie karty graficzne oparte na układzie ATI Rage 128, włącznie z
Rage Fury AGP 32MB, XPERT 128 AGP 16MB i XPERT 99 AGP 8MB.

%prep
%setup -q -n xf86-video-r128-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/r128_drv.so
%{_mandir}/man4/r128.4*
