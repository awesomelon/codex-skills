import csv
import io


def download(names):
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    for name in names:
        writer.writerow([name])
    return output.getvalue()
