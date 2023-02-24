import polars as pl

from drexelfetch.helpers import get_courses_df

classes = get_courses_df()
course_ids = list(classes.get_column("course number"))


def info(course: str) -> dict:
    course_info = classes.filter(pl.col("course number") == course).to_dict(
        as_series=False
    )
    return {key: value[0] for key, value in course_info.items()}


def prereq(course: str) -> list:
    course_preqs = classes.filter(pl.col("prereqs").str.contains(course))
    return list(course_preqs.get_column("course number"))
