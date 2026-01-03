Name:           maven-common-artifact-filters
Version:        3.4.0
Release:        1
Summary:        Maven Common Artifact Filters
License:        Apache-2.0
URL:            https://maven.apache.org/shared/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  javapackages-bootstrap

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%prep
%autosetup -p1 -C

# Test depends on jmh performance benchmarking library
%pom_remove_dep org.openjdk.jmh:jmh-core
%pom_remove_dep org.openjdk.jmh:jmh-generator-annprocess

rm src/test/java/org/apache/maven/shared/artifact/filter/PatternFilterPerfTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
