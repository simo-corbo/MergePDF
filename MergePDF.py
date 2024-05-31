# simple python script to merge the PDF files in a given directory
# The given directory is given by click argument, if not provided it will take the current directory of the terminal
# The merged PDF file is saved as MergedPDF.pdf in the same directory 
# Order of the PDF files is based on the file name

import os
import click
from PyPDF2 import PdfMerger


def merge_pdf(path):
    pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]
    pdf_files.sort()
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(path + '/' + pdf)
    merger.write(path + '/MergedPDF.pdf')
    merger.close()
    print("PDF files merged successfully")

@click.command()
@click.option('--path', default=os.getcwd(), help='Path to the directory containing PDF files')
def main(path):
    merge_pdf(path)

if __name__ == '__main__':
    main()