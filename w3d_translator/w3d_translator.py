import typer
import glob
import threading
import os

from unity import UNITY_VERSION, UNITY_PATH
from validate import validate_input  # , validate_output
from threads import projectThread

# TODO: Configure typer character length (100)
# TODO: Configure color/style for typer.echo
# TODO: Prompt user for confirmation if --force is used (?)

# TEMPORARY OVERRIDES
# Skip validate_output
# Skip create_project and copy_files (xml_to_unity.py)
# Only translate run.xml (xml_to_unity.py)


# Opening message
def greeting(in_dir, out_dir):
    typer.echo("W3D TRANSLATOR")
    typer.echo(f"Unity Version:\t {UNITY_VERSION}")
    typer.echo(f'Please ensure Unity is installed at {UNITY_PATH}')
    typer.echo(f"IN_DIR:\t\t {in_dir}")
    typer.echo(f"OUT_DIR:\t {out_dir}")
    typer.echo()


# Ending message
def farewell():
    typer.echo()
    typer.echo("Translation Complete!")


def main(
    in_dir: str = typer.Argument(
        ...,
        help="Input folder containing the xml project"
    ),
    out_dir: str = typer.Argument(
        ...,
        help="Output folder for the translated project"
    ),
    multiple: bool = typer.Option(
        False,
        help="Translate multiple projects?"
    ),
    force: bool = typer.Option(
        False,
        help="Overwite OUT_DIR?"
    ),
):
    """
    Translate W3D xml projects in IN_DIR to Unity projects in OUT_DIR

    --multiple: Translate multiple projects. \
        Each one is a subfolder of IN_DIR and OUT_DIR
    --force: Overwrite OUT_DIR folder if it exists
    """

    # Print greeting and validate arguments
    greeting(in_dir, out_dir)
    validate_input(in_dir)
    # validate_output(out_dir, force) # TEMP - Don't delete file

    if multiple:
        # Each project is run on a different thread
        lock = threading.Lock()
        threads = []
        for idx, project_dir in enumerate(glob.glob(f'{in_dir}/*/')):
            validate_input(project_dir)

            thread = projectThread(
                idx,
                os.path.basename(os.path.normpath(project_dir)),
                project_dir,
                out_dir,
                lock
            )
            threads.append(thread)
            thread.start()

        # Collect threads
        [t.join() for t in threads]
    else:
        t = projectThread(
            0,
            os.path.basename(os.path.normpath(in_dir)),
            in_dir,
            out_dir
        )
        t.start()
        t.join()

    # Print farewell and exit
    farewell()


if __name__ == '__main__':
    typer.run(main)
