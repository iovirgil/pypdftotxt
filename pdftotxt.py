import PyPDF2

def extract_text_from_pdf(input_path, output_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                output_file.write(text)

    print("Text extraction completed successfully.")

# Example usage
pdf_path = '/home/user/file.pdf'  # Replace with your PDF file path
txt_path = '/home/user/export.txt'  # Replace with desired output text file path

extract_text_from_pdf(pdf_path, txt_path)
