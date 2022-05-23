import os
import quarto
from jinja2 import Environment, PackageLoader
import shutil
from pkg_resources import resource_filename


def render_inventor_disambiguation_report(outdir, disambiguation_files, summary_table_files, execute=True, cache=True, **kwargs):
    env = Environment(loader=PackageLoader("pv_evaluation", package_path="templates"))
    template = env.get_template("inventor/0-report.qmd")

    qmdpath = os.path.join(outdir, "index.qmd")
    htmlpath = os.path.join(outdir, "index.html")

    shutil.copyfile(resource_filename("pv_evaluation", "templates/inventor/header.html"), os.path.join(outdir, "header.html"))
    shutil.copyfile(resource_filename("pv_evaluation", "templates/inventor/footer.html"), os.path.join(outdir, "footer.html"))

    with open(qmdpath, "w+") as file:
        file.write(template.render(disambiguation_files=disambiguation_files, summary_table_files=summary_table_files))
    
    quarto.render(qmdpath, output_format = "html", output_file = htmlpath, execute = execute, cache = cache, **kwargs)
