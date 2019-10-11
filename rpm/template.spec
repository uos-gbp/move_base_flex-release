Name:           ros-melodic-mbf-msgs
Version:        0.2.5
Release:        1%{?dist}
Summary:        ROS mbf_msgs package

Group:          Development/Libraries
License:        3-Clause BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib-msgs
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-actionlib-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-genmsg
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-message-runtime
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-std-msgs

%description
The move_base_flex messages package providing the action definition files for
the action GetPath, ExePath, Recovery and MoveBase. The action servers providing
these action are implemented in mbf_abstract_nav.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Oct 11 2019 Jorge Santos <santos@magazino.eu> - 0.2.5-1
- Autogenerated by Bloom

* Sun Jun 16 2019 Jorge Santos <santos@magazino.eu> - 0.2.4-1
- Autogenerated by Bloom

* Wed Nov 14 2018 Jorge Santos <santos@magazino.eu> - 0.2.3-0
- Autogenerated by Bloom

* Wed Oct 10 2018 Jorge Santos <santos@magazino.eu> - 0.2.2-0
- Autogenerated by Bloom

* Wed Oct 03 2018 Jorge Santos <santos@magazino.eu> - 0.2.1-0
- Autogenerated by Bloom

