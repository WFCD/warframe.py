warframe.py
===========
.. image:: https://img.shields.io/pypi/v/warframe.py.svg
   :target: https://pypi.python.org/pypi/warframe.py
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/warframe.py.svg
   :target: https://pypi.python.org/pypi/warframe.py
   :alt: PyPI supported Python versions
.. image:: https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release
   :target: https://github.com/semantic-release/semantic-release
   :alt: semantic-release: angular

An asynchronous and typed Python API wrapper for `the Warframestat API <https://hub.warframestat.us>`__ and (later) `the warframe.market API <https://warframe.market/api_docs>`__.

What to expect
--------------

This library is in its early states. The goal is to make it the best and most up-to-date Python Warframe API wrapper.

Quickstart
----------

.. code-block:: python

    
    import asyncio
    import logging

    from warframe.worldstate import WorldstateClient, utils

    # import the models you want to use
    from warframe.worldstate.models import Cetus

    async def main():
        # Note that the default logger is pretty much empty (nothing will be logged)
        # so if you want to make use of the logger, you can use this helper function:
        utils.setup_logging(handler=logging.StreamHandler(), level=logging.DEBUG, root=True)

        async with WorldstateClient() as client:
            # get current cetus data
            cetus = await client.get_cetus()

            # or... get it like this:

            # queries are just another way to get the data to the corresponding objects.
            # this is really just personal preference.
            cetus = await client.query(Cetus)

            print(cetus)


    if __name__ == "__main__":
        loop = asyncio.new_event_loop()
        loop.run_until_complete(main())



Installing
----------

To install the library, use the following command:

.. code-block:: bash

    pip install warframe.py

Supported python versions:

- 3.11
- 3.10
- 3.9
