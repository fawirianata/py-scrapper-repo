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
urlScrapSingle=['https://www.atrbpn.go.id/Publikasi/Peraturan-Perundangan/Nota-Kesepahaman-MoU']
tipeArtikel=['Undang-Undang',
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
# loop url yang akan di scrap
listTipeArtikel=[]
listHalamanArtikel=[]
listJudulArtikel=[]
listTentangArtikel=[]
listHalamanBaruArtikel=[]
listLinkDownload=[]
listDirektoriDownload=[]

for nomorTipeArtikel,url in enumerate(urlScrap):
	# print(nomorTipeArtikel,url)
	# get url yang akan di scrap
	req=simple_get(url)
	# initialize bs
	soup=BeautifulSoup(req,'html.parser')
	listHalaman=soup.find_all('div',{'class':'article_pager'})
	# extract listHalaman x=halaman y=kumpulanLinkHalaman z=linkHalaman
	for halaman in listHalaman:
		kumpulanLinkHalaman=halaman.find_all('a',href=True)
		for x in kumpulanLinkHalaman:
			linkHalaman=x.get('href')
			# print('---------------')
			# print(linkHalaman)
			# print('---------------')
			# scrap per halaman
			req=simple_get(linkHalaman)
			# initialize bs
			soup=BeautifulSoup(req,'html.parser')
			listArtikel=soup.find_all('div',{'class':'article'})
			# print(listArtikel)
			for x,artikel in enumerate(listArtikel):
				kumpulanArtikel=artikel.find_all('a',href=True)
				for x in kumpulanArtikel:
					halamanBaruArtikel=x.get('href')
					# print(halamanBaruArtikel)
					judulArtikel=x.get_text()
					# print(judulArtikel)
					# print('_______')

				kumpulanAbstrak=artikel.find_all('p')
				for x in kumpulanAbstrak:
					abstrakArtikel=x.get_text()
					if not abstrakArtikel:
						abstrakArtikel="Dokumen Kementerian Agraria dan Tataruang Republik Indonesia"
					else:
						abstrakArtikel=abstrakArtikel

				articleReq=simple_get(halamanBaruArtikel)
				documentSoup=BeautifulSoup(articleReq,'html.parser')
				aFinderDocumentSoup=documentSoup.find_all('li',{'class':'EDNdocument'})
				linkDocumentSoup=aFinderDocumentSoup[0].find_all('a',href=True)[0].get('href')
				linkDownload='https://www.atrbpn.go.id'+linkDocumentSoup
				namaFile=judulArtikel.replace(' ','-').replace('/','-').replace('.','').replace(',','')+'.pdf'

				hasil=linkHalaman+'; '+halamanBaruArtikel+'; '+linkDownload+'; '+judulArtikel.replace('.','').replace(',','').replace("\r","").replace("\n","")+'; '+abstrakArtikel.replace('.','').replace(',','').replace("\r","").replace("\n","")+'; '+namaFile+';'
				print(hasil)




# 			# pecah per article
# 			for nomor,artikel in enumerate(listArtikel):
# 				tipeArtikelIni=tipeArtikel[nomorTipeArtikel]
# 				halamanBaruArtikel=artikel[nomor].find_all('a',href=True)[nomor].get('href')
# 				judulArtikel=artikel[nomor].find_all('a',href=True)[nomor].get_text()
# 				tentangArtikel=artikel[nomor].find_all('p')[nomor].get_text()
# 				# request page halamanBaruArtikel
# 				articleReq=simple_get(halamanBaruArtikel)
# 				documentSoup=BeautifulSoup(articleReq,'html.parser')
# 				aFinderDocumentSoup=documentSoup.find_all('li',{'class':'EDNdocument'})
# 				linkDocumentSoup=aFinderDocumentSoup[0].find_all('a',href=True)[0].get('href')
# 				linkDownload='https://www.atrbpn.go.id'+linkDocumentSoup
# 				direktoriDownload=tipeArtikelIni+'/'+judulArtikel.replace(' ','-').replace('/','-')+'.pdf'

# 				listTipeArtikel.append(tipeArtikelIni)
# 				listHalamanArtikel.append(linkHalaman)
# 				listJudulArtikel.append(judulArtikel)
# 				listTentangArtikel.append(tentangArtikel)
# 				listHalamanBaruArtikel.append(halamanBaruArtikel)
# 				listLinkDownload.append(linkDownload)
# 				listDirektoriDownload.append(direktoriDownload)

# for i,v enumerate(listTipeArtikel):
# 	print(v+', '+listHalamanArtikel[i]+', '+listJudulArtikel[i]+', '+listTentangArtikel[i]+', '+listHalamanBaruArtikel[i]+', '+listLinkDownload[i]+', '+listDirektoriDownload[i])




