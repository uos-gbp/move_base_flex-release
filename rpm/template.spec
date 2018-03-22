Name:           ros-kinetic-mbf-abstract-nav
Version:        0.1.0
Release:        1%{?dist}
Summary:        ROS mbf_abstract_nav package

Group:          Development/Libraries
License:        3-Clause BSD
URL:            http://wiki.ros.org/move_base_flex
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-mbf-abstract-core
Requires:       ros-kinetic-mbf-msgs
Requires:       ros-kinetic-mbf-utility
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-xmlrpcpp
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-mbf-abstract-core
BuildRequires:  ros-kinetic-mbf-msgs
BuildRequires:  ros-kinetic-mbf-utility
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-xmlrpcpp

%description
The mbf_abstract_nav package contains the abstract navigation server
implementation of Move Base Flex (MBF). The abstract navigation server is not
bound to any map representation. It provides the actions for planning,
controlling and recovering. MBF loads all defined plugins at the program start.
Therefor, it loads all plugins which are defined in the lists *planners*,
*controllers* and *recovery_behaviors*. Each list holds a pair of a *name* and a
*type*. The *type* defines which kind of plugin to load. The *name* defines
under which name the plugin should be callable by the actions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Mar 22 2018 Sebastian Pütz <spuetz@uos.de> - 0.1.0-1
- Autogenerated by Bloom

* Wed Mar 21 2018 Sebastian Pütz <spuetz@uos.de> - 0.1.0-0
- Autogenerated by Bloom

