from PyPDF2 import PdfWriter, PdfReader
import os


def split_file(file_name, Destination_folder, pr):
    file = source_path + "\\" + file_name
    # define filename
    fn = os.path.basename(file)
    fn = fn.rstrip(".pdf")
    fn = pr + fn[fn.find("_")]

    input_pdf = PdfReader(file)
    for i in range(len(input_pdf.pages)):
        output = PdfWriter()
        output.add_page(input_pdf.pages[i])
        j = "{:04n}".format(i + 1)
        f = Destination_folder[Destination_folder.find("_") + 1:]
        of = fn + f'{f}_1_{j}' + ".pdf"
        cn = Destination_folder + "/"  # + of
        with open(cn, "wb") as output_stream:
            output.write(output_stream)
            print(fn + "  splitting .... " + str(i + 1) + " of " + str(len(input_pdf.pages)))


source_path = input(r"Enter the source directory path : ")
dest_path = input(r"enter the destination directory path : ")
prefix = input("Enter the prefix you wish to name:")

root = source_path
r = "\\"
root_name = root[root.rindex(r) + 1:]
root = dest_path + "\\" + root_name
os.mkdir(root)

for filename in os.listdir(source_path):
    split_file(filename, root, prefix)
