Name:           scrcpy
Version:        1.25
Release:        1
Summary:        Display and control your Android device from Linux OpenMandriva
License:        Apache-2.0
Group:          Applications/Internet
URL:            https://github.com/Genymobile/scrcpy
Source0:        https://github.com/Genymobile/scrcpy/archive/v%{version}/%{name}-%{version}.tar.gz
# We use prebuild server jar file, to save time and nerves without compiling it with java. Suggested by upstream anyway (angry)
# FIXME we should build from source at some point to make sure nobody hide any backdoors inside prebuilt files...
Source1:        https://github.com/Genymobile/scrcpy/releases/download/v%{version}/scrcpy-server-v%{version}.jar

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:	jdk-current
BuildRequires:	pkgconfig(sdl2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libusb-1.0)
Requires:  android-tools

%description
his application provides display and control of Android devices connected on USB (or over TCP/IP). 
It does not require any root access. It works on GNU/Linux, Windows and macOS.

%prep
%autosetup -p1

%build
. %{_sysconfdir}/profile.d/90java.sh
%meson -Dprebuilt_server=%{SOURCE1}
%meson_build

%install
. %{_sysconfdir}/profile.d/90java.sh
%meson_install

%files
%doc README.md DEVELOP.md FAQ.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/scrcpy.1.*
%{_iconsdir}/hicolor/*x*/apps/scrcpy.png
%{_datadir}/bash-completion/completions/scrcpy
%{_datadir}/zsh/site-functions/_scrcpy
