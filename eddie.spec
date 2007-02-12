# TODO:
# - finish install
# - init.d script
Summary:	A system monitoring, security and performance analysis agent
Summary(pl.UTF-8):   Agent monitorowania systemu oraz analizy bezpieczeństwa i wydajności
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

%description -l pl.UTF-8
EDDIE Tool może wykonywać wszystkie podstawowe testy monitorujące
system, w tym: systemu plików, procesów, obciążenia systemu,
konfiguracji sieci. Może także wykonywać zadania związane z
monitorowaniem sieci, takie jak: sprawdzanie pinga, sprawdzanie HTTP,
testy POP3, zapytania SMTP, testy uwierzytelnienia RADIUS i własne
sposoby sprawdzania portów TCP. Ponadto niektóre testy rozciągają się
na monitorowanie bezpieczeństwa: obserwowanie plików pod kątem zmian i
skanowanie plików logów.

EDDIE Tool może także wysyłać dowolne zbiorcze statystyki do plików
RRD w celu graficznego wyświetlenia przez dowolne standardowe
narzędzie RRD. Nie ma potrzeby uruchamiania wielu agentów do
monitorowania i zbierania danych.

Reguły monitorowania to zwykłe pythonowe wyrażenia, mogą być proste
lub złożone w zależności od potrzeb. Dostępna jest także zaawansowana
funkcjonalność kontroli alarmów, taka jak wykładnicze wycofywanie czy
zależności.

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
