from setuptools import setup

setup(
    name="lektor-butlablog",
    version="0.1",
    py_modules=["lektor_butlablog"],
    entry_points={"lektor.plugins": ["butlablog = lektor_butlablog:ButlablogPlugin"]},
)
