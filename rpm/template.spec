Name:           ros-indigo-mbf-costmap-core
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS mbf_costmap_core package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/move_base_flex/mbf_costmap_core
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mbf-abstract-core
Requires:       ros-indigo-mbf-utility
Requires:       ros-indigo-nav-core
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-mbf-abstract-core
BuildRequires:  ros-indigo-mbf-utility
BuildRequires:  ros-indigo-nav-core
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf

%description
This package provides common interfaces for navigation specific robot actions.
It contains the CostmapPlanner, CostmapController and CostmapRecovery
interfaces. The interfaces have to be implemented by the plugins to make them
available for Move Base Flex using the mbf_costmap_nav navigation
implementation. That implementation inherits the mbf_abstract_nav implementation
and binds the system to a local and a global costmap.

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

