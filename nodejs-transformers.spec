%{?nodejs_find_provides_and_requires}
%global enable_tests 0
Name:                nodejs-transformers
Version:             3.1.0
Release:             1
Summary:             String/Data transformations for Node.js
License:             MIT
URL:                 https://github.com/ForbesLindesay/transformers
Source0:             http://registry.npmjs.org/transformers/-/transformers-%{version}.tgz
#git clone git://github.com/ForbesLindesay/transformers.git
#cd transformers
#git archive --prefix="test/" --format=tar tags/3.1.0:test/ \
#    | bzip2 > "$pwd"/tests-3.1.0.tar.bz2
Source1:             tests-%{version}.tar.bz2
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging npm(clone) npm(css) npm(promise) npm(uglify-js)
%if 0%{?enable_tests}
BuildRequires:       mocha npm(expect.js) npm(promise)
%endif
%description
String/Data transformations for use in templating libraries, static site
generators and web frameworks. This gathers the most useful transformations
you can apply to text or data into one library with a consistent API.
Transformations can be pretty much anything but most are either compilers
or templating engines.

%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package
for i in history.md LICENSE README.md; do
    sed -i -e 's/\r$//' "${i}"
done
%nodejs_fixdep css
%nodejs_fixdep promise
%nodejs_fixdep uglify-js
%nodejs_fixdep clone

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/transformers
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/transformers
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc history.md README.md
%license LICENSE
%{nodejs_sitelib}/transformers

%changelog
* Tue Sep 1 2020 wutao <wutao61@huawei.com> - 3.1.0-1
- Package init
