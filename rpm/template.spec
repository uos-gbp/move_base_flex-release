Name:           ros-indigo-mbf-simple-nav
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS mbf_simple_nav package

Group:          Development/Libraries
License:        3-Clause BSD
URL:            http://wiki.ros.org/move_base_flex
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mbf-abstract-core
Requires:       ros-indigo-mbf-abstract-nav
Requires:       ros-indigo-mbf-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-ros
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-mbf-abstract-core
BuildRequires:  ros-indigo-mbf-abstract-nav
BuildRequires:  ros-indigo-mbf-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-ros

%description
The mbf_simple_nav package contains a simple navigation server implementation of
Move Base Flex (MBF). The simple navigation server is bound to no map
representation. It provides actions for planning, controlling and recovering.
MBF loads all defined plugins which are defined in the lists *planners*,
*controllers* and *recovery_behaviors*. Each list holds a pair of a *name* and a
*type*. The *type* defines which kind of plugin to load. The *name* defines
under which name the plugin should be callable by the actions. It tries to load
the defined plugins which implements the defined interfaces in
mbf_abstract_core.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Oct 03 2018 Sebastian Pütz <spuetz@uos.de> - 0.2.1-0
- Autogenerated by Bloom

