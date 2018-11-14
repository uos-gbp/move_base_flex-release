Name:           ros-indigo-mbf-abstract-core
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS mbf_abstract_core package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/mbf_abstract_core
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-std-msgs

%description
This package provides common interfaces for navigation specific robot actions.
It contains the AbstractPlanner, AbstractController and AbstractRecovery plugin
interfaces. This interfaces have to be implemented by the plugins to make the
plugin available for Move Base Flex. The abstract classes provides a meaningful
interface enabling the planners, controllers and recovery behaviors to return
information, e.g. why something went wrong. Derivided interfaces can, for
example, provide methods to initialize the planner, controller or recovery with
map representations like costmap_2d, grid_map or other representations.

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
* Wed Nov 14 2018 Sebastian Pütz <spuetz@uos.de> - 0.2.3-0
- Autogenerated by Bloom

* Wed Oct 10 2018 Sebastian Pütz <spuetz@uos.de> - 0.2.2-0
- Autogenerated by Bloom

* Wed Oct 03 2018 Sebastian Pütz <spuetz@uos.de> - 0.2.1-0
- Autogenerated by Bloom

