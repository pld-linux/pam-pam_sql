%define 	modulename pam_sql
Summary:	PAM module for authenticating users against SQL database
Summary(pl.UTF-8):   Moduł PAM uwierzytelniający użytkowników względem bazy danych
Name:		pam-%{modulename}
Version:	0.7.2
Release:	7
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://www.duluoz.net/%{modulename}/pkgs/%{modulename}-%{version}.tar.gz
# Source0-md5:	50b01818609a8d8d3bdb2848f3083502
Patch0:		%{name}-postgresql-7.1.patch
Patch1:		%{name}-sqlinjection.patch
URL:		http://www.duluoz.net/pam_sql/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel >= 7.2
Obsoletes:	pam_sql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_sql aims to provide a backend neutral means of authenticating
users against an SQL database. The author uses PostgreSQL, but there's
also some MySQL code leftover from the pam_mysql project (whence this
project evolved) that I'm quite sure doesn't work.

%description -l pl.UTF-8
pam_sql to moduł PAM mający na celu uwierzytelnianie użytkowników
względem bazy SQL niezależnie od używanego backendu. Autor używa
PostgreSQL-a, ale obecny jest także kod dla MySQL-a z projektu
pam_mysql (który prawdopodobnie na razie nie działa).

%prep
%setup -q -n %{modulename}-%{version}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* tools
%{__autoconf}
%configure \
	--with-postgres

%{__make} \
	CFLAGS="%{rpmcflags} -DUSE_POSTGRES -DHAVE_INLINE"

%install
rm -rf $RPM_BUILD_ROOT

install -D pam_sql $RPM_BUILD_ROOT/%{_lib}/security/pam_sql.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) /%{_lib}/security/pam_sql.so
