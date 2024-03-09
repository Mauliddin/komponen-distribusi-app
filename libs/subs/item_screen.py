from kivymd.uix.screen import MDScreen


class Item(MDScreen):
    from_camera = False

    def on_back(self):
        if self.from_camera:
            self.manager.current = "camera_page"
            self.manager.transition.direction = "right"
        else:
            self.manager.current = "library_page"
            self.manager.transition.direction = "right"


class ItemPenghantar(Item):
    text1 = (
        "Penghantar adalah materi atau bahan yang memiliki kemampuan untuk menghantarkan arus listrik. "
        "Mereka memungkinkan aliran elektron dari satu titik ke titik lainnya dalam suatu rangkaian listrik. "
        "Biasanya, penghantar terbuat dari logam seperti tembaga atau aluminium karena kemampuan konduktif "
        "yang tinggi. Namun, ada juga penghantar non-logam yang digunakan dalam aplikasi khusus, seperti grafen "
        "atau karbon nanotube."
    )
    
    image1 = "data/pic/item/kawat_aluminium.jpg"
    image2 = "data/pic/item/kabel.jpg"


class ItemKabel(Item):
    text1 = (
        "Kabel  merupakan  penghantar  yang  dibungkus atau dilapisi oleh bahan isolasi. Dalam jaringan "
        "distribusi listrik umumnya dibedakan berdasarkan fungsi, material insulasi, konstruksi serta "
        "penyalurannya. Jenis kabel menurut fungsinya dapat dibagi menjadi kabel listrik tegangan rendah, "
        "kabel listrik tegangan menengah, dan kabel listrik tegangan tinggi. "
    )
    text2 = (
        "Jika dilihat dari material insulasi maka kabel listrik dibedakan menjadi kabel listrik dengan "
        "insulasi PVC, kabel listrik dengan insulasi XLPE, dan kabel listrik dengan insulasi kertas. "
        "Selain itu, apabila ditinjau dari segi konstruksinya maka dibedakan menjadi single core, "
        "multi core, dan shielded. sedangkan berdasarkan penyalurannya dapat dibagi menjadi kabel udara "
        "dan kabel bawah tanah."
    )
    
    image1 = "data/pic/item/kabel.jpg"

class ItemKawat(Item):
    text1 = (
        "kawat adalah jenis penghantar yang tidak dilindungi oleh bahan isolasi. Secara umum kawat "
        "terbuat dari bahan konduktor yang mempunyai konduktivitas yang baik seperti tembaga, aluminium, "
        "dan baja."
    )
    
    image1 = "data/pic/item/kawat_aluminium.jpg"
    image2 = "data/pic/item/kawat_tembaga.jpg"

class ItemKawatAluminium(Item):
    text1 = (
        "Aluminium merupakan suatu logam yang sangat ringan, beratnya kirakira sepertiga dari tembaga, "
        "dan mempunyai tahanan jenis tiga kali dari tembaga. Sifat logam aluminium ini mudah "
        "dibengkok-bengkokkan karena lunaknya. Oleh karena itu kekuatan tarik dari kawat aluminium "
        "lebih rendah dari kawat tembaga, yaitu setengah dari kekuatan tarik kawat tembaga. Untuk "
        "itu kawat aluminium hanya dapat dipakai pada gawang (span) yang pendek, "
        "sedangkan untuk gawang yang panjang dapat digunakan kawat aluminium "
        "yang dipilin menjadi satu dengan logam yang sejenis maupun yang tidak "
        "sejenis, agar mempunyai kekutan tarik yang lebih tinggi."

        )
    text2 = (
        "Oleh karena itu kawat aluminium baik sekali digunakan sebagai kawat penghantar jaringan. "
        "Kelemahan kawat aluminium ini tidak tahan akan pengaruh suhu, sehingga "
        "pada saat cuaca dingin regangan (stress) kawat akan menjadi kendor. Agar "
        "kekendoran regangan kawat lebih besar, biasanya dipakai kawat aluminium "
        "campuran (alloy aluminium wire) pada gawang-gawang yang panjang. Selain "
        "itu kawat aluminium tidak mudah dipatri (disolder) maupun di las dan tidak "
        "tahan akan air yang bergaram, untuk itu diperlukan suatu lapisan dari logam "
        "lain sebagai pelindung. "
    )
    text3 = (
        "Juga kawat aluminium ini mudah terbakar, sehingga "
        "apabila terjadi hubung singkat (short circuit) akan cepat putus. Karena itu "
        "kawat aluminium ini banyak digunakan untuk jaringan distribusi sekunder "
        "maupun primer yang sedikit sekali mengalami gangguan dari luar. Sedangkan "
        "untuk jaringan transmisi kawat yang digunakan adalah kawat aluminium "
        "capuran dengan diperkuat oleh baja (aluminium conductor steel reinforsed) "
        "atau (aluminium clad steel)."
    )
    image1 = "data/pic/item/kawat_aluminium.jpg"

