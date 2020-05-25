%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-mbf-costmap-core
Version:        0.3.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mbf_costmap_core package

License:        BSD-3
URL:            http://wiki.ros.org/move_base_flex/mbf_costmap_core
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-costmap-2d
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-mbf-abstract-core
Requires:       ros-noetic-mbf-utility
Requires:       ros-noetic-nav-core
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-costmap-2d
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-mbf-abstract-core
BuildRequires:  ros-noetic-mbf-utility
BuildRequires:  ros-noetic-nav-core
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package provides common interfaces for navigation specific robot actions.
It contains the CostmapPlanner, CostmapController and CostmapRecovery
interfaces. The interfaces have to be implemented by the plugins to make them
available for Move Base Flex using the mbf_costmap_nav navigation
implementation. That implementation inherits the mbf_abstract_nav implementation
and binds the system to a local and a global costmap.

%prep
%autosetup

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
    -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Mon May 25 2020 Sebastian Pütz <spuetz@uos.de> - 0.3.2-1
- Autogenerated by Bloom

