%global _debugsource_template %{nil}
%define module nh3

Name:		python-nh3
Version:	0.3.4
Release:	1
Summary:	Python binding to Ammonia HTML sanitizer Rust crate
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/nh3/
Source0:	https://github.com/messense/nh3/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz

BuildSystem:	python
BuildRequires:	cargo
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	rust-packaging

%description
Python binding to Ammonia HTML sanitizer Rust crate

%prep -a
# extract vendered sources
tar xf %{SOURCE1}
# prep vendorered crates
%cargo_prep -v vendor/
# create .cargo/config file from vendoring output
cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build -p
export RUSTFLAGS="-lpython%{pyver}"
export CARGO_HOME=$PWD/.cargo
# sort out crate licenses
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%files
%doc README.md
%license LICENSE LICENSES.dependencies
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
