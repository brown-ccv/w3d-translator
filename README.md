# Writing3D Projects

Translate Writing3D xml projects into Unity projects. Each scene file is automatically generated.

## Install

```console
poetry install
```

### generateDS

This project uses [generateDS](https://www.davekuhlman.org/generateDS.html) to build each xml file in Python. This intermediary step is done to ease the translation into the Unity yaml specification. `generateDS` will be installed by poetry automatically. Then, from the root folder, run:

```console
poetry run python .\.venv\Scripts\generateDS.py -o w3d_translator/generateDS/classes.py -s w3d_translator/generateDS/subclasses.py --super=generateDS.classes --use-getter-setter=none --member-specs=dict --cleanup-name-list="[('[-:.]', '_'), ('Root$', 's'), ('Pos$', '')]" .\schema\caveschema.xsd
```

Poetry may not install the packages into the `.venv` subfolder depending on your local configuration. Replace `.\.venv\Scripts\generateDS.py` with the path to the local install if you run into issues.

* `classes.py`: The API outfile
* `subclasses.py`: The outfile for the subclass module
* `--super`: The import path of the API outfile in the subclass module
  * If this is not given `subclasses.py` will insert `???` and the file must be manually edited.
* `--use-getter-setter=none` disables the generation of get() and set() methods
* `--member-specs=dict` adds a `member_data_items_` property - a dict of each XML child. This is useful for validating and traversing the classes.
* `--cleanup-name-list` transforms a name in the XSD file in Python
  * Invalid Python characters are translated to `_`
  * Any name that ends in `Root` will end in `s`
  * `Pos` at the end of a name is removed

More details on the command line interface are found [here](https://www.davekuhlman.org/generateDS.html#the-command-line-interface-how-to-use-it).

### Unity

The translator uses Unity version 2021.3.0f1. Please ensure the `Unity.exe` file is in`C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe`. You can download the version from [Unity's archives](https://unity3d.com/get-unity/download/archive).

### Linting

```console
poetry run black . -l 79
```

## Usage

`poetry run python w3d_translator.py [OPTIONS] IN_DIR OUT_DIR`

* `IN_DIR`: Input folder containing the xml project(s)
* `OUT_DIR`: Output folder for the translated project(s)

### Options

* `--multiple`: Translate multiple projects, `IN_DIR` is the parent folder of the individual projects. Default: `False`
* `--force`: Overwrite `OUT_DIR`. Default: `False`
* `--dev`: Development flag - Unity subprocess is not called. Default: `False`.  

## Folders & Files

* `examples/`: Example .xml files
* `in/`: Input folder with test projects
* `schema/`: XML schema files for writing3D, pulled from the original project
* `unity/`: Unity Yaml file for example scenes.
* `w3d_translator/`: Python module containing the source code

## Example Projects

Multiple example projects are included in this repo in the `examples` folder, any changes to the original xml (as found in the old `CaveWriting` project) are noted in comments. More detail is given below but here's a tldr overview:

* `cweditor/minimum.xml` contains the minimum structure of a valid project
* `cweditor/maximum.xml` contains at least one of every valid tag
* The `cw2_samples` folder contains projects highlighting a specific object type
* The `samples` folder also generally includes projects highlighting a specific object type, but includes Events, Timelines, ParticleActions, etc.

### cweditor

Example projects from the cweditor java program. cweditor enabled CaveWriting project creation with a GUI.

**minimum.xml** contains the base xml necessary for each project. It includes the `PlacementRoot` (`Center`, `FrontWall`, `LeftWall`, `RightWall`, `FloorWall`) and the `Global` settings (`CameraPos`, `CaveCameraPos`, `Background`, `WandNavigation`). Each tag uses its default value.

**everything.xml** contains at least one of every possible Writing3D tag. The image (`w.png`) and sound (`bad.mp3`) used in the project are located in the `testMedia` subfolder. The default value seems to be used wherever possible, although I have not fully checked to be 100% sure.

### cw2_samples

Example projects broken down by object type. Many of the projects contain multiple objects but each is used to highlight a different object type and how they can be used. I've listed the projects in order below, from smallest to largest.

**play.xml** and **sound.xml** are the sadisplays a single text object. It plays a sound when clicked.

 contains a sound within the `SoundRoot` branch.

**I think play and sound are the exact same project**

**sample_random.xml**
**sample_fountain.xml**
**sample_light.xml**
**sample_move.xml**
**sample_image.xml**
**sample_model.xml**
**sample.xml**
**sound_positional.xml**

### samples

Space
