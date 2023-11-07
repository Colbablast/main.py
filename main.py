from PyPDF2 import PdfReader
import os

# SETUP --------------------------------------------------------------------------------------------
# Get all files in directory excluding the current python file
directory = os.listdir()
directory.remove(os.path.basename(__file__))

# For .idea pycharm folder (so I can code in pyCharm)
if ".idea" in directory:
    directory.remove(".idea")

# Make sure there are at least two PDF files in the directory
if len(directory) < 2:
    input("There needs to be at least two files in the directory.\n")
    exit()


# FUNCTION -------------------------------------------------------------------------------------------
def get_pdf(file_name):
    # Get name of the two pdf's then open them
    while True:
        try:
            print(f"Pick what PDF is your {file_name} (0 - {len(directory) - 1}):")
            for index, file in enumerate(directory):
                print(f"{index} - {file}")
            pdf_name = directory[int(input("> ")) - 1]
            reader = PdfReader(pdf_name)
        except:
            print(f"Error opening {file_name}.")
        else:
            break
    return pdf_name, reader


# Get the user to pick the lines they want to use for each pdf
def pick_pages(pdf_name, reader):
    while True:
        try:
            max_page = len(reader.pages)
            print(f"Choose a range of pages for {pdf_name} to check, total pages are 1 - {max_page}")
            page_range = [int(input("Start: ")), int(input("End: "))]
            for num in page_range:
                if num not in range(1, max_page + 1):
                    print(f"{num} is not in the available range.")
                    continue
        except ValueError:
            print("You entered something that isn't an integer.")
        else:
            break
    return page_range


# MAIN ------------------------------------------------------------------------------------------------
# Get pdf name and pdf file
info_pdf, info_reader = get_pdf("information")
assignment_pdf, assignment_reader = get_pdf("assignment")

# Get page ranges
info_pages = pick_pages(info_pdf, info_reader)
assignment_pages = pick_pages(assignment_pdf, assignment_reader)

# getting a specific page from the pdf file
# page = info_reader.pages[0]
# print(page.extract_text())

text = ""
for page in info_reader.pages:
    text += page.extract_text() + "\n"
print(text)
