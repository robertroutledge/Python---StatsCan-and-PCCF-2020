"""
https://gitlab.com/denials/pccf-parser/-/blob/master/pccf_parser.py
Parse the Canandian Postal Code Conversion File (PCCF) data.

Writes out a TSV file that you can then load into a database or spreadsheet, or
any other program / script that needs to make sense of PCCF.

Optionally filters the data by Census Subdivision name.
"""

import struct
import csv

def parse_pccf_data(infile, outfile, csd=''):
    """Iterates through PCCF data to write a TSV file

    infile - FileIO input (usually a file handle for the PCCF data itself)
    outfile - CSV writer object
    csd - Optional name of a Census Subdivision to filter by"""


    for line in infile:
        fields = parser(line.encode('cp1252'))
        if (csd == '' or fields[5][0:len(csd)].decode('cp1252').rstrip() == csd):
            outfile.writerow([field.decode('cp1252').rstrip() for field in fields])

def pccf_parser():
    """Returns a parser for the PCCF data

    Structure drawn from field layout in PCCF Reference Guide:
      chars, data type, field name, description"""

    pccf_fields = (
            (6, 'c', 'PostalCode', 'Postal Code'),
            (3, 'c', 'FSA', 'Forward Sortation Area'),
            (2, 'c', 'PR', 'Province or territory code'),
            (4, 'c', 'CDuid', 'Census Division unique identifier'),
            (7, 'c', 'CSDuid', 'Census Subdivision unique identifier'),
            (70, 'c', 'CSDName', 'Census Subdivision name'),
            (3, 'c', 'CSDType', 'Census Subdivision type'),
            (3, 'c', 'CCSCode', 'Census Consolidated Subdivision code'),
            (3, 'c', 'SAC', 'Statistical Area Classification code (includes CMA/CA)'),
            (1, 'c', 'SACType', 'Statistical Area Classification type (includes CMA/CA)'),
            (7, 'c', 'CTName', 'Census Tract name'),
            (2, 'c', 'ER', 'Economic region code'),
            (4, 'c', 'DPL', 'Designated place code'),
            (5, 'c', 'FED13uid', 'Federal electoral district – 2013 Representation Order unique identifier'),
            (4, 'c', 'POP_CNTR_RA', 'Population centre/rural area code'),
            (1, 'c', 'POP_CNTR_RA_type', 'Population centre/rural area type'),
            (8, 'c', 'DAuid', 'Dissemination area unique identifier'),
            (3, 'c', 'DisseminationBlock', 'Dissemination block code'),
            (1, 'c', 'Rep_Pt_Type', 'Representative point type'),
            (11, 'c', 'LAT', 'Latitude of lowest level geographic area for postal code OM record (as indicated in Rep_point variable)'),
            (13, 'c', 'LONG', 'Longitude of lowest level geographic area for postal code OM record (as indicated in Rep_point variable)'),
            (1, 'c', 'SLI', 'Single link indicator'),
            (1, 'c', 'PCtype', 'Postal code type'),
            (30, 'c', 'Comm_Name', 'Community name'),
            (1, 'c', 'DMT', 'Delivery mode type'),
            (1, 'c', 'H_DMT', 'Historical delivery mode type'),
            (8, 'c', 'Birth_Date', 'Birth date (yyyymmdd)'),
            (8, 'c', 'Ret_Date', 'Retired date (yyyymmdd)'),
            (1, 'c', 'PO', 'Delivery installation'),
            (3, 'c', 'QI', 'Quality indicator'),
            (1, 'c', 'Source', 'Source of geocoding'),
            (1, 'c', 'POP_CNTR_RA_SIZE_CLASS', 'Population centre and rural area classification')
            )


    header = [fname for flen, ftype, fname, fdesc in pccf_fields]

    fmtstring = ''.join(["%d%s" % (flen, 's' if ftype == 'c' else 'i') for flen, ftype, fname, fdesc in pccf_fields])
    field_struct = struct.Struct(fmtstring)
    parser = field_struct.unpack_from

    return header, parser,pccf_fields

if __name__ == '__main__':
    pccf_source = 'pccfNat_fccpNat_112020.txt'
    pccf_datafile = 'pccf_subset_test.tsv'

    # optional: filter by CSD name
    csdname = ''

    header, parser,test_case = pccf_parser()


    with open(pccf_source, encoding='cp1252') as pccf_input, open(pccf_datafile, 'w', newline='') as pccf_out:
        writer = csv.writer(pccf_out, delimiter='\t')
        writer.writerow(header)
        #RR removed
        # parse_pccf_data(pccf_input, writer, csdname)
        parse_pccf_data(pccf_input, writer)
