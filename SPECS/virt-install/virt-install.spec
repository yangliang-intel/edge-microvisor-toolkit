Summary:        Utilities for installing virtual machines
Name:           virt-install
Version:        4.1.0
Release:        1%{?dist}
License:        GPLv2+
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
BuildArch:      noarch
URL:            https://virt-manager.org/
Source0:        https://releases.pagure.org/virt-manager/virt-manager-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk3-devel

# CLI runtime dependencies
Requires:       python3-libvirt
Requires:       python3-libxml2
Requires:       python3-requests
Requires:       libvirt-client

%description
Package includes virt-install, virt-clone, and virt-xml for creating and managing
virtual machines from the command line.

%prep
%autosetup -n virt-manager-%{version}

%build
python3 setup.py build

%install
# Pre-create necessary GTK icon cache file so gtk-update-icon-cache succeeds
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
touch %{buildroot}%{_datadir}/icons/hicolor/.icon-theme.cache

python3 setup.py install --skip-build --root=%{buildroot}

# Manually install bash-completion files (skipped by --skip-build)
install -d %{buildroot}%{_datadir}/bash-completion/completions/
install -m 644 build/bash-completion/virt-install %{buildroot}%{_datadir}/bash-completion/completions/virt-install
install -m 644 build/bash-completion/virt-clone   %{buildroot}%{_datadir}/bash-completion/completions/virt-clone
install -m 644 build/bash-completion/virt-xml     %{buildroot}%{_datadir}/bash-completion/completions/virt-xml

# Remove GUI components - CLI only
rm -f %{buildroot}%{_bindir}/virt-manager
rm -rf %{buildroot}%{_datadir}/applications/
rm -rf %{buildroot}%{_datadir}/icons/
rm -rf %{buildroot}%{_datadir}/metainfo/
rm -rf %{buildroot}%{_datadir}/glib-2.0/
rm -rf %{buildroot}%{_datadir}/virt-manager/ui/
rm -rf %{buildroot}%{_datadir}/virt-manager/virtManager/
rm -f  %{buildroot}%{_mandir}/man1/virt-manager.1*

%files
%license COPYING
%doc README.md NEWS.md
%{_bindir}/virt-install
%{_bindir}/virt-clone
%{_bindir}/virt-xml
%{_mandir}/man1/virt-install.1*
%{_mandir}/man1/virt-clone.1*
%{_mandir}/man1/virt-xml.1*
%{_datadir}/bash-completion/completions/virt-install
%{_datadir}/bash-completion/completions/virt-clone
%{_datadir}/bash-completion/completions/virt-xml
%{_datadir}/virt-manager/virtinst/

%changelog
* Thu Apr 04 2026 Liang Yang <liang1.yang@intel.com> - 4.1.0-1
- Initial virt-install package for Edge Microvisor Toolkit
- Initial Edge Microvisor Toolkit import from the source project (license: same as "License" tag).
- Command-line VM installation and management tools only from virt-manager-4.1.0 package

