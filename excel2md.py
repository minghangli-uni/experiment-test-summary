#!/usr/bin/env python3
import sys
import pandas as pd

def excel_to_markdown(excel_file, output_markdown):
    # Load the Excel file with pandas.
    xls = pd.ExcelFile(excel_file)
    with open(output_markdown, "w") as out_file:
        for sheet in xls.sheet_names:
            # Write the sheet name as a level-2 md heading.
            out_file.write(f"## {sheet}\n\n")
            df = pd.read_excel(xls, sheet_name=sheet)
            if df.empty:
                out_file.write("*(No data found)*\n\n")
            else:
                # Replace "nan" with "N/A"
                df = df.astype(str).replace("nan", "N/A")

                md_table = df.to_markdown(index=False)
                out_file.write(md_table + "\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 excel2md.py input_excel_file.xlsx output_markdown_file.md")
        sys.exit(1)
    excel_to_markdown(sys.argv[1], sys.argv[2])