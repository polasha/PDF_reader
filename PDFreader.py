import PyPDF2

pdfFileObject = open("Mostafa_Md. Surat_Curriculum Vitae_ 1990-11-09.pdf ", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

print(" No. Of Pages :", pdfReader.numPages)

pageObject = pdfReader.getPage(0)

print(pageObject.extractText())

pdfFileObject.close()