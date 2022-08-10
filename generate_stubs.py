import pathlib
import shutil
import subprocess

stubdir = pathlib.Path("./open3d-stubs")

# Remove old stubs.
if stubdir.exists():
    assert stubdir.is_dir()
    print("Deleting ./open3d-stubs/!")
    shutil.rmtree(stubdir)

# Generate rough stubs.
print("Generating (rough) stubs!")
subprocess.call(
    args=[
        "pybind11-stubgen",
        "-o",
        ".",
        "open3d",
        "--ignore-invalid",
        "all",
        "--skip-signature-downgrade",
    ],
)


# Move stubs from open3d.cpu.pybind.* to open3d.*.
cpu_pybind_dir = stubdir / "cpu/pybind"
for source_path in cpu_pybind_dir.glob("**/*.pyi"):
    target_path = stubdir / source_path.relative_to(cpu_pybind_dir)
    target_path.parent.mkdir(exist_ok=True)

    print(f"Moving {source_path} to {target_path}")
    source_path.rename(target_path)

# Delete old CPU directory, which should only have one stub file in it: cpu/__init__.pyi.
assert (
    len(list((stubdir / "cpu").glob("**/*.pyi")))
    == len(list((stubdir / "cpu").glob("*.pyi")))
    == 1
)
shutil.rmtree(stubdir / "cpu")

# Enforce directory structure.
stubdir = stubdir.rename("./open3d-stubs-temp/")
pathlib.Path("./open3d-stubs").mkdir()
stubdir = stubdir.rename("./open3d-stubs/open3d-stubs/")
pathlib.Path(stubdir / "setup.py").rename(stubdir.parent / "setup.py")

