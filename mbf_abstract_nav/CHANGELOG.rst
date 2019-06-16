^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package mbf_abstract_nav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.2.3 (2018-11-14)
------------------
* Do not publish path from MBF
* Single publisher for controller execution objects
* Ignore max_retries if value is negative and patience if 0
* Avoid annoying INFO log msg on recovery

0.2.2 (2018-10-10)
------------------
* Add outcome and message to the action's feedback in ExePath and MoveBase

0.2.1 (2018-10-03)
------------------
* Fix memory leak
* Fix uninitialized value for cost
* Make MBF melodic and indigo compatible
* Fix GoalHandle references bug in callbacks

0.2.0 (2018-09-11)
------------------
* Update copyright and 3-clause-BSD license
* Concurrency for planners, controllers and recovery behaviors
* New class structure, allowing multiple executoin instances
* Fixes minor bugs

0.1.0 (2018-03-22)
------------------
* First release of move_base_flex for kinetic and lunar