class ItemKawatTembaga(Item):

    text1 = (
        "Tembaga murni merupakan logam liat berwarna kemerah- merahan, "
        "yang mempunyai tahanan jenis 0,0175 dengan berat jenis 8,9 dan titik cair "
        "sampai 1083° C, lebih tinggi dari kawat aluminium. Kawat tembaga ini "
        "mempunyai konduktivitas dan daya hantar yang tinggi. Pada mulanya kawat "
        "tembaga ini banyak dipakai untuk penghantar jaringan, tetapi bila "
        "dibandingkan dengan kawat aluminium untuk tahanan (resistansi) yang sama, "
        "kawat tembaga lebih berat sehingga harganya akan lebih mahal. Dengan berat "
        "yang sama, kawat alauminium mempunyai diameter yang lebih besar dan "
        "lebih panjang dibandingkan kawat tembaga."
    )
    
    image1 = "data/pic/item/kawat_tembaga.jpg"

class ItemTiangPenyangga(Item):
    text1 = (
        "Tiang penyangga adalah salah satu komponen jaringan distribusi yang sangat dibutuhkan pada "
        "saluran udara jaringan distribusi. Tiang penyangga digunakan untuk menjaga saluran agar tetap "
        "berada pada jarak aman yang diperbolehkan. Tiang penyangga biasanya terbuat dari kayu, "
        "baja atau beton. Jarak tiap tiang penyangga diatur agar penghantar tetap terletak pada jarak aman."
    )
    
    image1 = "data/pic/item/tiang-beton.jpg"
    
class ItemTiangKayu(Item):
    text1 = (
        "Tiang kayu digunakan sebagai penyangga jaringan disebabkan konstruksinya yang sederhana dan "
        "biayanya lebih murah dibandingkan dengan tiang jenis yang lain. Tiang ini juga merupakan "
        "isolator (penyekat) yang baik sehingga sangat cocok untuk dijadikan tiang penyangga. "
        "Jenis kayu yang digunakan dalam pembuatannya berasal dari jenis tertentu. Di indonesia jenis "
        "kayu yang digunakan berupa kayu jati, kayu ulin, kayu rasamala. Kekurangan dari tiang jenis ini "
        "adalah persediaannya berdasarkan dari ketersediaan stok kayu, diperlukannya pengawetan terlebih "
        "dahulu, serta umurnya yang pendek."
    )
    
    image1 = "data/pic/item/tiang_kayu.jpg"
    

class ItemTiangBaja(Item):
    text1 = (
        "Tiang baja menggunakan pipa-pipa baja berbentuk bulat dengan diameter yang bervariasi dari pangkal "
        "sampai ujung nya. Diameter penampang bagian pangkal biasanya lebih besar dari ujung penampangnya. "
        "Dikarenakan  kekokohan konstruksinya tiang baja banyak digunakan untuk penopang jaringan distribusi "
        "tegangan tinggi yang mempunyai beban lebih besar dibandingkan dengan jaringan distribusi tegangan "
        "rendah. Kekurangan dari tiang ini adalah biayanya pemeliharaan dan pengangkutannya lebih mahal "
        "dibandingkan dengan tiang kayu maupun tiang beton."
    )
    
    image1 = "data/pic/item/tiang-baja.jpg"
    

