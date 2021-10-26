%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-mbf-costmap-nav
Version:        0.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mbf_costmap_nav package

License:        BSD-3
URL:            http://wiki.ros.org/move_base_flex
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-actionlib
Requires:       ros-noetic-actionlib-msgs
Requires:       ros-noetic-costmap-2d
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-mbf-abstract-nav
Requires:       ros-noetic-mbf-costmap-core
Requires:       ros-noetic-mbf-msgs
Requires:       ros-noetic-mbf-utility
Requires:       ros-noetic-move-base
Requires:       ros-noetic-move-base-msgs
Requires:       ros-noetic-nav-core
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-actionlib-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-costmap-2d
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-mbf-abstract-nav
BuildRequires:  ros-noetic-mbf-costmap-core
BuildRequires:  ros-noetic-mbf-msgs
BuildRequires:  ros-noetic-mbf-utility
BuildRequires:  ros-noetic-nav-core
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The mbf_costmap_nav package contains the costmap navigation server
implementation of Move Base Flex (MBF). The costmap navigation server is bound
to the costmap_2d representation. It provides the Actions for planning,
controlling and recovering. At the time of start MBF loads all defined plugins.
Therefor, it loads all plugins which are defined in the lists *planners*,
*controllers* and *recovery_behaviors*. Each list holds a pair of a *name* and a
*type*. The *type* defines which kind of plugin to load. The *name* defines
under which name the plugin should be callable by the actions. Additionally the
mbf_costmap_nav package comes with a wrapper for the old navigation stack and
the plugins which inherits from the nav_core base classes. Preferably it tries
to load plugins for the new API. However, plugins could even support both
move_base and move_base_flex by inheriting both base class interfaces located in
the nav_core package and in the mbf_costmap_core package.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Oct 26 2021 Sebastian Pütz <spuetz@uos.de> - 0.4.0-1
- Autogenerated by Bloom

* Wed Dec 02 2020 Sebastian Pütz <spuetz@uos.de> - 0.3.4-1
- Autogenerated by Bloom

* Wed Nov 11 2020 Sebastian Pütz <spuetz@uos.de> - 0.3.3-1
- Autogenerated by Bloom

* Mon May 25 2020 Sebastian Pütz <spuetz@uos.de> - 0.3.2-1
- Autogenerated by Bloom

