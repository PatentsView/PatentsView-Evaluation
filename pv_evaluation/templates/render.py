import os
import quarto
from jinja2 import Environment, PackageLoader
import shutil
from pkg_resources import resource_filename
from datetime import datetime


def render_inventor_disambiguation_report(outdir, summary_table_files, cache=True, **kwargs):
    """Create html report based on disambiguation results.

    Args:
        outdir (str): directory where to output html files.
        summary_table_files (list): list of paths to disambiguation table files (tables with the five columns "mention-id", "inventor_id", "patent_id", "name_first", and "name_last").
            File format can be one of tsv, csv, or parquet.
        cache (bool, optional): whether or not to cache jupyter chunk execution between runs. Defaults to True.

    Notes:
        * Summary table filenames are used for figure legends. Keep them short.
    """
    env = Environment(loader=PackageLoader("pv_evaluation", package_path="templates"))
    template = env.get_template("inventor/0-report.qmd")

    qmdpath = os.path.join(outdir, "index.qmd")
    htmlpath = os.path.join(outdir, "index.html")

    shutil.copyfile(resource_filename("pv_evaluation", "templates/inventor/header.html"), os.path.join(outdir, "header.html"))
    shutil.copyfile(resource_filename("pv_evaluation", "templates/inventor/footer.html"), os.path.join(outdir, "footer.html"))

    with open(qmdpath, "w+") as file:
        file.write(
            template.render(summary_table_files=summary_table_files, datetime=datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        )

    if quarto.path() is None:
        raise Exception("Could not find quarto. Is quarto (quarto.org) installed?")

    quarto.render(qmdpath, output_format="html", output_file=htmlpath, execute=True, cache=cache, **kwargs)
