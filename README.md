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
* The `sample.xml`, `sample_image.xml`, `sample_light.xml`, and `sample_model.xml` files (`cw2_samples`) showcase the basic file types.
* The `samples/particles` folder contains 2 projects highlighting how ParticleActions
* `samples/vr_movement.xml` file enables player movement within the CAVE.

### cweditor

Example projects from the cweditor java program. cweditor enabled CaveWriting project creation with a GUI.

**minimum.xml** contains the base xml necessary for each project. It includes the `PlacementRoot` (`Center`, `FrontWall`, `LeftWall`, `RightWall`, `FloorWall`) and the `Global` settings (`CameraPos`, `CaveCameraPos`, `Background`, `WandNavigation`). Each tag uses its default value.

**everything.xml** contains at least one of every possible Writing3D tag. The image (`w.png`) and sound (`bad.mp3`) used in the project are located in the `testMedia` subfolder. The default value seems to be used wherever possible, although I have not fully checked to be 100% sure.

### cw2_samples

Example projects broken down by object type. Many of the projects contain multiple objects but each is used to highlight a different object type and how they can be used.

**sample.xml** displays a piece of text and several text links. The links move the text object  to different walls.

**sample_image.xml** displays a single image and several text links. The different links move the image onto a given wall.

**sample_light.xml** displays 3 different lights and moves them around the CAVE.

**sample_model.xml** displays a single object and several text links. The links move the .obj file to different walls.

**sample_move.xml** displays several links. Clicking each link moves or rotates the link. One uses `MoveCave` to move the entire cave and the last link restarts the position of everything.

**sample_fountain.xml** highlights the usage of  `ParticleActionList`s rather than a specific object. It adds a bunch of particles inside the CAVE that float around some centered letters.

**sample_random.xml** highlights the usage of `Timeline`s rather than a specific object. It randomly selects one of 3 objects and moves them up or down. Note that this project uses `<Story version="5">` and must be translated to version 8 usage the `.xslt` files.

**sound_positional.xml** displays several instances of the same sound in different positions around the CAVE, as well as a few links. The sound(s) play in spatial audio when a link is pressed - some actually move the sound around in space.

**sound.xml** displays a single text object that, when clicked, plays a sound.

### samples

**vr_movement** enables player rotation and movement within the CAVE.

**sample_00_random.xml** is the same project as `cw2_samples/sample_random.xml` but uses `Story version="8">`



**sample_01_first.xml**, **sample_02_image.xml**, **sample_03_light.xml**, **sample_04_model.xml**, and **sample_05_move.xml** are updated versions of their counterparts in `cw2_samples`.


**particles/fountain.xml** is an updated version of `cw2_samples/sample_fountain.xml`. 

**sample_02alt_image.xml**
**sample_06_movie.xml**
**sample_07_stereoimage.xml**
**sample_08_stereoleftvsright.xml**
**sample_09_fontlights.xml**
**sample_10_textalign.xml**
**sample_11_click.xml**
**sample_12_move.xml**
**sample_13_scaling.xml**
**sample_14_alignment.xml**
**sample_15_multiline.xml**
**sample_16_multiline.xml**
**particles/text_blizzard.xml**

The files in `notYetPublished` are more example projects that were never completed. They may be useful to look at and see the development process but should generally be ignored.

### Student Projects

Three different student projects are found in the `projects` folder. These are completed projects used to develop this package. Run the script and see their projects for real!

### test

Input folder used during development.
