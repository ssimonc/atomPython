from setuptools import setup

setup(name='atomPython',
      version='1.0',
      install_requires=['numpy', 'pandas', 'matplotlib'],  # And any other dependencies needed
      packages = ["atomPython"]
      package_data={  # we need only the files below:
        "instapy": [
            "atom.py",
             "binary_heap.py",
             "data_processing.py",
              "testatom.py"
        ]
    }
)
