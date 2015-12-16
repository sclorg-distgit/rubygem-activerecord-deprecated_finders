%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from activerecord-deprecated_finders-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activerecord-deprecated_finders

%global bootstrap 0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.3
Release: 3%{?dist}
Summary: This gem contains deprecated finder APIs extracted from Active Record
Group: Development/Languages
License: MIT
URL: https://github.com/rails/activerecord-deprecated_finders
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
%if 0%{bootstrap} < 1
Requires: %{?scl_prefix}rubygem(activerecord) >= 4.0.0
Requires: %{?scl_prefix}rubygem(activerecord) < 5.0
%endif
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(atomic)
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
BuildRequires: %{?scl_prefix}rubygem(activerecord) >= 4.0.0
BuildRequires: %{?scl_prefix}rubygem(activerecord) < 5.0
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Deprecated finder APIs extracted from Active Record.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

# Remove shebang from non-executable Rakefile
sed -i '1d' Rakefile

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
# Get rid of Bundler
sed -i "1d" test/helper.rb
%{?scl:scl enable %{scl} - << \EOF}
testrb -Ilib test/*_test.rb
%{?scl:EOF}
popd
%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/%{gem_name}.gemspec.erb
%{gem_instdir}/test

%changelog
* Fri Oct 04 2013 Josef Stribny <jstribny@redhat.com> - 1.0.3-4
- Convert to scl

* Thu Aug 08 2013 Josef Stribny <jstribny@redhat.com> - 1.0.3-3
- Enable tests and proper requires again

* Thu Aug 01 2013 Josef Stribny <jstribny@redhat.com> - 1.0.3-2
- Bootsrap required as well because of circular dep with ActiveRecord

* Thu Aug 01 2013 Josef Stribny <jstribny@redhat.com> - 1.0.3-1
- Update to 1.0.3
- Remove shebang from Rakefile

* Wed Jul 31 2013 Josef Stribny <jstribny@redhat.com> - 1.0.2-2
- Add bootstrap to build the package before Rails 4.0

* Thu May 09 2013 Josef Stribny <jstribny@redhat.com> - 1.0.2-1
- Initial package
