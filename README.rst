
Gauss Algorithmic Hash Module
=============================


Installation
------------

.. code-block:: sh

    pip install git...


Python usage
------------

.. code-block:: python

    from gauss_hash import GuassHashSha256
    gh = GuassHashSha256(salt='salt')
    print(gh.get_hash('text'))


Commandline usage
-----------------

.. code-block:: sh

    echo 'Krystof Harant z Polzic a Bezdruzic' | gauss-hash --salt 'my_best_salt' --mode dummy
    70196dd57853b2c397e3d35ac4943c4b09002a0b9b835b5f43ceadbfdb30b51e


