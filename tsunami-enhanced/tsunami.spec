Summary: Tsunami UDP file transport
Name: tsunami
Version: 1.1b43
Release: 1
License: Indiana University
Group: VLBI
BuildRoot: /var/tmp/tsunami-1.1b43-buildroot
Requires: gcc >= 4.1.0
Prefix: /usr
Source: tsunami-%{version}.tar.gz

%define debug_package %{nil}

%description
Fast UDP-based file transport protocol.  First developed by University
of Indiana.  Then further developed by Jan Wagner (Metsahovi) and finally
with some additions by Walter Brisken (NRAO)

%prep
%setup -q -n tsunami-%{version}

%build
./configure --prefix=$RPM_BUILD_ROOT/usr
make

%install
make install

%files
%defattr(-,root,root)
%{_bindir}/tsunami
%{_bindir}/tsunamid
%{_bindir}/rttsunami
%{_bindir}/rttsunamid

%changelog
* Sat Jul 20 2013 Walter Brisken <wbrisken@nrao.edu>
- Walter's first version, 0.92wb
* Thu Aug 15 2013 Jan Wagner <jwagner@mpifr.de>
- merged Walters changes into sourceforge CVS repository
