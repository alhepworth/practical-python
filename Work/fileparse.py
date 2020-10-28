# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a delimited file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers=next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select and has_headers:
            indices=[headers.index(colname) for colname in select]
            headers=select
        elif select and not(has_headers):
            raise RuntimeError('Select but file has no headers')
        else:
            indices=[]

        records=[]
        for rowno, row in enumerate(rows,1):
            if not row: # Skip rows with no data
                continue
            # Filter the row if specific cols selected
            if indices:
                row=[row[index] for index in indices]

            # Convert type if specified
            if types:
                try:
                    row=[func(val) for func, val in zip(types,row)]
                except ValueError as e:
                    if not(silence_errors):
                        print(f'Row {rowno}: Could not convert {row}')
                        print(f'Row {rowno}: Reason {e}')

            if has_headers:
                record=dict(zip(headers,row))
            else:
                record=tuple(row)

            records.append(record)
    return records
