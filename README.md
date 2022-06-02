# Writing3D Projects

Translate Writing3D xml projects into Unity projects. Each scene file is automatically generated.

## Install

The translator uses Unity version 2021.3.0f1. Please ensure the `Unity.exe` file is in`C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe`. You can download the version from [Unity's archives](https://unity3d.com/get-unity/download/archive).

## Usage

`poetry run python w3d_translator.py [OPTIONS] IN_DIR OUT_DIR`

* `IN_DIR`: Input folder containing the xml project(s)
* `OUT_DIR`: Output folder for the translated project(s)

### Options

* `--multiple`: Translate multiple projects, `IN_DIR` the parent folder of the individual projects. Default: `False`
* `--force`: Overwrite `OUT_DIR`. Default: `False`
* `--dev`: Development flag - Unity subprocess is not called. Default: `False`.  

### Linting

```console
poetry run black . -l 79
```

## Folders & Files

* `examples/`: Example .xml files
* `in/`: Input folder with test projects
* `schema/`: XML schema files for writing3D, pulled from the original project
* `unity/`: Unity Yaml file for example scenes.
* `w3d_translator/`: Python module containing the source code

## generateDS

This project uses [generateDS](https://www.davekuhlman.org/generateDS.html) to build each xml file in Python. This intermediary step is done to ease the translation into the Unity yaml specification. The relevant files have already been generated and changed, and should not need to be touched.

Should you need to regenerate the code, generateDS should be [installed](https://www.davekuhlman.org/generateDS.html#how-to-build-and-install-it) on your local machine. It is run with the following arguments:

```console
python generateDS.py -o w3d_translator/generateDS/[classes.py] -s w3d_translator/generateDS/[subclasses.py] --super=[generateDS.classes] --use-getter-setter=none --member-specs=dict --cleanup-name-list="[('[-:.]', '_'), ('Root$', 's'), ('Pos$', '')]" .\schema\caveschema.xsd
```

* `classes.py` contains the API outfile
* `subclasses.py` contains the outfile for the subclasses
* `--super` should point to the API outfile module
  * If this is not given `subclasses.py` will insert ??? and the file must be manually edited.
* `--use-getter-setter=none` disables the generation of get() and set() methods
* `--member-specs=dict` adds a `member_data_items_` property - a dict of each XML child. This is useful for validating and traversing the classes
* `--cleanup-name-list` transforms a name in the XSD file in Python
  * Invalid Python characters are translated to _
  * Any name that ends in `Root` will end in `s`
  * `Pos` at the end of a name is removed

More details on the command line interface are found [here](https://www.davekuhlman.org/generateDS.html#the-command-line-interface-how-to-use-it).
