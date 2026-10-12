%global _debugsource_template %{nil}
%define module nh3

Name:		python-nh3
Version:	0.3.5
Release:	2
Summary:	Python binding to Ammonia HTML sanitizer Rust crate
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/nh3/
Source0:	https://github.com/messense/nh3/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz

BuildSystem:	python
BuildRequires:	cargo
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python binding to Ammonia HTML sanitizer Rust crate

%prep -a
# The crates are already vendored, so this build does not need rust-packaging.
tar -xf %{SOURCE1}
mkdir -p .cargo
cat > .cargo/config.toml << 'EOF'
[net]
offline = true

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build -p
export CARGO_NET_OFFLINE=true
export RUSTFLAGS="-lpython%{pyver}"
export CARGO_HOME=$PWD/.cargo
cargo tree --workspace --offline --edges no-build,no-dev,no-proc-macro \
	--prefix none --format '{l}: {p}' \
	| sed -e "s: ($(pwd)[^)]*)::g" -e 's: / :/:g' -e 's:/: OR :g' \
	| sort -u > LICENSES.dependencies

%files
%doc README.md
%license LICENSE LICENSES.dependencies
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
