
%define plugin	director
%define name	vdr-plugin-%plugin
%define version	0.2.8
%define rel	17

Summary:	VDR plugin: plugin to use the premiere multifeed option
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.wontorra.net/staticpages/index.php?page=director
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		90_director-0.2.8-1.5.3.dpatch
Patch1:		director-0.2.8-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Director is a plugin to use the multifeed option of some Premiere
channels (Direkt, Sport Portal).

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
chmod -x HISTORY COPYING README
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY




%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.2.8-17mdv2011.0
+ Revision: 404565
- rebuild due to BS building the previous release against wrong VDR on i586

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.2.8-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.2.8-15mdv2009.1
+ Revision: 359306
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.2.8-14mdv2009.0
+ Revision: 197919
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.2.8-13mdv2009.0
+ Revision: 197650
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt to api changes of vdr 1.5.3 (P0 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.8-12mdv2008.1
+ Revision: 145065
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.2.8-11mdv2008.1
+ Revision: 103083
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.2.8-10mdv2008.0
+ Revision: 49989
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.8-9mdv2008.0
+ Revision: 42075
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.2.8-8mdv2008.0
+ Revision: 22738
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.2.8-7mdv2007.0
+ Revision: 90910
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.2.8-6mdv2007.1
+ Revision: 73982
- rebuild for new vdr
- Import vdr-plugin-director

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.8-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.2.8-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.8-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.2.8-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.2.8-1mdv2007.0
- initial Mandriva release

