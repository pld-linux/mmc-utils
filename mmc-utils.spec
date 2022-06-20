%define		snapdate	20220620
%define		gitcommit	b7e4d5a6ae9942d26a11de9b05ae7d52c0802802

Summary:	Tool for configuring MMC storage devices from userspace
Name:		mmc-utils
Version:	0
Release:	0.%{snapdate}.1
License:	GPL v2
Group:		Applications/System
Source0:	https://git.kernel.org/pub/scm/utils/mmc/mmc-utils.git/snapshot/%{name}-%{gitcommit}.tar.gz
# Source0-md5:	cf25e3725987c858ce33acb4e16ebf1d
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
