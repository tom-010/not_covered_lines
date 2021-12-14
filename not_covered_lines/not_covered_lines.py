import pathlib
from coverage.control import Coverage
from coverage.report import get_analysis_to_report


def not_covered_lines(path_to_coverage_file):
    """
    It returns all not covered lines from a previous run of 
    `coverage.py`, which stores its data in `.coverage`. The 
    path can either be the path to directory in which this 
    `.coverage` file resides or the path to the file itself. 

    """
    
    path_to_coverage_file = _normalize_path(path_to_coverage_file)
    
    current_dir = '/'.join(path_to_coverage_file.split('/')[:-1])
    coverage_base_path = str(pathlib.Path(current_dir).absolute()) + '/'
    
    print(path_to_coverage_file)
    coverage = Coverage(data_file=path_to_coverage_file, check_preimported=True, messages=True)
    coverage.load()

    res = set()

    analysis = get_analysis_to_report(coverage, [])
    for file_reporter, analysis in get_analysis_to_report(coverage, []):
        fullname = analysis.filename
        filename = fullname.replace(coverage_base_path, '')
        missing_lines = analysis.missing
        if not missing_lines:
            continue
        for line in missing_lines:
            res.add((filename, line))
    return res

def _normalize_path(path):
    if path.endswith('/'):
        path = path[:-1]
    if not path.endswith('.coverage'):
        path += '/.coverage'
    return path