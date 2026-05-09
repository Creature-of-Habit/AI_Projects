from pypdf import PdfReader


reader = PdfReader('me/linkedin.pdf')
linkedin = ''
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

with open('me/summary.txt','r',encoding='utf-8') as f:
    summary = f.read()