class ItemTiangBeton(Item):
    text1 = (
        "Tiang listrik distribusi yang terbuat dari beton merupakan salah satu jenis yang paling umum "
        "digunakan. Mereka dibuat dengan mencampur beton dengan serat baja untuk memberikan kekuatan dan "
        "keawetan yang diperlukan. Tiang beton tahan terhadap cuaca dan korosi, sehingga mereka cocok untuk "
        "digunakan di daerah dengan kondisi lingkungan yang keras. Tiang beton juga relatif mudah diproduksi "
        "dan biayanya lebih terjangkau dibandingkan dengan beberapa jenis tiang lainnya. Namun, tiang beton "
        "memiliki kekurangan berupa berat dan sulit dipindahkan, kurang fleksibel, serta membutuhkan waktu "
        "produksi yang lebih lama. Dalam memilih tiang listrik distribusi, perlu mempertimbangkan kebutuhan "
        "spesifik dan lingkungan sekitar."
    )
    
    image1 = "data/pic/item/tiang-beton.jpg"
    

class ItemFuseCutOut(Item):
    text1 = (
        "Fuse Cut Out adalah alat yang digunakan untuk mengamankan jaringan listrik. cara kerjanya dengan "
        "memutuskan rangkaian jaringan listrik melalui peleburan bagian komponennya sehingga menyebabkan rangkaian "
        "terputus apabila besar arus pada jaringan melebihi nilai tertentu. Fuse Cut Out berfungsi untuk "
        "mengamankan jaringan tegangan menengah dari gangguan hubung singkat antar fasa maupun fasa tanah, "
        "sedangkan Fuse Cut Out yang dipasangkan di atas trafo berfungsi sebagai pengaman gangguan hubung singkat "
        "pada trafo."
    )
    
    image1 = "data/pic/item/fuse-cut-out.jpg"
    

class ItemLightningArrester(Item):
    text1 = (
        "Lightning Arrester merupakan alat yang digunakan untuk melindungi sistem tenaga listrik yang "
        "disebabkan oleh surja petir. Alat ini bekerja dengan menghambat surja tegangan lebih yang datang "
        "dan menyalurkannya ke tanah. "
    )
    
    image1 = "data/pic/item/lightning-arrester.jpg"
    
    

class ItemLightningArresterEkspulsi(Item):
    text1 = (
        "Arrester jenis ekspulsi memiliki dua sela, yaitu sela luar dan sela dalam. arrester jenis ini "
        "bekerja apabila gangguan tegangan lebih (over voltage) maupun turja petir mengenai terminal "
        "arrester, maka sela percik batang yang berada di luar dan sela percik yang berada dalam tabung "
        "akan menimbulkan percikan. Panas yang disebabkan oleh mengalirnya arus susulan dalam tabung serat "
        "menyebabkan tabung tersebut mengeluarkan gas. Arus itu berbentuk sinusoidal yang seiring waktu akan "
        "berada pada siklus dengan nilai nol. pada kondisi nol gas yang terdapat pada tabung akan berfungsi "
        "sebagai isolasi untuk memadamkan arus tersebut."
    )
    
    image1 = "data/pic/item/lightning-arrester-ekspulsif.jpg"
    

class ItemLightningArresterKatup(Item):
    text1 = (
        "Pada arrester ini beberapa sela percik disusun secara seri dengan resistor non linier."
        "apabila dilewati oleh arus besar tahanan resistor tersebut akan memiliki nilai resistansi "
        "yang kecil dan nilai resistansinya akan menjadi besar jika nilai arus yang mengalirinya kecil."
        "Resistor non linier dan sela percikan diletakkan didalam tabung isolasi sehingga udara luar "
        "tidak dapat mempengaruhinya."
    )
    
    image1 = "data/pic/item/lightning-arrestors-katup.jpg"
    

