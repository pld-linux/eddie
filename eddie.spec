# TODO:
# - finish install
# - init.d script
Summary:	A system monitoring, security and performance analysis agent
Summary(pl):	Agent monitorowania systemu oraz analizy bezpiecze�stwa i wydajno�ci
Name:		eddie
Version:	0.35
Release:	0.1
License:	GPL v2
Group:		Daemons
Source0:	http://eddie-tool.net/download/pub/%{name}-%{version}.tgz
# Source0-md5:	c0f318b0b2fcbe2ed5966e04bebe3ef2
URL:		http://eddie-tool.net/
BuildRequires:	python >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The EDDIE Tool can perform all basic system monitoring checks, such
as: filesystem; processes; system load; and network configuration. It
can also perform such network monitoring tasks as: ping checks; HTTP
checks; POP3 tests; SNMP queries; RADIUS authentication tests; and
customized TCP port checks. Finally, a few checks lend themselves to
security monitoring: watching files for changes; and scanning
logfiles.

The EDDIE Tool can also send any collected statistic to RRD files to
be displayed graphically by any standard RRD tool. No need to run
multiple monitoring and data collection agents.

Monitoring rules are just like Python expressions and can be as simple
or as complex as needed. Advanced alert control functionality such as
exponential back-off and dependencies are also standard.

%description -l pl
EDDIE Tool mo�e wykonywa� wszystkie podstawowe testy monitoruj�ce
system, w tym: systemu plik�w, proces�w, obci��enia systemu,
konfiguracji sieci. Mo�e tak�e wykonywa� zadania zwi�zane z
monitorowaniem sieci, takie jak: sprawdzanie pinga, sprawdzanie HTTP,
testy POP3, zapytania SMTP, testy uwierzytelnienia RADIUS i w�asne
sposoby sprawdzania port�w TCP. Ponadto niekt�re testy rozci�gaj� si�
na monitorowanie bezpiecze�stwa: obserwowanie plik�w pod k�tem zmian i
skanowanie plik�w log�w.

EDDIE Tool mo�e tak�e wysy�a� dowolne zbiorcze statystyki do plik�w
RRD w celu graficznego wy�wietlenia przez dowolne standardowe
narz�dzie RRD. Nie ma potrzeby uruchamiania wielu agent�w do
monitorowania i zbierania danych.

Regu�y monitorowania to zwyk�e pythonowe wyra�enia, mog� by� proste
lub z�o�one w zale�no�ci od potrzeb. Dost�pna jest tak�e zaawansowana
funkcjonalno�� kontroli alarm�w, taka jak wyk�adnicze wycofywanie czy
zale�no�ci.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitescriptdir}/%{name},%{_sysconfdir}/%{name}}

install bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/Linux lib/common $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}
cp -a config.sample/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%dir %{_sysconfdir}/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.cf
%dir %{_sysconfdir}/%{name}/rules
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/rules/*.rules
