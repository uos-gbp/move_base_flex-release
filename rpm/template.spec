%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-move-base-flex
Version:        0.3.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS move_base_flex package

License:        BSD-3
URL:            http://wiki.ros.org/move_base_flex
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-mbf-abstract-core
Requires:       ros-noetic-mbf-abstract-nav
Requires:       ros-noetic-mbf-costmap-core
Requires:       ros-noetic-mbf-costmap-nav
Requires:       ros-noetic-mbf-msgs
Requires:       ros-noetic-mbf-simple-nav
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Move Base Flex (MBF) is a backwards-compatible replacement for move_base. MBF
can use existing plugins for move_base, and provides an enhanced version of the
planner, controller and recovery plugin ROS interfaces. It exposes action
servers for planning, controlling and recovering, providing detailed information
of the current state and the plugin’s feedback. An external executive logic can
use MBF and its actions to perform smart and flexible navigation strategies.
Furthermore, MBF enables the use of other map representations, e.g. meshes or
grid_map This package is a meta package and refers to the Move Base Flex stack
packages.The abstract core of MBF – without any binding to a map representation
– is represented by the mbf_abstract_nav and the mbf_abstract_core. For
navigation on costmaps see mbf_costmap_nav and mbf_costmap_core.

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

