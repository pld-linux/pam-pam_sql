%define 	modulename pam_sql
Summary:	PAM module for auth UNIX users using data base
Summary(pl):	modu� PAM autentyfikuj�cy u�ytkownik�w Linuksa poprzez baz� danych
Name:		pam-%{modulename}
Version:	0.7.2
Release:	6
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://www.duluoz.net/%{modulename}/pkgs/%{modulename}-%{version}.tar.gz
# Source0-md5:	50b01818609a8d8d3bdb2848f3083502
Patch0:		%{name}-postgresql-7.1.patch
Patch1:		%{name}-sqlinjection.patch
URL:		http://www.duluoz.net/%{modulename}/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel >= 7.2
Obsoletes:	pam_sql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pam_sql aims to provide a backend neutral means of authenticating
users against an SQL database. The author uses PostgreSQL, but there's
also some mysql code leftover from the pam_mysql project (whence this
project evolved) that I'm quite sure doesn't work.

%description -l pl
Modu� PAM pozwalaj�cy na autentyfikacj� u�ytkownik�w Linuksa poprzez
baz� danych PostgreSQL lub MySQL.

%prep
%setup -q -n %{modulename}-%{version}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* tools
%{__autoconf}
%configure \
	--with-postgres

%{__make} CFLAGS="%{rpmcflags} -DUSE_POSTGRES -DHAVE_INLINE"

%install
rm -rf $RPM_BUILD_ROOT

install -D pam_sql $RPM_BUILD_ROOT/lib/security/pam_sql.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) /lib/security/pam_sql.so