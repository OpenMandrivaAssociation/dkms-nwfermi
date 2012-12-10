%define module_name nwfermi

Name:		dkms-%{module_name}
Version:	0.4.2
Release:	%mkrel 1
Summary:	DKMS-ready kernel-source for the %name driver
License:	GPL
URL:		http://www.fusionnetwork.us/index.php/articles/linux-tutorials/hp-touchsmart-300-touchscreen-linux-nextwindow-working/
Source:		%module_name-%{version}.tar.bz2
Group:		System/Kernel and hardware
Requires(pre):	dkms
Requires(post): dkms
Buildroot:	%{_tmppath}/%{name}-%{version}-root
Buildarch:	noarch

%description
Driver for USB touchscreen chipset,
Nextwindow Fermi touchscreen driver

%prep
%setup -q -n %module_name-%version

%build

%clean
rm -fr $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/src/%{module_name}-%{version}-%{release}
install -m 644 dkms.conf $RPM_BUILD_ROOT/usr/src/%{module_name}-%version-%release/dkms.conf
tar c . | tar x -C $RPM_BUILD_ROOT/usr/src/%{module_name}-%version-%release/


%post
   dkms add -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade
   dkms build -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade
   dkms install -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade

%preun
dkms remove -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade --all ||:

%files
%defattr(-,root,root)
/usr/src/%{module_name}-%{version}-%{release}



%changelog
* Fri Jan 07 2011 Antoine Ginies <aginies@mandriva.com> 0.4.2-1mdv2011.0
+ Revision: 629590
- import dkms-nwfermi

