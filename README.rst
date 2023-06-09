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

An asynchronous Python API wrapper for `the Warframestat API <https://hub.warframestat.us>`__ and (later) `the warframe.market API <https://warframe.market/api_docs>`__.

What to expect
--------------

This library is in its early states. The goal is to make it the best and most up-to-date Python Warframe API wrapper.

Quickstart
----------

.. code-block:: python

    import asyncio

    from warframe.worldstate import Language, WorldstateClient


    async def main():
        async with WorldstateClient() as client:
            cetus = await client.get_cetus(language=Language.English)  # english is default
            print(cetus.short_string)


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
