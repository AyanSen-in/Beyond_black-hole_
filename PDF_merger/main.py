import PyPDF2
import os


def merge_pdfs(output_filename, input_files):
    # Use PdfMerger (PyPDF2 >= 1.28 / 2.x / 3.x)
    pdf_merger = PyPDF2.PdfMerger()

    appended_any = False
    for file in input_files:
        if not os.path.exists(file):
            print(f"Warning: File '{file}' not found. Skipping...")
            continue
        try:
            with open(file, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)
                appended_any = True
                print(f"Added: {file}")
        except Exception as e:
            print(f"Error reading '{file}': {e}")

    if not appended_any:
        print("No valid PDF files to merge. Aborting.")
        pdf_merger.close()
        return

    try:
        with open(output_filename, 'wb') as output_file:
            pdf_merger.write(output_file)
        print(f"PDFs merged successfully! Output file: {output_filename}")
    except Exception as e:
        print(f"Error writing output file: {e}")
    finally:
        pdf_merger.close()


def main():
    print("PDF Merge Tool")
    print("Please enter the names of the two PDF files to merge:")

    pdf1 = input("PDF 1: ").strip().strip('"').strip("'")
    pdf2 = input("PDF 2: ").strip().strip('"').strip("'")
    output_filename = input("Enter the name for the merged PDF: ").strip().strip('"').strip("'")

    merge_pdfs(output_filename, [pdf1, pdf2])


if __name__ == "__main__":
    main()