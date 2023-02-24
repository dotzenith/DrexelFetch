import polars as pl
import subprocess
from pathlib import Path

def get_courses_df() -> pl.DataFrame:
    """
    Returns the top-level git repo's path
    """

    git_repo = (
        subprocess.Popen(
            ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE
        )
        .communicate()[0]
        .rstrip()
        .decode("utf-8")
    )

    courses_path = Path(f"{git_repo}/courses.csv")

    return pl.read_csv(courses_path, sep=",")
