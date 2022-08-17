import pathlib
import shutil
import subprocess

assert not pathlib.Path("./open3d").exists()
stubdir = pathlib.Path("./open3d-stubs/open3d-stubs/")

# Remove old stubs.
if stubdir.exists():
    assert stubdir.is_dir()
    print("Deleting ./open3d-stubs/open3d-stubs/!")
    shutil.rmtree(stubdir)

# Generate rough stubs.
print("Generating (rough) stubs!")
for module in (
    "open3d.ml",
    "open3d.cpu.pybind",
    "open3d.cpu.pybind.visualization.gui",
    "open3d.cpu.pybind.visualization.rendering",
):
    subprocess.call(
        args=[
            "stubgen",
            "-o",
            "./open3d-stubs",
            "-p",
            module,
        ],
    )

pathlib.Path("open3d-stubs/open3d").rename(stubdir)

# Move stubs from open3d.cpu.pybind.* to open3d.*.
cpu_pybind_dir = stubdir / "cpu/pybind"
for source_path in cpu_pybind_dir.glob("**/*.pyi"):
    target_path = stubdir / source_path.relative_to(cpu_pybind_dir)
    target_path.parent.mkdir(exist_ok=True)

    print(f"Moving {source_path} to {target_path}")
    if target_path.exists():
        # Merge stub files.
        target_path.write_text(target_path.read_text() + "\n" + source_path.read_text())
        source_path.unlink()
    else:
        source_path.rename(target_path)

# Delete old CPU directory.
assert (
    len(list((stubdir / "cpu").glob("**/*.pyi")))
    == len(list((stubdir / "cpu").glob("*.pyi")))
    == 0
)
shutil.rmtree(stubdir / "cpu")

# camera.pyi -> camera/__init__.pyi
for source_path in stubdir.glob("**/*.pyi"):
    if source_path.stem != "__init__":
        new_dir = source_path.parent / source_path.stem
        if not new_dir.exists():
            new_dir.mkdir()
            source_path.rename(new_dir / "__init__.pyi")
        else:
            target_path = new_dir /  "__init__.pyi"
            target_path.write_text(target_path.read_text() + "\n" + source_path.read_text())

# Fix some names.
for source_path in stubdir.glob("**/*.pyi"):
    source = source_path.read_text()

    source = source.replace("open3d.cpu.pybind", "open3d")
    source = source.replace("numpy.", "np.")
    source = source.replace("np.ndarray", "npt.NDArray")
    source = source.replace("import numpy\n", "")
    source = source.replace(
        "from typing import ",
        "import numpy as np\nimport numpy.typing as npt\nfrom typing_extensions import Annotated\nfrom typing import Set, ",
    )

    # Fix array types.
    while "np.float64[" in source:
        begin, _, mid = source.partition("np.float64[")
        shape, _, end = mid.partition("]")

        source = f"{begin}Annotated[np.float64, '{shape}']{end}"
    while "np.float32[" in source:
        begin, _, mid = source.partition("np.float32[")
        shape, _, end = mid.partition("]")

        source = f"{begin}Annotated[np.int32, '{shape}']{end}"
    while "np.int32[" in source:
        begin, _, mid = source.partition("np.int32[")
        shape, _, end = mid.partition("]")

        source = f"{begin}Annotated[np.int32, '{shape}']{end}"

    if "open3d-stubs/pipelines/registration/__init__.pyi" in source_path.as_posix():
        source = source.replace(
            "float from 0 to 1\n", "Annotated[float, 'from 0 to 1']\n"
        )
    if "open3d-stubs/visualization/__init__.pyi" in source_path.as_posix():
        source = source.replace(
            "    @overload\n    def show_geometry(name, True) -> Any: ...\n", ""
        )
        source = source.replace(
            " = ..., lookat, up, front, zoom)",
            " = ..., lookat = ..., up = ..., front = ..., zoom = ...)",
        )
        source = source.replace(
            "from typing", "import open3d.visualization.gui\nimport open3d.visualization.rendering\nfrom typing"
        )
        source = source.replace(": string\n", ": str\n")
        source = source.replace(": gui.", ": open3d.visualization.gui.")
        source = source.replace("-> gui.", "-> open3d.visualization.gui.")
        source = source.replace(": rendering.", ": open3d.visualization.rendering.")
        source = source.replace("-> rendering.", "-> open3d.visualization.rendering.")
    if "open3d-stubs/camera/__init__.pyi" in source_path.as_posix():
        source = source.replace(
            "3x3 numpy array", "npt.NDArray[Annotated[np.float64, '3,3']]"
        )
        source = source.replace(
            "4x4 numpy array", "npt.NDArray[Annotated[np.float64, '4,4']]"
        )
    if "open3d-stubs/geometry/__init__.pyi" in source_path.as_posix():
        source = source.replace("List of Sets", "List[Set[int]]")
    if "open3d-stubs/core/__init__.pyi" in source_path.as_posix():
        source = source.replace(": handle", ": Any")
        source = source.replace("-> capsule:", "-> Any:")
        source = source.replace(": bool", ": __builtins__.bool")
        source = source.replace("-> bool", "-> __builtins__.bool")

    if source_path.as_posix().endswith("__init__.pyi"):
        local_imports = []
        for local_path in source_path.parent.iterdir():
            print(local_path, local_path.suffix)
            if local_path.name.startswith("_"):
                continue
            if local_path.is_dir() and (local_path / "__init__.pyi").exists():
                local_imports.append(local_path.stem)

        source = "from . import " + ",".join(local_imports) + "\n" + source

        for line in source.split("\n"):
            if not line.startswith(" ") and ":" in line:
                name, _, _ = line.partition(":")
                if "(" not in name and " " not in name:
                    local_imports.append(name)
                    continue

            if line.startswith("class "):
                line = line[len("class "):]
                if "(" in line:
                    local_imports.append(line.partition("(")[0])
                else:
                    assert line.endswith(":")
                    local_imports.append(line[:-1])
                continue

            if line.startswith("def "):
                local_imports.append(line[len("def "):].partition("(")[0])
                continue

        source = (
            source
            + "\n__all__ = ["
            + ",".join(map(lambda x: f'"{x}"', local_imports))
            + "]"
        )

    source = source.replace(
        "    @overload\n    def __init__(self, arg0: buffer) -> None: ...\n", ""
    )

    lines = []
    for line in source.split("\n"):
        if line.strip().startswith("def __init__") and line.endswith("-> Any: ..."):
            line = line.replace("-> Any:", "-> None:")

        # Remove methods with no arguments; these are errors.
        if line.startswith("    def ") and line.endswith("() -> Any: ...") and lines[-1].strip() == "@overload":
            lines.pop(-1)
            continue
        lines.append(line)

    source = "\n".join(lines)

    source_path.write_text(source)

# Format with isort, then black.
subprocess.call(args=["isort", stubdir.parent.as_posix()])
subprocess.call(args=["black", stubdir.parent.as_posix()])
subprocess.call(args=["mypy", stubdir.parent.as_posix()], stdout=open("./mypy_errors", "w"))
subprocess.call(args=["mypy", stubdir.parent.as_posix()], stdout=open("./mypy_errors", "w"))

for source_path in cpu_pybind_dir.glob("**/*.pyi"):
    subprocess.call(args=["autoflake", "--in-place", source_path.as_posix()], stdout=open("./mypy_errors", "w"))
print()
print("Generated: ", stubdir)
