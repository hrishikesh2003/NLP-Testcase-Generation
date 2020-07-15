"""file to deal with batch operations"""
import sys
import json
import xlwt
import extract_info
from fit_sheet_wrapper import FitSheetWrapper
from xlwt import Workbook

""" Gets the arguments from the command line input """
SENTENCES = sys.argv[1:]

wb = Workbook()
ws = FitSheetWrapper(wb.add_sheet('Sheet 1'))

style = xlwt.XFStyle()

font = xlwt.Font()
font.bold = True
style.font = font

i = 1
for request in SENTENCES:
    result = extract_info.main(request)

    ws.write(i, 0, "Test Case Number", style=style)
    ws.write(i, 1, result['case_id'])
    i += 1
    ws.write(i, 0, "Test Case Type", style=style)
    ws.write(i, 1, "Unique" if result['type'] else "General")
    i += 1
    ws.write(i, 0, "Test Case Description", style=style)
    ws.write(i, 1, result['action'])
    i += 1
    if len(result["inputs"]) > 0:
        ws.write_merge(
            i, i + len(result["inputs"]) - 1, 0, 0, "Expected Inputs", style=style)
        for inp in result["inputs"]:
            ws.write(i, 1, inp[0] + " = " + inp[1])
            i += 1
    else:
        ws.write(i, 0, "Expected Inputs", style=style)
        ws.write(i, 1, "-")
        i += 1
    ws.write(i, 0, "Expected Resuls", style=style)
    ws.write(i, 1, result['expectation'])
    i += 4

wb.save('genTestCases.xls')

print(json.dumps({"code":True}))
sys.stdout.flush()
