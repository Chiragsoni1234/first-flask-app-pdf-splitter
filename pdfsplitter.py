from PyPDF2 import PdfReader, PdfWriter

def cropper(start, end, file):
    # Open the PDF file
    with open(file, "rb") as f:
        inputPdf = PdfReader(f)
        outPdf = PdfWriter()

        # Create output file name
        output_file = file.split(".")[0] + "cropped" + ".pdf"

        # Open the output file for writing
        with open(output_file, "wb") as ostream:
            for page_num in range(start, end + 1):
                # Add the specified pages to the output PDF
                outPdf.add_page(inputPdf.pages[page_num])
            
            # Write the output PDF to the file
            outPdf.write(ostream)

# Example usage:
# cropper(0, 1, "example.pdf")
