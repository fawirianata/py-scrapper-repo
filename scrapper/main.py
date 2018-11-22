from scrap import simple_get
from bs4 import BeautifulSoup

urlScrap=['https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Undang-Undang',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Perpu',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Peraturan-Pemerintah',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Peraturan-Presiden',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Keputusan-Presiden',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Peraturan-Menteri-Negara',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Keputusan-Menteri-Negara',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Instruksi-Menteri-Negara',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Peraturan-Menteri-ATR-Kepala-BPN',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Keputusan-Menteri-ATR-Kepala-BPN',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Surat-Edaran',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Peraturan-Lain',
    'https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Nota-Kesepahaman-MoU']

titleSrap=['Undang-Undang',
    'Perpu',
    'Peraturan-Pemerintah',
    'Peraturan-Presiden',
    'Keputusan-Presiden',
    'Peraturan-Menteri-Negara',
    'Keputusan-Menteri-Negara',
    'Instruksi-Menteri-Negara',
    'Peraturan-Menteri-ATR-Kepala-BPN',
    'Keputusan-Menteri-ATR-Kepala-BPN',
    'Surat-Edaran',
    'Peraturan-Lain',
    'Nota-Kesepahaman-MoU'
]
reqSection=simple_get(urlScrap[7])
soup=BeautifulSoup(reqSection,'html.parser')
pagerClassSoup=soup.find_all('div',{'class':'article_pager'})
pagingLinkSoup=pagerClassSoup[0].find_all('a',href=True)[0].get('href')
articleSoup=soup.find_all('div',{'class':'article'})
linkArticleSoup=articleSoup[0].find_all('a',href=True)[0].get('href')
titleArticleSoup=articleSoup[0].find_all('a',href=True)[0].get_text()
abstractArticleSoup=articleSoup[0].find_all('p')[0].get_text()
documentReq=simple_get(linkArticleSoup)
documentSoup=BeautifulSoup(documentReq,'html.parser')
aFinderDocumentSoup=documentSoup.find_all('li',{'class':'EDNdocument'})
linkDocumentSoup=aFinderDocumentSoup[0].find_all('a',href=True)[0].get('href')
urlDocument='https://www.atrbpn.go.id'+linkDocumentSoup
r = requests.get(urlDocument, stream = True, verify=False)
with open("aturan/"+titleArticleSoup.replace('/','-').replace(' ','-')+".pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):

         # writing one chunk at a time to pdf file
         if chunk:
             pdf.write(chunk)