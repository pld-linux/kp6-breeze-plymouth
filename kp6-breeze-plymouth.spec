#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.0.3
%define		qtver		5.15.2
%define		kpname		breeze-plymouth

Summary:	breeze-plymouth
Name:		kp6-%{kpname}
Version:	6.0.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	83885a3eba356552f094874192c31c28
URL:		http://www.kde.org/
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf6-extra-cmake-modules >= 1.8.0
BuildRequires:	ninja
BuildRequires:	plymouth-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
breeze-plymouth.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/breeze-text.so
%{_datadir}/plymouth/themes/breeze-text
%{_datadir}/plymouth/themes/breeze
