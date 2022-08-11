# open3d-stubs

Python stub files for type checking and autocomplete for [Open3D](https://github.com/isl-org/Open3D).

### Installation

From the `install` branch:

```
pip install git+https://github.com/brentyi/open3d-stubs.git@install
```

Installation can also be done directly from the development branch, but `pip`
will unnecessarily clone submodules.

### Development

The package is in a usable state, but still a work-in-progress! See
[mypy errors](./mypy_errors) for automatically detected issues.

1. Clone:

```
git clone --recurse-submodules https://github.com/brentyi/open3d-stubs.git
```

2. Install dependencies:

```
cd open3d-stubs
pip install -r requirements.txt
cd pybind11-stubgen
pip install -e .
cd ../Open3D
# Follow directions for building Open3D from source: http://www.open3d.org/docs/release/compilation.html
...
```

4. Run stub generation:

```
python generate_stubs.py
```

### Misc

Similar project: https://github.com/againxx/open3d-stubs
