import json
from pathlib import Path

base = Path(__file__).parent
rows = [
    (
        "fasting-purpose",
        "Tujuan puasa",
        "Purpose of fasting",
        "Puasa melatih ketakwaan melalui ibadah yang dilakukan karena Allah dengan menahan diri pada waktu yang ditentukan.",
        "Fasting cultivates taqwa through worship for Allah by abstaining during the prescribed time.",
        [
            (
                "Tujuan puasa mencakup ketaatan, pengendalian diri, syukur, dan kepedulian.",
                "Purposes of fasting include obedience, self-restraint, gratitude, and care for others.",
            ),
            (
                "Hasil puasa tidak hanya diukur dari lapar dan haus, tetapi juga dari penjagaan perilaku.",
                "The fruits of fasting are not measured only by hunger and thirst, but also by guarded conduct.",
            ),
        ],
        ["source.quran-2-183"],
    ),
    (
        "fasting-conditions",
        "Syarat puasa",
        "Conditions of fasting",
        "Syarat wajib dan syarat sah puasa membantu membedakan siapa yang berkewajiban dan kapan ibadah dinilai sah.",
        "Conditions of obligation and validity help distinguish who is required to fast and when the worship is valid.",
        [
            (
                "Keislaman, kemampuan, kedewasaan, akal, dan keadaan khusus perlu dinilai menurut pembahasan yang tepat.",
                "Islam, ability, maturity, mental capacity, and special circumstances require proper assessment.",
            ),
            (
                "Sakit, perjalanan, kehamilan, menyusui, usia lanjut, serta menstruasi atau nifas memerlukan rincian individual.",
                "Illness, travel, pregnancy, nursing, old age, menstruation, and postnatal bleeding require individual detail.",
            ),
        ],
        ["source.quran-2-184", "source.quran-2-185"],
    ),
    (
        "fasting-pillars",
        "Rukun puasa",
        "Pillars of fasting",
        "Rukun puasa berpusat pada niat dan menahan diri dari hal yang membatalkan sejak fajar hingga matahari terbenam.",
        "The pillars of fasting center on intention and abstaining from invalidators from dawn until sunset.",
        [
            (
                "Pelajari waktu dan cara niat sesuai jenis puasa serta pendapat yang diikuti.",
                "Learn the timing and manner of intention for the type of fast and the position followed.",
            ),
            (
                "Rentang puasa dimulai pada fajar yang benar dan berakhir saat matahari terbenam.",
                "The fasting period begins at true dawn and ends at sunset.",
            ),
        ],
        ["source.quran-2-187", "source.bukhari-1"],
    ),
    (
        "fasting-invalidators",
        "Hal yang membatalkan puasa",
        "Invalidators of fasting",
        "Pembatal puasa harus dipelajari bersama unsur kesengajaan, pengetahuan, paksaan, lupa, dan keadaan medis.",
        "Invalidators of fasting should be learned together with intent, knowledge, coercion, forgetfulness, and medical circumstances.",
        [
            (
                "Makan, minum, dan hubungan seksual secara sengaja termasuk pembahasan utama pembatal puasa.",
                "Intentional eating, drinking, and sexual relations are central topics among fasting invalidators.",
            ),
            (
                "Jangan menetapkan batal atau kewajiban pengganti untuk kasus medis tanpa nasihat ahli yang tepat.",
                "Do not determine invalidity or compensation for medical cases without suitable expert advice.",
            ),
        ],
        ["source.quran-2-187"],
    ),
    (
        "suhur",
        "Suhur",
        "Suhur",
        "Suhur adalah makan atau minum sebelum fajar sebagai persiapan puasa, tanpa sengaja melewati batas waktu.",
        "Suhur is food or drink before dawn in preparation for fasting, without intentionally crossing the time boundary.",
        [
            (
                "Periksa waktu fajar pada jadwal tepercaya untuk tanggal dan lokasi setempat.",
                "Check dawn on a trusted schedule for the local date and location.",
            ),
            (
                "Pilih asupan yang wajar, hidrasi yang aman, dan jangan menjadikan suhur sebagai beban.",
                "Choose reasonable food, safe hydration, and do not make suhur burdensome.",
            ),
        ],
        ["source.quran-2-187"],
    ),
    (
        "iftar",
        "Berbuka puasa",
        "Breaking the fast",
        "Puasa diakhiri ketika matahari terbenam; berbuka dilakukan dengan syukur dan tanpa berlebihan.",
        "The fast ends at sunset; breaking it is done with gratitude and without excess.",
        [
            (
                "Pastikan matahari telah terbenam berdasarkan tanda atau jadwal tepercaya.",
                "Confirm sunset through observation or a trusted schedule.",
            ),
            (
                "Doa berbuka dan klaim keutamaannya harus memakai sumber yang telah diverifikasi.",
                "Breaking-fast supplications and claims about their merit must use verified sources.",
            ),
        ],
        ["source.quran-2-187"],
    ),
    (
        "ramadan",
        "Bulan Ramadan",
        "The month of Ramadan",
        "Ramadan adalah bulan puasa wajib dan kesempatan memperkuat ibadah, Al-Quran, kedermawanan, serta akhlak.",
        "Ramadan is the month of obligatory fasting and an opportunity to strengthen worship, Quran engagement, generosity, and character.",
        [
            (
                "Rencanakan ibadah dengan realistis sambil menjaga kesehatan, pekerjaan, keluarga, dan kewajiban lain.",
                "Plan worship realistically while caring for health, work, family, and other duties.",
            ),
            (
                "Malam dan hari Ramadan saling melengkapi dalam salat, membaca, doa, sedekah, dan istirahat.",
                "Ramadan nights and days complement each other through prayer, reading, supplication, charity, and rest.",
            ),
        ],
        ["source.quran-2-185"],
    ),
    (
        "voluntary-fasts",
        "Puasa sunah",
        "Voluntary fasts",
        "Puasa sunah menambah ibadah setelah kewajiban diperhatikan dan keadaan pribadi memungkinkan.",
        "Voluntary fasts add worship after obligations are addressed and personal circumstances allow.",
        [
            (
                "Pelajari hari yang dianjurkan, hari yang dilarang, dan niat untuk setiap jenis puasa.",
                "Learn recommended days, prohibited days, and intention for each kind of fast.",
            ),
            (
                "Jangan memaksakan puasa sunah bila membahayakan atau mengabaikan hak dan kewajiban.",
                "Do not force voluntary fasting when it causes harm or neglects rights and duties.",
            ),
        ],
        ["source.quran-2-184"],
    ),
    (
        "qada-fasting",
        "Qada puasa",
        "Making up missed fasts",
        "Qada mengganti hari puasa wajib yang terlewat ketika ketentuan mengharuskannya dan kemampuan telah kembali.",
        "Qada replaces missed obligatory fasting days when required and ability has returned.",
        [
            (
                "Catat jumlah hari dengan jujur, tetapi simpan catatan pribadi di aplikasi atau media milik pengguna.",
                "Record the number of days honestly, but keep personal records in user-owned storage.",
            ),
            (
                "Tentukan kewajiban qada berdasarkan sebab terlewatnya puasa dan nasihat yang dapat dipercaya.",
                "Determine qada obligations based on why the fast was missed and reliable advice.",
            ),
        ],
        ["source.quran-2-184", "source.quran-2-185"],
    ),
    (
        "fidyah",
        "Fidyah",
        "Fidyah",
        "Fidyah adalah bentuk kompensasi pada keadaan tertentu dan bukan pengganti umum untuk puasa yang mampu dilakukan.",
        "Fidyah is compensation in certain circumstances and not a general substitute for fasting one can perform.",
        [
            (
                "Penerapan, penerima, bentuk, dan besaran fidyah memerlukan rujukan hukum serta konteks setempat.",
                "Eligibility, recipients, form, and amount of fidyah require legal guidance and local context.",
            ),
            (
                "Kalkulator hanya membantu perkiraan; ia tidak menetapkan kewajiban pribadi.",
                "A calculator only assists estimation; it does not determine personal obligation.",
            ),
        ],
        ["source.quran-2-184"],
    ),
    (
        "zakat-purpose",
        "Tujuan zakat",
        "Purpose of zakat",
        "Zakat menyucikan harta dan jiwa, memenuhi kewajiban, serta menyalurkan hak kepada penerima yang ditetapkan.",
        "Zakat purifies wealth and the self, fulfills an obligation, and delivers rights to designated recipients.",
        [
            (
                "Bedakan zakat wajib dari sedekah sukarela.",
                "Distinguish obligatory zakat from voluntary charity.",
            ),
            (
                "Perhitungan dan penyaluran harus menjaga amanah, martabat penerima, dan ketepatan sasaran.",
                "Calculation and distribution should preserve trust, recipient dignity, and correct allocation.",
            ),
        ],
        ["source.quran-9-103"],
    ),
    (
        "zakat-fitrah",
        "Zakat fitrah",
        "Zakat al-fitr",
        "Zakat fitrah berkaitan dengan akhir Ramadan dan ditunaikan bagi pihak yang memenuhi kewajiban sebelum batas waktu yang berlaku.",
        "Zakat al-fitr is connected to the end of Ramadan and is paid by those obligated before the applicable deadline.",
        [
            (
                "Pelajari siapa yang wajib ditanggung, waktu pembayaran, bentuk, dan ukuran menurut panduan setempat.",
                "Learn who must be covered, payment time, form, and measure under local guidance.",
            ),
            (
                "Salurkan melalui penerima atau lembaga yang amanah sebelum batas yang ditetapkan.",
                "Distribute through eligible recipients or a trustworthy institution before the deadline.",
            ),
        ],
        ["source.quran-9-60"],
    ),
    (
        "zakat-mal",
        "Zakat mal",
        "Zakat on wealth",
        "Zakat mal mencakup kategori harta tertentu yang memenuhi syarat kepemilikan, nisab, dan masa kepemilikan bila berlaku.",
        "Zakat on wealth covers specified asset categories meeting ownership, nisab, and holding-period conditions where applicable.",
        [
            (
                "Pisahkan kategori seperti uang, perdagangan, emas, hasil pertanian, atau kategori lain sebelum menghitung.",
                "Separate categories such as cash, trade goods, gold, agricultural produce, or others before calculating.",
            ),
            (
                "Utang, aset campuran, valuasi, dan tanggal haul memerlukan panduan yang sesuai.",
                "Debts, mixed assets, valuation, and haul dates require appropriate guidance.",
            ),
        ],
        ["source.quran-2-267"],
    ),
    (
        "zakat-obligation",
        "Kewajiban zakat",
        "Zakat obligation",
        "Kewajiban zakat ditentukan oleh jenis harta, kepemilikan, nisab, haul bila berlaku, dan keadaan pemilik.",
        "Zakat obligation is determined by asset type, ownership, nisab, haul where applicable, and the owner's circumstances.",
        [
            (
                "Jangan menyimpulkan wajib hanya dari total kasar tanpa mengelompokkan harta.",
                "Do not infer obligation from a rough total without classifying assets.",
            ),
            (
                "Gunakan tanggal penilaian, harga acuan, dan metode yang konsisten serta dapat dijelaskan.",
                "Use a consistent, explainable valuation date, reference price, and method.",
            ),
        ],
        ["source.quran-2-267", "source.quran-9-103"],
    ),
    (
        "zakat-recipients",
        "Penerima zakat",
        "Zakat recipients",
        "Al-Quran menyebut delapan golongan penerima zakat dan penyaluran memerlukan penilaian yang amanah.",
        "The Quran names eight categories of zakat recipients, and distribution requires trustworthy assessment.",
        [
            (
                "Golongan penerima mencakup fakir, miskin, amil, muallaf, pembebasan, orang berutang, jalan Allah, dan musafir sesuai rincian hukum.",
                "Recipient categories include the poor, needy, administrators, those whose hearts are reconciled, emancipation, debtors, Allah's cause, and stranded travelers under legal details.",
            ),
            (
                "Jangan menilai kelayakan seseorang secara serampangan atau membuka data pribadinya.",
                "Do not judge someone's eligibility carelessly or expose private data.",
            ),
        ],
        ["source.quran-9-60"],
    ),
    (
        "zakat-calculator-guidance",
        "Panduan kalkulator zakat",
        "Zakat calculator guidance",
        "Kalkulator zakat memberi perkiraan non-otoritatif berdasarkan data dan asumsi yang dimasukkan pengguna.",
        "A zakat calculator provides a non-authoritative estimate based on user-entered data and assumptions.",
        [
            (
                "Periksa mata uang, harga acuan, nisab, tanggal, kategori aset, dan aturan pembulatan.",
                "Check currency, reference price, nisab, date, asset categories, and rounding rules.",
            ),
            (
                "Konfirmasikan hasil kepada ahli atau lembaga tepercaya; jangan mengirim data sensitif tanpa memahami privasinya.",
                "Confirm results with a trusted expert or institution; do not submit sensitive data without understanding privacy.",
            ),
        ],
        ["source.quran-2-267", "source.quran-9-103"],
    ),
    (
        "hajj-umrah-rulings",
        "Hukum Haji dan Umrah",
        "Hajj and Umrah rulings",
        "Haji wajib sekali bagi Muslim yang memenuhi kemampuan, sedangkan rincian hukum Umrah perlu dipelajari sesuai panduan yang diikuti.",
        "Hajj is obligatory once for Muslims who have the required ability, while detailed Umrah rulings should be learned under the guidance followed.",
        [
            (
                "Kemampuan mencakup aspek fisik, finansial, keamanan, perjalanan, dan tanggungan.",
                "Ability includes physical, financial, safety, travel, and dependent-care dimensions.",
            ),
            (
                "Bedakan rukun, wajib, sunah, larangan, serta konsekuensi agar tidak mencampur tingkat hukum.",
                "Distinguish pillars, obligations, recommendations, prohibitions, and consequences rather than mixing legal levels.",
            ),
        ],
        ["source.quran-3-97"],
    ),
    (
        "hajj-umrah-conditions",
        "Syarat Haji dan Umrah",
        "Conditions of Hajj and Umrah",
        "Syarat ibadah dan syarat kewajiban perlu diperiksa sebelum membuat keputusan perjalanan atau pembayaran.",
        "Conditions of worship and obligation should be checked before making travel or payment decisions.",
        [
            (
                "Tinjau identitas, kesehatan, kemampuan, pendampingan yang diperlukan, izin, dan aturan resmi terbaru.",
                "Review identity documents, health, ability, required support, permits, and current official rules.",
            ),
            (
                "Gunakan penyelenggara tepercaya dan jangan mengambil utang yang tidak terkelola demi perjalanan.",
                "Use a trustworthy organizer and do not take unmanaged debt for the journey.",
            ),
        ],
        ["source.quran-3-97"],
    ),
    (
        "ihram",
        "Ihram dan miqat",
        "Ihram and miqat",
        "Ihram adalah keadaan ritual yang dimulai dengan niat di miqat, bukan hanya pakaian yang dikenakan.",
        "Ihram is a ritual state begun with intention at the miqat, not merely the clothing worn.",
        [
            (
                "Pelajari lokasi atau waktu miqat yang sesuai dengan rute perjalanan.",
                "Learn the miqat location or time applicable to the travel route.",
            ),
            (
                "Persiapkan kebersihan, pakaian, niat, talbiyah, obat, dan kebutuhan aksesibilitas sebelum miqat.",
                "Prepare cleanliness, clothing, intention, talbiyah, medicine, and accessibility needs before the miqat.",
            ),
        ],
        ["source.quran-2-196"],
    ),
    (
        "ihram-prohibitions",
        "Larangan ihram",
        "Ihram prohibitions",
        "Larangan ihram berlaku setelah niat ihram dan memiliki rincian serta konsekuensi yang berbeda menurut perbuatan dan keadaan.",
        "Ihram prohibitions apply after entering ihram and have differing details and consequences according to the act and circumstances.",
        [
            (
                "Pelajari aturan rambut, kuku, wewangian, pakaian tertentu, perburuan, akad nikah, dan hubungan suami istri sebelum berangkat.",
                "Learn rules on hair, nails, fragrance, specified clothing, hunting, marriage contracts, and marital relations before departure.",
            ),
            (
                "Bila terjadi pelanggaran, jangan menetapkan dam sendiri tanpa menjelaskan kasus kepada pembimbing.",
                "If a violation occurs, do not determine compensation alone without explaining the case to a guide.",
            ),
        ],
        ["source.quran-2-197"],
    ),
    (
        "hajj-umrah-sequence",
        "Urutan Haji dan Umrah",
        "Hajj and Umrah sequence",
        "Urutan ritual harus dibedakan menurut jenis manasik dan jadwal resmi agar setiap tahap dilakukan pada tempat serta waktunya.",
        "The ritual sequence must be distinguished by pilgrimage type and official schedule so each stage occurs in its proper place and time.",
        [
            (
                "Umrah umumnya mencakup ihram, tawaf, sai, lalu tahallul dengan rincian yang perlu dipelajari.",
                "Umrah generally includes ihram, tawaf, sai, then release from ihram, with details to be learned.",
            ),
            (
                "Haji menambahkan rangkaian hari dan tempat seperti Arafah, Muzdalifah, Mina, dan ritual lain sesuai jenis manasik.",
                "Hajj adds days and places such as Arafah, Muzdalifah, Mina, and other rites according to pilgrimage type.",
            ),
        ],
        ["source.quran-2-196", "source.quran-2-197"],
    ),
    (
        "hajj-umrah-prayers",
        "Doa dalam Haji dan Umrah",
        "Prayers during Hajj and Umrah",
        "Doa yang memiliki sumber khusus dibedakan dari doa pribadi yang boleh dipanjatkan dengan makna baik.",
        "Supplications with specific evidence are distinguished from personal prayers that may be made with good meanings.",
        [
            (
                "Talbiyah dan doa yang bersumber perlu dipelajari dengan teks serta konteks yang terverifikasi.",
                "Talbiyah and sourced supplications should be learned with verified wording and context.",
            ),
            (
                "Tidak setiap putaran atau tempat memiliki doa khusus; hindari menetapkan bacaan tanpa sumber.",
                "Not every circuit or place has a specific supplication; avoid assigning words without evidence.",
            ),
        ],
        ["source.quran-2-201"],
    ),
    (
        "hajj-umrah-travel",
        "Panduan perjalanan Haji dan Umrah",
        "Hajj and Umrah travel guidance",
        "Perjalanan ibadah memerlukan persiapan dokumen, kesehatan, keselamatan, dana, komunikasi, dan kepedulian kepada jamaah lain.",
        "Pilgrimage travel requires preparation of documents, health, safety, funds, communication, and care for fellow pilgrims.",
        [
            (
                "Simpan salinan dokumen, kontak rombongan, obat, identitas medis, dan rencana pertemuan bila terpisah.",
                "Keep document copies, group contacts, medicine, medical identification, and a reunion plan if separated.",
            ),
            (
                "Ikuti petugas resmi, jaga hidrasi dan energi, hindari desakan kerumunan, serta gunakan penyesuaian yang dibutuhkan.",
                "Follow officials, manage hydration and energy, avoid crowd pressure, and use needed accommodations.",
            ),
        ],
        ["source.quran-3-97"],
    ),
]
review = {
    "content": {"outcome": "pending"},
    "locales": {"id": {"outcome": "pending"}, "en": {"outcome": "pending"}},
}
practice_links = {
    "fasting-purpose": "fasting-day-plan",
    "qada-fasting": "qada-fidyah-planning",
    "fidyah": "qada-fidyah-planning",
    "zakat-obligation": "zakat-obligation-check",
    "zakat-calculator-guidance": "zakat-estimate",
    "ihram": "ihram-readiness",
    "hajj-umrah-sequence": "hajj-umrah-sequence",
    "hajj-umrah-travel": "hajj-umrah-travel",
}
for i, (slug, title_id, title_en, summary_id, summary_en, points, sources) in enumerate(
    rows, 1
):
    previous = "voluntary-prayer" if i == 1 else rows[i - 2][0]
    next_ids = [] if i == len(rows) else [f"lesson.{rows[i][0]}"]
    if i <= 10:
        group, tags = "fasting", ["season.ramadan"]
    elif i <= 16:
        group = "zakat"
        tags = (
            ["season.ramadan", "season.eid-al-fitr"]
            if slug == "zakat-fitrah"
            else ["season.ramadan"]
        )
    else:
        group, tags = "hajj-umrah", ["season.hajj"]
    features = []
    if slug in {"suhur", "iftar", "ramadan", "voluntary-fasts", "qada-fasting"}:
        features.append(
            {
                "featureId": "feature.reminders",
                "required": False,
                "parameters": {"topic": slug},
            }
        )
    if slug in {"suhur", "iftar"}:
        features.extend(
            [
                {"featureId": "feature.prayer-schedule", "required": False},
                {
                    "featureId": "feature.location",
                    "required": False,
                    "parameters": {"purpose": "fasting-times"},
                },
            ]
        )
    if slug in {"fidyah", "zakat-calculator-guidance"}:
        features.append(
            {
                "featureId": "feature.calculator",
                "required": False,
                "parameters": {
                    "calculatorType": "fidyah" if slug == "fidyah" else "zakat"
                },
            }
        )
    if slug in {
        "hajj-umrah-conditions",
        "ihram",
        "hajj-umrah-sequence",
        "hajj-umrah-travel",
    }:
        features.append(
            {
                "featureId": "feature.location",
                "required": False,
                "parameters": {"purpose": "hajj-umrah"},
            }
        )
    related = [f"practice.{practice_links[slug]}"] if slug in practice_links else []
    document = {
        "schemaVersion": "2.0",
        "id": f"lesson.{slug}",
        "type": "lesson",
        "slug": slug,
        "title": {"id": title_id, "en": title_en},
        "summary": {"id": summary_id, "en": summary_en},
        "status": "draft",
        "stageId": "stage.pillars-journey",
        "stageOrder": i,
        "group": group,
        "relationships": {
            "prerequisites": [f"lesson.{previous}"],
            "next": next_ids,
            "related": related,
        },
        "featureLinks": features,
        "sourceIds": sources,
        "review": review,
        "seasonalTags": tags,
        "blocks": [
            {
                "id": f"block.{slug}.overview",
                "type": "paragraph",
                "text": {"id": summary_id, "en": summary_en},
            },
            {
                "id": f"block.{slug}.key-points",
                "type": "unordered-list",
                "items": [
                    {"id": f"item.{slug}.{j}", "text": {"id": point[0], "en": point[1]}}
                    for j, point in enumerate(points, 1)
                ],
            },
            {
                "id": f"block.{slug}.review-note",
                "type": "callout",
                "kind": "important",
                "body": {
                    "id": "Materi ini berstatus draf dan menunggu telaah isi serta bahasa. Keadaan pribadi memerlukan nasihat dari pembimbing atau ahli yang sesuai.",
                    "en": "This material is a draft awaiting content and language review. Personal circumstances require advice from an appropriate instructor or expert.",
                },
            },
            {
                "id": f"block.{slug}.sources",
                "type": "source-reference",
                "sourceIds": sources,
            },
        ],
        "completionPrompt": {
            "type": "acknowledgement",
            "label": {
                "id": "Saya memahami pokok bahasan, batas panduan, dan status drafnya.",
                "en": "I understand the key topic, guidance limits, and draft status.",
            },
        },
    }
    (base / f"{slug}.json").write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
