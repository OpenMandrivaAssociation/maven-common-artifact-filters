%{?_javapackages_macros:%_javapackages_macros}
Name:          maven-common-artifact-filters
Version:       1.4
Release:       11.1%{?dist}
Summary:       Maven Common Artifact Filters
License:       ASL 2.0
Url:           http://maven.apache.org/shared/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: easymock3

BuildRequires: maven-shared
BuildRequires: maven-resources-plugin
BuildRequires: plexus-containers-container-default
BuildRequires: maven-test-tools
BuildRequires: maven-plugin-testing-harness


Provides:      maven-shared-common-artifact-filters = %{version}-%{release}
Obsoletes:     maven-shared-common-artifact-filters < %{version}-%{release}

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

# Maven 2 -> Maven 3
%pom_remove_dep :maven-project
%pom_add_dep org.apache.maven:maven-core
%pom_add_dep org.apache.maven:maven-compat
%pom_xpath_set "pom:dependency[pom:groupId[text()='org.apache.maven']]/pom:version" 3.0.4

# Workaround for rhbz#911365
%pom_add_dep aopalliance:aopalliance::test
%pom_add_dep cglib:cglib::test

# Migrate from easymock 1 to easymock 3
%pom_remove_dep easymock:
%pom_add_dep org.easymock:easymock:3.2:test

%build
# NoSuchMethodError: org.easymock.internal.ObjectMethodsFilter.<init>(Ljava/lang/reflect/InvocationHandler;)V
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Aug 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11
- Migrate from easymock 1 to easymock 3
- Resolves: rhbz#1002476

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Michal Srb <msrb@redhat.com> - 1.4-9
- Enable tests again, they don't cause any trouble anywhere

* Thu Apr 11 2013 Michal Srb <msrb@redhat.com> - 1.4-8
- Run tests only in Fedora

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7
- Build with xmvn
- Bring back BR on maven-shared

* Mon Feb 18 2013 Tomas Radej <tradej@redhat.com> - 1.4-6
- Removed B/R on maven-shared (unnecessary + blocking maven-shared retirement)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 22 2012 gil <puntogil@libero.it> 1.4-3
- resolves rhbz#879363 (NOTICE file is not installed with javadoc package)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 gil cattaneo <puntogil@libero.it> 1.4-1
- initial rpm
