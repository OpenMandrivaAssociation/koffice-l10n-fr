Name: koffice-l10n-fr
Version: 2.2.81
Release: %mkrel 1
Summary: Language files for KOffice French
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: http://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/unstable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
Patch0: koffice-l10n-fr-2.2.0-fix-build.patch
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-fr
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides French translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0 -b .orig

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot
