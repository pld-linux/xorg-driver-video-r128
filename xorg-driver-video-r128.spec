Summary:	X.org video drivers for ATI Rage128 adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych ATI Rage128
Name:		xorg-driver-video-r128
Version:	6.8.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-r128-%{version}.tar.bz2
# Source0-md5:	007bec0c6b07d9d3aeca4da18e561efb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.1.0
Obsoletes:	X11-driver-r128 < 1:7.0.0
Obsoletes:	XFree86-Rage128
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
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/r128_drv.so
%{_mandir}/man4/r128.4*
