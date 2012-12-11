%define realname TK
%define modname tk
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A31_%{modname}.ini

Summary:	Provides TK functions for PHP
Name:		php-%{modname}
Version:	0.1.1
Release:	%mkrel 32
Group:		Development/PHP
License:	PHP License
URL:		http://php-tk.sourceforge.net/
Source0:	tk-%{version}.tar.bz2
Patch0:		tk-0.1.1-lib64.diff
Patch1:		tk-0.1.1-format_not_a_string_literal_and_no_format_arguments.diff
Patch2:		tk-0.1.1-php54x.diff
Requires:	php-cli >= 3:5.2.0
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	tk tk-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHP/TK is an native extension for the PHP programming language that implements
language bindings for TCL/TK. It provides an object-oriented interface and
greatly simplifies writing client-side cross-platform GUI applications. 

%prep

%setup -q -n tk-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%serverbuild
phpize
%configure2_5x
%make

mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
[ "../package.xml" != "/" ] && rm -f ../package.xml

%files 
%defattr(-,root,root)
%doc tests CREDITS
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-32mdv2012.0
+ Revision: 796976
- fix build
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-31
+ Revision: 761337
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-30
+ Revision: 696482
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-29
+ Revision: 695477
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-28
+ Revision: 646696
- rebuilt for php-5.3.6

* Mon Feb 07 2011 Funda Wang <fwang@mandriva.org> 0.1.1-27
+ Revision: 636561
- tighten BR

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-26mdv2011.0
+ Revision: 629893
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-25mdv2011.0
+ Revision: 628201
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-24mdv2011.0
+ Revision: 600542
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-23mdv2011.0
+ Revision: 588879
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-22mdv2010.1
+ Revision: 514698
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-21mdv2010.1
+ Revision: 485494
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-20mdv2010.1
+ Revision: 468265
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-19mdv2010.0
+ Revision: 451367
- rebuild

* Sun Jul 19 2009 RaphaÃ«l Gertz <rapsys@mandriva.org> 0.1.1-18mdv2010.0
+ Revision: 397623
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-17mdv2010.0
+ Revision: 377037
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-16mdv2009.1
+ Revision: 346679
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-15mdv2009.1
+ Revision: 341841
- rebuilt against php-5.2.9RC2

* Sun Jan 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-14mdv2009.1
+ Revision: 324397
- fix build with -Werror=format-security

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-13mdv2009.1
+ Revision: 310317
- rebuilt against php-5.2.7

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-12mdv2009.0
+ Revision: 238452
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-11mdv2009.0
+ Revision: 200278
- rebuilt for php-5.2.6

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-10mdv2008.1
+ Revision: 162255
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-9mdv2008.1
+ Revision: 107734
- restart apache if needed

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.1.1-8mdv2008.0
+ Revision: 82077
- rebuild for new soname of tk

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-7mdv2008.0
+ Revision: 77586
- rebuilt against php-5.2.4

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-6mdv2008.0
+ Revision: 39531
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-5mdv2008.0
+ Revision: 33884
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-4mdv2008.0
+ Revision: 21364
- rebuilt against new upstream version (5.2.2)


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-3mdv2007.0
+ Revision: 117637
- rebuilt against new upstream version (5.2.1)

* Wed Nov 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-2mdv2007.0
+ Revision: 78112
- rebuilt for php-5.2.0
- Import php-tk

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-1
- rebuilt for php-5.1.6

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.1-5
- rebuilt for php-4.4.4

* Sun Aug 06 2006 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.1-4mdv2007.0
- rebuilt for php-4.4.3

* Wed Jul 26 2006 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.1-3mdk
- rebuild

* Mon Jan 16 2006 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.1-2mdk
- rebuilt against php-4.4.2

* Wed Nov 02 2005 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.1-1mdk
- rebuilt for php-4.4.1
- fix versioning

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 4.4.0-2mdk
- Fix BuildRequires

* Tue Jul 12 2005 Oden Eriksson <oeriksson@mandriva.com> 4.4.0-1mdk
- rebuilt for php-4.4.0 final

* Wed Jul 06 2005 Oden Eriksson <oeriksson@mandriva.com> 4.4.0-0.RC2.1mdk
- rebuilt for php-4.4.0RC2

* Wed Jun 15 2005 Oden Eriksson <oeriksson@mandriva.com> 4.4.0_0.1.1-0.RC1.1mdk
- rebuilt for php-4.4.0RC1

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 4.3.11_0.1.1-1mdk
- renamed to php4-*

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 4.3.11_0.1.1-1mdk
- 4.3.11

* Mon Mar 21 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_0.1.1-4mdk
- use the %%mkrel macro

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_0.1.1-3mdk
- rebuilt against a non hardened-php aware php lib

* Sat Jan 15 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_0.1.1-2mdk
- rebuild due to hardened-php-0.2.6
- cleanups

* Sat Jan 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_0.1.1-1mdk
- initial mandrake package
- added P0

