%define realname TK
%define modname tk
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A31_%{modname}.ini

Summary:	Provides TK functions for PHP
Name:		php-%{modname}
Version:	0.1.1
Release:	%mkrel 7
Group:		Development/PHP
License:	PHP License
URL:		http://php-tk.sourceforge.net/
Source0:	tk-%{version}.tar.bz2
Patch0:		tk-0.1.1-lib64.diff
Requires:	php-cli >= 3:5.2.0
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	tk tk-devel
BuildRequires:  X11-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
PHP/TK is an native extension for the PHP programming language that implements
language bindings for TCL/TK. It provides an object-oriented interface and
greatly simplifies writing client-side cross-platform GUI applications. 

%prep

%setup -q -n tk-%{version}
%patch0 -p0

%build
%serverbuild

# source tk stuff
. %{_libdir}/tkConfig.sh

%{_usrsrc}/php-devel/buildext tk "tk.c" \
    "${TK_XLIBSW} ${TK_LIB_SPEC} " "-DCOMPILE_DL_TK \
    -I${TK_SRC_DIR} ${TK_XINCLUDES}"

#phpize
#export LIBS="$LIBS -ltk"
#%%configure2_5x \
#    --with-%{modname}=shared,%{_prefix}
#
#%%make
#mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
[ "../package.xml" != "/" ] && rm -f ../package.xml

%files 
%defattr(-,root,root)
%doc tests CREDITS
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}
