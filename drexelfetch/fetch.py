import subprocess
from pathlib import Path

import polars as pl


def get_quotes_df() -> pl.DataFrame:
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

    quotes_path = Path(f"{git_repo}/courses.csv")

    return pl.read_csv(quotes_path, sep=",")

def main():
    print(get_quotes_df())

if __name__ == "__main__":
    print(get_quotes_df())
