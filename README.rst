Toolium Examples
================

Set of examples to learn how to use `Toolium <https://github.com/Telefonica/toolium>`_ to test web, Android or iOS
applications, in different scenarios.

Getting Started
---------------

The requirements to install Toolium are `Python 2.7 or 3.3+ <http://www.python.org>`_ and
`pip <https://pypi.python.org/pypi/pip>`_. If you use Python 2.7.9+, you don't need to install pip separately.

Clone `toolium-automation <https://github.com/KorolevskyMax/toolium-automation>`_ repository and install requirements. It's
highly recommendable to use a virtualenv.

.. code:: console

    $ git clone git@github.com:KorolevskyMax/toolium-automation.git
    $ cd toolium-automation
    $ pip install -r requirements.txt

Running Tests
-------------

Each folder contains a sample project to test web, Android or iOS applications using behave to execute
them.

Running web tests
~~~~~~~~~~~~~~~~~

By default, web tests are configured to run in chrome locally, so chrome must be installed in your machine and the
chrome driver must be downloaded and configured:

- Download chromedriver
- Configure driver path in *[Driver]* section in `web_behave/conf/properties.cfg` file ::

    [Driver]
    chrome_driver_path: C:\Drivers\chromedriver.exe

**/web**

To run web tests with nose:

**/web_behave**

To run behave web tests:

.. code:: console

    $ behave web_behave


Running mobile tests
~~~~~~~~~~~~~~~~~~~

By default, mobile tests are configured to run against a local Appium server, so
`Appium <http://appium.io/slate/en/master/?ruby#setting-up-appium>`_ must be installed, configured and started before
executing tests.

**/android**

Android tests need an Android Emulator or a plugged Android device.

To run Android tests with nose:

**/android_behave**

To run behave Android tests:

.. code:: console

    $ behave android_behave

**/ios_behave**

To run behave iOS tests:

.. code:: console

    $ behave ios_behave

**/web_behave**

The same `/web_behave` tests already run in a browser could also be executed in an Android or iOS
device using different configuration files per environment.

To run behave web tests in an Android device:

.. code:: console

    $ behave web_behave/features/login.feature -D Config_environment=android

To run behave web tests in an iOS device:

.. code:: console

    $ behave web_behave/features/login.feature -D Config_environment=ios