class ItemIsolator(Item):
    text1 = (
        "Isolator merupakan peralatan listrik yang berfungsi untuk mengisolasi penghantar atau konduktor."
        "Pada jaringan distribusi, isolator digunakan untuk memisahkan secara elektris konduktor supaya "
        "menghindari terjadi kebocoran arus (leakage current) atau loncatan bunga api (flash over) yang "
        "akan mengakibatkan terjadinya kerusakan pada sistem jaringan tenaga listrik. Isolator dalam "
        "konstruksinya menggunakan bahan berupa keramik / porselen dan kaca merupakan isolator yang paling "
        "banyak dipakai dalam sistem distribusi listrik. "
    )
    
    image1 = "data/pic/item/isolator.jpg"
    

class ItemIsolatorPin(Item):
    text1 = (
        "Isolator jenis pinmerupakan isolator yang pertama kali dirancang sebagai "
        "penopang penghantar saluran. Isolatorpinini banyak digunakan pada jaringan "
        "distribusi tegangan menengah sebagai penyangga konduktor. Isolator jenis pin ini "
        "digunakan pada tiang pendukung jaringan distribusi hantaran udara. Isolator pin "
        "terdiri dari satu atau beberapa lapisan petticoats (rain shed) yang disemen, dipasang "
        "pada poros crossarm pada tiang pendukung. Isolator pin dilengkapi dengan lapisan-lapisan "
        "(rain shed) yang cukup panjang untuk memperpanjang jarak rambat isolator sehingga lewat denyar "
        "(flashover) tidak mudah untuk terjadi. Lapisan petticoats dirancang sedemikian rupa agar air hujan "
        "yang membasahi permukaan isolator tidak menempel pada isolator."
    )
    text2 = (
        "Beberapa kelebihan dari isolator pin adalah sebagai berikut :\n"
        "1. Berdasarkan perbandingan jarak rambat (creepage distance) dengan jarak percik (arching distance), "
        "isolator pin termasuk dalam kategori isolator kelas B. \n"
        "2. Isolator pin dirancang dengan profil yang sedemikian sehingga pada saat hujan membasahi permukaan "
        "isolator, maka air hujan dapat diteteskan dari permukaannya agar tidak terjadi "
        "penimbunan polusi pada permukaan isolator. \n"
        "3. Isolator pin hanya dapat digunakan pada beban tekan. Artinya isolator pin ini "
        "didesain agar dapat menahan beban konduktor yang terpasang pada saluran udara tegangan menegah."
    )
    
    image1 = "data/pic/item/pin-insulator.jpg"
    

class ItemIsolatorPost(Item):
    text1 = (
        "Sama halnya dengan isolator pin, isolator post juga digunakan pada tegangan "
        "tinggi, khususnya pada jaringan distribusi tegangan menengah. Isolator jenis post "
        "digunakan pada tiang-tiang pendukung dan tiang sudut distribusi hantaran udara. Isolator post "
        "terdiri atas bahan isolator berbentuk silinder padat dengan sisi berlekukan untuk memperpanjang "
        "jarak rambat permukaan isolator. Semakin tinggi tegangan isolasinya makin banyak lekukan-lekukan "
        "tersebut. Untuk pengoperasian tegangan yang lebih tinggi lebih cocok digunakan isolator post karena "
        "harganya lebih murah jika dibandingkan dengan menggunakan isolator pin."
    )
    text2 = (
        "Beberapa kelebihan dari isolator post adalah sebagai berikut:\n"
        "1. Memiliki kekuatan dielektrik yang lebih tinggi dibandingkan dengan isolator pin. \n"
        "2. Isolator post termasuk dalam kategori isolator kelas. Artinya tegangan lewat denyar "
        "isolator post lebih tinggi dari tegangan lewat denyar isolator pin. \n"
        "3. Isolator post dapat digunakan untuk menahan beban tarik dan beban tekuk."
    )
    
    image1 = "data/pic/item/post-insulator.jpg"
    

