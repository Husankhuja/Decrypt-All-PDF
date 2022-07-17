from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file:
    reader = PdfFileReader(input_file)
    if reader.isEncrypted:
      reader.decrypt(password)  

      writer = PdfFileWriter()
      for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))

        with open(output_path, 'wb') as output_file:
          writer.write(output_file)

if __name__ == '__main__':
  folderPath = os.getcwd()
  password = input('Enter Password: ')
  for file in os.listdir(folderPath):
    if file[-4:] == '.pdf':
      ogf = os.path.join(folderPath, file)
      newf = os.path.join(folderPath, file[:-4] + '-decrypted.pdf')
      decrypt_pdf(ogf, newf, password)