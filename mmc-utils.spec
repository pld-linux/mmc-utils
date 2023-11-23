%define		snapdate	20231010
%define		gitcommit	b5ca140312d279ad2f22068fd72a6230eea13436

Summary:	Tool for configuring MMC storage devices from userspace
Name:		mmc-utils
Version:	0
Release:	0.%{snapdate}.1
License:	GPL v2
Group:		Applications/System
Source0:	https://git.kernel.org/pub/scm/utils/mmc/mmc-utils.git/snapshot/%{name}-%{gitcommit}.tar.gz
# Source0-md5:	8d15562e038f232b1e9f542cfcd3b0b3
URL:		https://git.kernel.org/pub/scm/utils/mmc/mmc-utils.git/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for configuring MMC storage devices from userspace.

%prep
%setup -q -n %{name}-%{gitcommit}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	GIT_VERSION=%(echo %{gitcommit} | cut -c -6)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir="%{_bindir}"

cp -p man/mmc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mmc
%{_mandir}/man1/mmc.1*