class ItemIsolatorSpool(Item):
    text1 = (
        "Isolator jenis cincin (spool type insulator), digunakan pada tiang-tiang lurus (tangent pole) "
        "dengan sudut 0° sampai 10°, yang dipasang secara horizontal maupun vertikal. Isolator cincin "
        "bentuknya bulat berlubang ditengahnya seperti cincin yang hanya terdapat satu atau dua lekukan "
        "saja yang seluruhnya terbuat dari bahan porselin."
    )
    text2 = (
        "Isolator cincin ini tidak menggunakan pasak (pin) sehingga isolator cincin memiliki kualitas "
        "tegangannya lebih rendah. Biasanya tak lebih dari 3 kV. Isolator cincin ini besarnya tidak lebih "
        "dari 7,5 cm tinggi maupun diameternya, yang dipasangkan pada jaringan distribusi sekunder serta "
        "saluran pelayanan ke rumah-rumah. \n"
        "Isolator ini dipasang pada sebuah clamp (pengapit) dengan sebuah pasak yang dimasukkan ke dalam "
        "lubang ditengahnya. Pemasangan secara horizontal digunakan untuk jaringan lurus (tangent line) "
        "dengan sudut antara 0° sampai 10°. Untuk jaringan lurus (angle line) untuk sudut lebih dari 10° "
        "dipasang pada kedudukan vertikal. Kesemuanya dipasang pada tiang penyangga dengan jarak satu meter "
        "dari tiang atau 60 cm dari palang kayu (cross arm)."
    )
    
    image1 = "data/pic/item/spool-insulator.jpg"
    

class ItemIsolatorSuspension(Item):
    text1 = (
        "Isolator jenis gantung (suspension type insulator), digunakan pada tiang-tiang sudur (angle pole) "
        "untuk sudut 30° sampai 90°, tiang belokan tajam, dan tiang ujung (deadend pole). Isolator jenis "
        "clevis lebih banyak digunakan karena lebih kokoh dan kuat dalam penggandengannya, serta tidak ada "
        "kemungkinan lepas dari gandengannya, karena pada ujungnya digunakan mur baut untuk mengikatnya. \n"
        "Isolator gantung (suspension insulator) terdiri dari sebuah piringan yang terbuat dari bahan "
        "porselin, dengan tutup (cap) dari bahan besi tempaan (melleable iron) dan pasaknya terbuat dari "
        "bahan baja yang diikatkan dengan semen yang berkualitas, sehingga membentuk satu unit isolator "
        "yang berkualitas tinggi. \n"
    )
    text2 = (
        "Dibandingkan isolator jenis pasak, isolator gantung ini hanya mempunyai satu piringan yang terbuat "
        "dari bahan porselin atau bahan gelas biru kelabu (blue gray glaze). Dengan menggunakan bahan gelas "
        "biru kelabu ini harga isolator dapat ditekan lebih murah dan dapat digunakan untuk beberapa "
        "gandengan. Umumnya isolator gantung dengan bahan gelas ini digunakan untuk jaringan distribusi "
        "primer, sedangkan isolator gantung dari bahan porselin banyak digunakan untuk gandengan-gandengan "
        "pada jaringan transmisi tegangan tinggi."
    )
    
    image1 = "data/pic/item/suspension-insulator.jpg"
    

class ItemGarduDistribusi(Item):
    text1 = (
        "Gardu Distribusi merupakan suatu bangunan gardu listrik berisi atau terdiri dari instalasi "
        "Perlengkapan Tegangan Menengah (PHB-TM) dan Perlengkapan Hubung Bagi Tegangan Rendah (PHB-TR) "
        "untuk memasok kebutuhan tenaga listrik bagi para pelanggan baik Tegangan Menengah (TM 20 kV) "
        "maupun Tegangan Rendah (TR 220/380V). Jenis perlengkapan hubung bagi tegangan menengah pada gardu "
        "distribusi berbeda sesuai dengan jenis konstruksi gardunya. "
    )
    
    image1 = "data/pic/item/gardu-portal.jpg"
    

