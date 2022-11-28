import os
import quarto
from jinja2 import Environment, PackageLoader
import shutil
from pkg_resources import resource_filename
from datetime import datetime


def render_inventor_disambiguation_report(outdir, disambiguation_files, inventor_not_disambiguated, cache=True, **kwargs):
    """Create html report based on disambiguation results.

    Args:
        outdir (str): directory where to output html files.
        disambiguation_files (list): list of string paths to disambiguation files (tables with the two columns "mention_id" and "inventor_id"). Files format can be one of tsv, csv, or parquet.
        inventor_not_disambiguated (str): string path to a file containing the columns "patent_id", "inventor_sequence", "raw_inventor_name_first", and "raw_inventor_name_last".
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
