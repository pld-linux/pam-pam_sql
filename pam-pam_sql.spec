Summary:	PAM module for auth UNIX users using data base
Summary(pl):	modu³ PAM autentyfikuj±cy u¿ytkowników Linuksa poprzez bazê danych
Name:		pam-pam_sql
Version:	0.7.2
Release:	4
License:	GPL
Group:		Base
Source0:	http://devel.duluoz.net/pam_sql/pkgs/%{name}-%{version}.tar.gz
# Source0-md5:	50b01818609a8d8d3bdb2848f3083502
Patch0:		%{name}-postgresql-7.1.patch
Patch1:		%{name}-sqlinjection.patch
URL:		http://devel.duluoz.net/pam_sql/
BuildRequires:	autoconf
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel >= 7.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pam_sql aims to provide a backend neutral means of authenticating
users against an SQL database. The author uses PostgreSQL, but there's
also some mysql code leftover from the pam_mysql project (whence this
project evolved) that I'm quite sure doesn't work.

%description -l pl
Modu³ PAM pozwalaj±cy na autentyfikacjê u¿ytkowników Linuksa poprzez
bazê danych PostgreSQL lub MySQL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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
