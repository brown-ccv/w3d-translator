# Writing3D Projects

Translate Writing3D xml projects into Unity projects. Each scene file is automatically generated.

## Install

The translator uses Unity version 2021.3.0f1. Please ensure the `Unity.exe` file is in`C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe`. You can download the version from [Unity's archives](https://unity3d.com/get-unity/download/archive).

## Usage

`w3d_translator.py [OPTIONS] IN_DIR OUT_DIR`

* `IN_DIR`: Input folder containing the xml project(s)
* `OUT_DIR`: Output folder for the translated project(s)

### Options

* `--multiple`: Translate multiple projects, `IN_DIR` the parent folder of the individual projects. Default: `False`
* `--force`: Overwrite `OUT_DIR`. Default: `False`
* `--dev`: Developmen flag - Unity subprocess is not called. Default: `False`.  

## Folders & Files

* `in`: Input folder for translating multiple projects at the same time
* `out`: Output folder (Should be in .gitignore)
* `EmptyScene.unity`: Unity Yaml file for an entirely empty scene.

<!-- TODO: Add generateDS instructions to README -->

## Development

Linting

```console
poetry run black . -l 79
```
