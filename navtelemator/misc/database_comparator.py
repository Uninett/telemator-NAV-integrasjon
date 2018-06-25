import subprocess
import difflib
import os

def compare_databases(url1, url2):
    old = subprocess.check_output(['sqlacodegen', url1])
    new = subprocess.check_output(['sqlacodegen', url2])

    old_outfile = open('old_outfile.txt', 'a')
    old_outfile.write(old)
    old_outfile.close()
    old_outfile_read = open('old_outfile.txt', 'r')


    new_outfile = open('new_outfile.txt', 'a')
    new_outfile.write(new)
    new_outfile.close()
    new_outfile_read = open('new_outfile.txt', 'r')


    diff = difflib.HtmlDiff().make_file(old_outfile_read.readlines(), new_outfile_read.readlines())
    outfile = open('database_diff.html', 'w')
    outfile.write(diff)
    outfile.close()
    os.remove('old_outfile.txt')
    os.remove('new_outfile.txt')


# run compare_databases with the two urls of the databases being compared. generated html file shows differences.