class ItemGarduPortal(Item):
    text1 = (
        "Gardu Portal adalah gardu listrik jenis terbuka (outdoor) dengan memakai konstruksi dua "
        "tiang atau lebih. Tempat kedudukan transformator sekurang – kurangnya 3 meter di atas tanah "
        "dan ditambahkan platform sebagai fasilitas kemudahan kerja teknisi operasi dan pemeliharaan. "
        "Transformator dipasang bagian atas dan lemari panel atau PHB-TR pada bagian bawah. Lokasi "
        "penempatan gardu portal biasanya berdekatan langsung dengan daerah pelayanan konsumen, tegangan "
        "disalurkan ke konsumen melewati jurusan-jurusan, dan untuk setiap unit gardu portal dapat "
        "disalurkan sampai empat jurusan. "
    )
    
    image1 = "data/pic/item/gardu-portal.jpg"
    

class ItemGarduCantol(Item):
    text1 = (
        "Gardu Cantol adalah tipe gardu distribusi jenis pasangan luar (outdoor) yang terpasang dengan "
        "konstruksi 1 tiang dan memiliki transformator yang terpasang jenis 3 phasa atau 1 phasa dengan "
        "tipe CSP (Completely Self Protected Transformator) yaitu peralatan switching dan proteksinya sudah "
        "terpasang lengkap dalam tangki transformator. Perlengkapan perlindungan tambahan LA "
        "(Lightning Arrester) dipasang terpisah dengan penghantar hubung bagi tegangan rendah (PHB-TR) "
        "maksimum 2 jurusan dengan saklar pemisah pada sisi masuk dan pengaman lebur (type NH,NT) sebagai "
        "pengaman jurusan. Semua bagian konduktif terbuka (BKT) dan bagian konduktif ekstra (BKE) "
        "dihubungkan dengan pembumian sisi tegangan rendah."
    )
    
    image1 = "data/pic/item/gardu-cantol-satu-fasa.jpg"
    image2 = "data/pic/item/gardu-cantol-tiga-fasa.jpg"
    

class ItemGarduKios(Item):
    text1 = (
        "Gardu kios adalah bangunan prefabricated terbuat dari konstruksi baja, fiberglass atau "
        "kombinasinya, yang dapat dirangkai di lokasi rencana pembangunan gardu distribusi. Terdapat "
        "beberapa jenis konstruksi, yaitu kios kompak, kios modular dan kios bertingkat. Gardu ini "
        "dibangun di tempat-tempat yang tidak diperbolehkan membangun gardu beton. Karena sifat "
        "mobilitasnya, maka kapasitas transformator distribusi yang terpasang terbatas. Kapasitas "
        "maksimum adalah 400 kVA, dengan empat jurusan tegangan rendah. Khusus untuk kios kompak, "
        "seluruh instalasi komponen utama gardu sudah dirangkai selengkapnya di pabrik, sehingga "
        "dapat langsung diangkut ke lokasi dan disambungkan pada sistem distribusi yang sudah ada "
        "untuk difungsikan sesuai tujuannya. "
    )
    
    image1 = "data/pic/item/gardu-kios.png"
    

class ItemTrafoDistribusi(Item):
    text1 = (
        "Transformator distribusi adalah suatu peralatan tenaga listrik yang berfungsi untuk menyalurkan "
        "tenaga/daya listrik dari tegangan tinggi ke tegangan rendah. Tujuan dari penggunaan transformator "
        "distribusi adalah untuk mengurangi tegangan utama dari sistem distribusi tenaga listrik menjadi "
        "tegangan untuk penggunaan konsumen. Penempatan transformator untuk instalasi gardu pasangan "
        "luar (outdoor) dipasang diatas tiang, dengan menggunakan satu tiang untuk gardu cantol dan dua "
        "tiang untuk gardu portal. Sedangkan penempatan transformator untuk instalasi pasangan dalam "
        "dipasang dibawah yang alasnya disemen dengan beton dalam sebuah ruangan tembok atau kios."
    )
    text2 = (
        " Transformator distribusi yang umum digunakan adalah transformator step down 20 kV/400 kV 3 phasa "
        "dan 1 phasa, dan ada juga yang menggunakan tiga buah transformator 1 phasa. Tegangan phasa ke "
        "phasa sistem jaringan tegangan rendah 380 Volt. Karena terjadi drop tegangan, maka pada tegangan "
        "rendahnya dibuat diatas 380 Volt agar tegangan pada ujung penerima tidak lebih kecil dari 380 Volt. "
        "Transformator distribusi dapat dibedakan menjadi dua jenis yaitu transformator 1 phasa dengan "
        "penggunaan 3 transformator 1 phasa identik dan transformator 3 phasa dengan penggunaan 1 "
        "transformator konstruksi 3 phasa. Sedangkan menurut karakteristiknya dibedakan menjadi tiga tipe "
        "yaitu, transformator konvensional, CSP, dan CSPB."
    )
    
    image1 = "data/pic/item/trafo-distribusi.jpg"
    