# Fix some names.
for source_path in stubdir.glob("**/*.pyi"):
    source_path = source_path.absolute()
    print("Replacing in", source_path)
    source = source_path.read_text()

    # Generalize CPU / CUDA.
    source = source.replace(".cpu.pybind.", ".")

    # Try to fix missing names.
    source = source.replace("::", ".")

    # For whatever reason, typing_extensions is not always imported.
    source = source.replace(
        "import typing\n", "import typing\nimport typing_extensions\n"
    )

    # Use np as alias for numpy.
    source = source.replace("import numpy.typing\n", "import numpy.typing as npt\n")
    source = source.replace("numpy.typing.", "npt.")

    source = source.replace("import numpy\n", "import numpy as np\n")
    source = source.replace("numpy.", "np.")

    # Remove overloads from raw buffers; I don't think it's possible to pass a buffer directly in
    # via Python?
    source = source.replace(
        "    @typing.overload\n    def __init__(self, arg0: buffer) -> None: ...\n",
        "\n",
    )

    # Local imports. For whatever reason, these are sometimes missing.
    if "__all__" in source:
        names = source.partition("\n__all__ = [\n")[2].partition("\n]\n")[0].strip()
        for name in names.split("\n"):
            name = name.strip()
            if len(name) == 0:
                continue
            if name.startswith('"'):
                name = name[1:]
            if name.endswith(","):
                name = name[:-1]
            if name.endswith('"'):
                name = name[:-1]

            if (source_path.parent / name / "__init__.pyi").exists():
                source = source.replace(
                    "import typing\n", f"import typing\nfrom . import {name}\n"
                )

    # File-specific tweaks.
    if "open3d-stubs/core/__init__.pyi" in source_path.as_posix():
        # Fix overloaded `bool` name.
        assert "bool: open3d.core.Dtype" in source
        source = source.replace("-> bool", "-> __builtins__.bool")
        source = source.replace(": bool", ": __builtins__.bool")

        # Fix issue with arguments with default coming before argument without.
        source = source.replace("] = None, stop: float,", "], stop: float,")
        source = source.replace("] = None, stop: int,", "], stop: int,")

        # Make missing capsule type.
        source = source.replace(
            "class Tensor():",
            'DLPackCapsule = typing.NewType("DLPackCapsule", object)\nclass Tensor():',
        )
        source = source.replace(": capsule", ": DLPackCapsule")
        source = source.replace("-> capsule", "-> DLPackCapsule")

        # Make missing DtypeCode type.
        source = source.replace(
            "    Bool: open3d.core.Dtype",
            '    DtypeCode = typing.NewType("DtypeCode", object)\n    Bool: open3d.core.Dtype',
        )
        source = source.replace(": capsule", ": DLPackCapsule")
        source = source.replace("-> capsule", "-> DLPackCapsule")

        # Not really sure what this is, but the name is undefined.
        source = source.replace("arg1: handle", "arg1: typing.Any")

    elif "open3d-stubs/visualization/__init__.pyi" in source_path.as_posix():
        for option in ("MeshColorOption", "MeshShadeOption", "PointColorOption"):
            source = source.replace(f"RenderOption.{option}", option)
        source = source.replace(
            "VisualizerWithVertexSelection.PickedPoint", "PickedPoint"
        )
        source = source.replace("(gui.", "(open3d.visualization.gui.")
        source = source.replace(": gui.", ": open3d.visualization.gui.")
        source = source.replace("-> gui.", "-> open3d.visualization.gui.")
        source = source.replace("(rendering.", "(open3d.visualization.rendering.")
        source = source.replace(": rendering.", ": open3d.visualization.rendering.")
        source = source.replace("-> rendering.", "-> open3d.visualization.rendering.")

    elif "open3d-stubs/visualization/gui/__init__.pyi" in source_path.as_posix():
        source = source.replace("gui.PyWindow", "gui.Window")

    elif "open3d-stubs/visualization/rendering/__init__.pyi" in source_path.as_posix():
        # Fix REHandle name error, since it's not exposed via pybind.
        source = source.replace("<(open3d.visualization.rendering.EntityType)10>", "")
        source = source.replace(
            "class Renderer():",
            'REHandle = typing.NewType("REHandle", object)\nclass Renderer():',
        )
        source = source.replace(
            "open3d.visualization.rendering.REHandle<",
            "REHandle",
        )
        source = source.replace(
            "open3d.visualization.rendering.REHandle",
            "REHandle",
        )

    elif "open3d-stubs/pipelines/odometry/__init__.pyi" in source_path.as_posix():
        source = source.replace(
            " = IntVector[20, 10, 5]",
            " = open3d.utility.IntVector([20, 10, 5])",
        )

    elif "t/geometry/__init__.pyi" in source_path.as_posix():
        # Add missing import open3d.visualization import, fix namespace.
        source = source.replace(
            "import typing", "import typing\nimport open3d.visualization"
        )
        source = source.replace(
            "open3d.visualization.rendering.Material",
            "open3d.visualization.Material",
        )

    elif "t/pipelines/slam/__init__.pyi" in source_path.as_posix():
        source = source.replace(
            "import typing", "import typing\nimport open3d.t.geometry"
        )

    elif "t/pipelines/slac/__init__.pyi" in source_path.as_posix():
        source = source.replace(
            "import typing", "import typing\nimport open3d.t.geometry"
        )
    elif "t/pipelines/registration/__init__.pyi" in source_path.as_posix():
        source = source.replace(
            "class TransformationEstimationForColoredICP(TransformationEstimation):",
            'RobustKernel = typing.NewType("RobustKernel", object)\n'
            "class TransformationEstimationForColoredICP(TransformationEstimation):",
        )

    source = source.replace(" = CPU:0", ' = open3d.core.Device("CPU:0")')
    source = source.replace(" = Int64", " = open3d.core.Dtype.Int64")
    source = source.replace(" = Float32", " = open3d.core.Dtype.Float32")
    source = source.replace(" = inf", ' = float("inf")')

    source_path.write_text(source)

# Format with isort, then black.
subprocess.call(args=["isort", stubdir.parent.as_posix()])
subprocess.call(args=["black", stubdir.parent.as_posix()])
subprocess.call(
    args=["mypy", stubdir.parent.as_posix()], stdout=open("./mypy_errors", "w")
)
