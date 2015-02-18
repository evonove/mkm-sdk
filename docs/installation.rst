============
Installation
============

From the command line::

    pip install mkmsdk

For the SDK to work properly you need to create four environment variables holding the tokens necessary to create the
authorization to make requests. You can find them in your Magic Kard Market account page under the apps section.

* MKM_APP_TOKEN
* MKM_APP_SECRET
* MKM_ACCESS_TOKEN
* MKM_ACCESS_TOKEN_SECRET


Linux & Mac OS X
~~~~~~~~~~~~~~~~

From the command line::

    export MKM_APP_TOKEN=Xv59wJ6XwyaQFOhI

    export MKM_APP_SECRET=fTvgiZGgly6OHYDExKxrFhwTwTsdJsly

    export MKM_ACCESS_TOKEN=63Q0MJKgNe9LhF57bGH2li85HycaGvtI

    export MKM_ACCESS_TOKEN_SECRET=uq8GN4Yn5pZABrsZ7PZKHFYTguquGUbC

This won't set them permanently but only until you close the shell.


Windows
~~~~~~~

From the command prompt::

    setx MKM_APP_TOKEN "Xv59wJ6XwyaQFOhI"

    setx MKM_APP_SECRET "fTvgiZGgly6OHYDExKxrFhwTwTsdJsly"

    setx MKM_ACCESS_TOKEN "63Q0MJKgNe9LhF57bGH2li85HycaGvtI"

    setx MKM_ACCESS_TOKEN_SECRET "uq8GN4Yn5pZABrsZ7PZKHFYTguquGUbC"

You need to restart the command prompt for the variables to work.
