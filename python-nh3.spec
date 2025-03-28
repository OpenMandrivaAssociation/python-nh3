%global debug_package %{nil}

Name:		python-nh3
Version:	0.2.21
Release:	6
Source0:	https://files.pythonhosted.org/packages/source/n/nh3/nh3-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Python binding to Ammonia HTML sanitizer Rust crate
URL:		https://pypi.org/project/nh3/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python-maturin
BuildRequires:	cargo
BuildSystem:	python



%description
Python binding to Ammonia HTML sanitizer Rust crate

%prep
%autosetup -n nh3-%{version} -a1
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%install -a
mkdir -p %{buildroot}/usr/lib/python3.11/site-packages
mkdir -p %{buildroot}/usr/lib64/python3.11/site-packages

%files
%{_libdir}/*