class ItemTrafoSatuFasa(Item):
    text1 = (
        "Transformator distribusi dirangkai dan dioperasikan dengan 3 transformator 1 phasa yang bertipe "
        "sama (identik). Keuntungan menggunakan transformator 3 x 1 phasa yaitu, kumparan primer dan "
        "sekunder dapat dibuat beberapa vektor grup sesuai dengan yang diinginkan, ketiga transformator "
        "tersebut dapat juga dioperasikan ke beban menjadi 1 phasa (dihubungkan paralel karena ketiga "
        "transformator tersebut identik), dan tegangan untuk ketiga phasanya, primer dan sekunder benar "
        "benar seimbang. Adapun kerugiannya yaitu, dengan daya yang sama untuk ketiga phasa, maka phasa "
        "untuk 3 x 1 phasa dibanding dengan 1 x 3 phasa lebih berat dan lebih mahal."
    )
    
    image1 = "data/pic/item/trafo-satu-fasa.jpg"
    

class ItemTrafoTigaFasa(Item):
    text1 = (
        "Karakteristik transformator 3 phasa yaitu, konstruksinya sudah dirancang permanen dari pabrik "
        "pembuatnya, dapat digunakan untuk mensuplai beban 1 phasa, maka tiap phasa maksimal beban yang "
        "dapat ditanggungnya hanya sepertiga dari daya tiga phasa. Transformator ini lebih ringan, "
        "sehingga lebih murah karena bahan materialnya lebih kecil tetapi keseimbangan tegangan antara "
        "ketiga phasanya, primer dan sekunder tidak terlalu simetris."
    )
    
    image1 = "data/pic/item/trafo-tiga-fasa.jpg"
    

class ItemTrafoKonvensional(Item):
    text1 = (
        "Transformator tipe ini tidak mempunyai peralatan pengaman terhadap sambaran petir ataupun "
        "perlindungan terhadap gangguan disebabkan beban lebih sebagai satu kesatuan dengan unit "
        "transformator. Peralatan pengaman seperti FCO dan LA tersebut dipasang secara terpisah. "
        "Untuk rating yang tidak terlalu besar, tipe ini adalah dalam bentuk pasangan tiang. Sedang "
        "untuk rating yang besar, ditempatkan pada gardu distribusi pasangan dalam."
    )
    
    image1 = "data/pic/item/trafo-konvensional-satu-fasa.jpg"
    image2 = "data/pic/item/trafo-konvensional-tiga-fasa.jpg"
    

class ItemTrafoCsp(Item):
    text1 = (
        "Transformator tipe ini mempunyai peralatan proteksi sendiri terhadap gangguan petir, "
        "gelombang surja, beban lebih, dan hubung singkat. Lightning arrester terpasang langsung "
        "pada tangki transformator sebagai proteksi terhadap petir. Untuk proteksi terhadap beban lebih, "
        "digunakan fuse yang dipasang di dalam tangki, fuse ini disebut weak link. Proteksi transformator "
        "terhadap gangguan internal menggunakan hubungan proteksi internal yang dipasang antara kumparan "
        "primer dengan bushing primer."
    )
    
    image1 = "data/pic/item/trafo-csp.jpg"
    