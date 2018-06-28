import subprocess
import difflib

def compare_databases(url1, url2):
    old = subprocess.check_output(['sqlacodegen', url1])
    new = subprocess.check_output(['sqlacodegen', url2])

    diff = difflib.HtmlDiff().make_file(
        old.decode("utf-8").split("\n"),
        new.decode("utf-8").split("\n"))

    outfile = open('database_diff.html', 'w')
    outfile.write(diff)
    outfile.close()


# run compare_databases with the two urls of the databases being compared. generated html file shows differences.
