# Build the business_lookup release package
# rpmbuild -ba business_lookup.spec --define 'version '$(date +%Y%m%d) --define 'commit master' 
# Commit will be used as the release
%{!?appdir: %define appdir /opt/%{name}}
%{!?version: %define version 0}
%{!?target_os: %define target_os el6}
%{!?release: %define release 1.%{target_os}}
%{!?git_repo: %define git_repo https://github.2ndsiteinc.com/dev/%{name}}
%{!?commit: %define commit release/%{version}}
%{!?indexhost: %define indexhost INVALID}

Name:           business_lookup
Version:        %{version}
Release:        %{release}
Summary:        Looks up businesses based on location
# Some of the extensions are compiled, and thus this can't be noarch
BuildArch:      x86_64
Group:          Application/Internet
License:        Commercial
URL:            https://github.2ndsiteinc.com/dev/%{name}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# RPM Guess it needs the interpreter that it is supplying, but within the buildroot
AutoReqProv:    no

BuildRequires: gcc git python27 python27-virtualenv wget
Requires: python27-libs python27

%description
Looks up businesses based on location

%build
rm -rf %{name}
pushd $RPM_SOURCE_DIR
git clone %{git_repo} %{name}
# Go into the business_lookup dir, checkout the right version and make a wheel
pushd %{name}
git checkout %{commit}
echo "%{version}" > business_lookup/VERSION
virtualenv-2.7 env
env/bin/pip install wheel
env/bin/python setup.py bdist_wheel

%install
# Start clean
rm -rf $RPM_BUILD_ROOT
virtualenv-2.7 $RPM_BUILD_ROOT/%{appdir}

$RPM_BUILD_ROOT/%{appdir}/bin/pip install -i https://pi.builds.2ndsiteinc.com/dev/releases $RPM_SOURCE_DIR/%{name}/dist/*.whl

virtualenv-2.7 --relocatable $RPM_BUILD_ROOT/%{appdir}
install -d $RPM_BUILD_ROOT/%{appdir}/etc
cp $RPM_SOURCE_DIR/%{name}/gunicorn.conf.py $RPM_BUILD_ROOT/%{appdir}/etc

mkdir -p $RPM_BUILD_ROOT/%{migdir}
cp -r $RPM_SOURCE_DIR/%{name}/migrations/* $RPM_BUILD_ROOT/%{migdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{appdir}
