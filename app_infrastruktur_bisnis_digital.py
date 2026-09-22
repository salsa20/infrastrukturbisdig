
import streamlit as st

st.set_page_config(
    page_title="Pertemuan 6 | Infrastruktur Bisnis Digital",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}
.hero {
    padding: 2rem;
    border-radius: 22px;
    background: linear-gradient(135deg, #f6f8ff 0%, #eefaf7 100%);
    border: 1px solid rgba(120,120,120,.18);
    margin-bottom: 1.2rem;
}
.hero h1 {
    margin: 0 0 .4rem 0;
    font-size: 2.35rem;
}
.hero p {
    font-size: 1.05rem;
    margin: 0;
    opacity: .82;
}
.card {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    background: rgba(255,255,255,.65);
}
.small-card {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 16px;
    padding: 1rem;
    min-height: 120px;
}
.flow {
    border-radius: 16px;
    padding: 1rem 1.1rem;
    background: rgba(120,120,120,.06);
    border: 1px dashed rgba(120,120,120,.35);
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    line-height: 1.75;
}
.badge {
    display: inline-block;
    padding: .28rem .7rem;
    border-radius: 999px;
    border: 1px solid rgba(120,120,120,.25);
    margin: .15rem .2rem .15rem 0;
    font-size: .86rem;
}
.note {
    padding: 1rem 1.1rem;
    border-left: 5px solid #6c63ff;
    background: rgba(108,99,255,.08);
    border-radius: 12px;
}
.quiz-box {
    border: 1px solid rgba(120,120,120,.22);
    border-radius: 18px;
    padding: 1.15rem;
    margin-bottom: 1rem;
}
div[data-testid="stMetric"] {
    border: 1px solid rgba(120,120,120,.16);
    padding: .8rem;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Data
# -----------------------------
quiz = [
    {
        "q": "Manakah yang paling tepat menggambarkan infrastruktur bisnis digital?",
        "options": [
            "Strategi perusahaan untuk menaikkan harga produk",
            "Kumpulan teknologi yang mendukung operasional bisnis digital",
            "Teknik membuat konten media sosial",
            "Metode promosi menggunakan influencer",
        ],
        "answer": 1,
        "explanation": "Infrastruktur bisnis digital mencakup teknologi seperti hardware, jaringan, aplikasi, server/cloud, database, integrasi, dan keamanan yang mendukung proses bisnis digital.",
    },
    {
        "q": "Komponen yang paling tepat digunakan untuk menyimpan data transaksi pelanggan adalah...",
        "options": ["Router", "Database", "Browser", "Keyboard"],
        "answer": 1,
        "explanation": "Database digunakan untuk menyimpan data secara terstruktur, misalnya pelanggan, produk, transaksi, dan stok.",
    },
    {
        "q": "Jaringan internal yang digunakan oleh anggota organisasi disebut...",
        "options": ["Internet", "Marketplace", "Intranet", "Extranet"],
        "answer": 2,
        "explanation": "Intranet digunakan untuk kebutuhan internal organisasi, misalnya portal karyawan, SOP, absensi, atau pengajuan cuti.",
    },
    {
        "q": "Kemampuan sistem untuk menyesuaikan kapasitas ketika jumlah pengguna meningkat disebut...",
        "options": ["Scalability", "Branding", "Promotion", "Authentication"],
        "answer": 0,
        "explanation": "Scalability adalah kemampuan sistem menyesuaikan kapasitas ketika beban pengguna atau transaksi meningkat.",
    },
    {
        "q": "Teknologi yang memungkinkan satu aplikasi berkomunikasi dengan aplikasi lain disebut...",
        "options": ["CPU", "Monitor", "API", "Keyboard"],
        "answer": 2,
        "explanation": "API (Application Programming Interface) memungkinkan sistem yang berbeda saling bertukar data dan layanan.",
    },
    {
        "q": "Tujuan utama backup dalam infrastruktur digital adalah...",
        "options": [
            "Mempercepat koneksi internet",
            "Menyediakan salinan data jika data utama hilang atau rusak",
            "Memperindah tampilan aplikasi",
            "Meningkatkan jumlah pelanggan",
        ],
        "answer": 1,
        "explanation": "Backup menyediakan salinan data yang dapat digunakan ketika data utama hilang, rusak, atau terganggu.",
    },
    {
        "q": "Portal perusahaan yang dapat diakses supplier tertentu merupakan contoh...",
        "options": ["Internet publik", "Intranet", "Extranet", "Social media"],
        "answer": 2,
        "explanation": "Extranet memberikan akses terbatas kepada pihak eksternal tertentu seperti supplier atau mitra.",
    },
    {
        "q": "Jika website menjadi sangat lambat saat flash sale, aspek infrastruktur yang paling relevan untuk dianalisis adalah...",
        "options": ["Logo perusahaan", "Scalability dan performance", "Nama merek", "Desain kemasan"],
        "answer": 1,
        "explanation": "Lonjakan pengguna memengaruhi kapasitas dan performa sistem, sehingga scalability dan performance menjadi perhatian utama.",
    },
    {
        "q": "Manakah contoh fungsi server yang paling tepat?",
        "options": [
            "Menjalankan aplikasi dan memproses permintaan pengguna",
            "Mencetak struk secara manual",
            "Mengganti strategi pemasaran",
            "Mendesain logo perusahaan",
        ],
        "answer": 0,
        "explanation": "Server dapat menjalankan aplikasi, memproses permintaan, menyimpan file, dan mengakses database.",
    },
    {
        "q": "Manakah langkah keamanan yang paling sesuai untuk membatasi siapa yang boleh mengakses data tertentu?",
        "options": ["Access control", "Diskon", "Promosi", "Rebranding"],
        "answer": 0,
        "explanation": "Access control mengatur siapa yang memiliki hak untuk mengakses data atau fungsi tertentu.",
    },
]

flows = {
    "Coffee Shop Digital": {
        "case": (
            "Coffee shop mengalami antrean panjang pada jam sibuk. Pelanggan ingin bisa melihat menu, "
            "memesan, dan membayar melalui QR tanpa harus mengantre lama di kasir."
        ),
        "steps": [
            "Pelanggan", "QR Menu / Mobile Web", "Internet", "Cloud / Server",
            "Database", "Payment API / POS / Inventory", "Kitchen / Barista", "Pelanggan"
        ],
        "focus": "Integrasi order, pembayaran, POS, stok, dan proses pembuatan minuman."
    },
    "Laundry Digital": {
        "case": (
            "Laundry ingin menyediakan layanan pickup dan delivery. Pelanggan juga ingin mengetahui "
            "status cucian secara online, mulai dari dijemput, dicuci, disetrika, hingga dikirim kembali."
        ),
        "steps": [
            "Pelanggan", "Mobile App / Website", "Internet", "Cloud / Server",
            "Database", "Payment / Pickup / Delivery API", "Laundry Process", "Pelanggan"
        ],
        "focus": "Tracking status, pembayaran digital, dan integrasi pickup-delivery."
    },
    "Marketplace / Toko Online": {
        "case": (
            "Bisnis fashion yang awalnya hanya memiliki toko fisik ingin menjual produk secara nasional. "
            "Sistem harus menangani pencarian produk, checkout, pembayaran, stok, dan pengiriman."
        ),
        "steps": [
            "Customer", "Website / Mobile App", "Internet", "Cloud / Server",
            "Database", "Payment / Inventory / Logistics API", "Warehouse / Fulfillment", "Customer"
        ],
        "focus": "Sinkronisasi stok, pembayaran, warehouse, dan logistik."
    },
    "Kursus Online": {
        "case": (
            "Lembaga kursus ingin mengubah kelas tatap muka menjadi platform digital. Mahasiswa dapat "
            "mendaftar, membayar, menonton materi, mengerjakan kuis, melihat progres, dan memperoleh sertifikat."
        ),
        "steps": [
            "Student", "Learning App / Website", "Internet", "Cloud / Server",
            "Database", "Payment / Video / Learning System", "Learning Process", "Student"
        ],
        "focus": "Autentikasi, penyimpanan materi, progres belajar, pembayaran, dan sertifikat."
    },
    "Restoran Digital": {
        "case": (
            "Restoran menerima pesanan dari dine-in, website, dan layanan delivery. Masalah muncul ketika "
            "stok, pembayaran, dan order dapur tidak sinkron."
        ),
        "steps": [
            "Customer", "Website / App / QR Menu", "Internet", "Cloud / Server",
            "Database", "Payment / POS / Inventory", "Kitchen / Delivery", "Customer"
        ],
        "focus": "Integrasi order, POS, inventory, kitchen, payment, dan delivery."
    },
}

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Pertemuan 6")
st.sidebar.caption("Pengantar Bisnis Digital")

menu = st.sidebar.radio(
    "Navigasi",
    [
        "🏠 Beranda",
        "📘 Materi",
        "🔗 Simulasi Infrastruktur",
        "🧭 5 Contoh Alur",
        "🧩 Latihan",
        "🏆 Kuis 10 Soal",
        "✅ Ringkasan",
    ],
)

st.sidebar.divider()
st.sidebar.markdown("**Sub-CPMK**")
st.sidebar.write("Mahasiswa mampu memahami Infrastruktur Bisnis Digital.")
st.sidebar.markdown("**Referensi RPS**")
st.sidebar.write("Dave Chaffey — Digital Business and e-Commerce.")
st.sidebar.caption("Materi dikembangkan dari topik RPS agar lebih mudah dipahami mahasiswa.")

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🌐 Infrastruktur Bisnis Digital</h1>
    <p>Memahami teknologi yang membuat sebuah bisnis digital dapat beroperasi, terhubung, aman, dan berkembang.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# BERANDA
# -----------------------------
if menu == "🏠 Beranda":
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="small-card">
        <b>🎯 Fokus</b><br><br>
        Memahami komponen dan alur infrastruktur bisnis digital.
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="small-card">
        <b>🧠 Metode</b><br><br>
        Materi ringkas, 5 contoh alur bisnis, simulasi, latihan, dan kuis.
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="small-card">
        <b>📚 Hasil Akhir</b><br><br>
        Mahasiswa mampu menganalisis kebutuhan infrastruktur bisnis sederhana.
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Tujuan Pembelajaran")
    st.markdown("""
    Setelah mengikuti pertemuan ini, mahasiswa diharapkan mampu:
    1. Menjelaskan pengertian infrastruktur bisnis digital.
    2. Mengidentifikasi hardware, jaringan, software, server/cloud, database, integrasi, dan keamanan.
    3. Membedakan internet, intranet, dan extranet.
    4. Menjelaskan peran cloud computing, API, backup, dan access control.
    5. Menganalisis masalah sederhana seperti website lambat, gagal transaksi, atau lonjakan pengguna.
    """)

    st.markdown("""
    <div class="note">
    <b>Analogi sederhana:</b> jika toko fisik membutuhkan gedung, rak, kasir, gudang, dan listrik,
    maka bisnis digital membutuhkan perangkat, jaringan, aplikasi, server, database, integrasi, dan keamanan.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# MATERI
# -----------------------------
elif menu == "📘 Materi":
    tabs = st.tabs([
        "Konsep Dasar",
        "Komponen",
        "Jaringan",
        "Cloud & Server",
        "Database & API",
        "Security",
        "Kualitas Infrastruktur",
    ])

    with tabs[0]:
        st.subheader("1. Pengertian Infrastruktur Bisnis Digital")
        st.write(
            "Infrastruktur bisnis digital adalah kumpulan teknologi yang mendukung aktivitas bisnis "
            "agar dapat berjalan secara digital, mulai dari komunikasi, transaksi, penyimpanan data, "
            "pembayaran, hingga integrasi dengan pihak lain."
        )
        st.markdown(
            '<span class="badge">Perangkat</span>'
            '<span class="badge">Jaringan</span>'
            '<span class="badge">Aplikasi</span>'
            '<span class="badge">Server / Cloud</span>'
            '<span class="badge">Database</span>'
            '<span class="badge">API</span>'
            '<span class="badge">Security</span>',
            unsafe_allow_html=True,
        )
        st.markdown("### Contoh")
        st.write(
            "Ketika pelanggan membeli produk di toko online, proses sederhana seperti klik–bayar–kirim "
            "sebenarnya melibatkan banyak komponen teknologi yang bekerja bersama."
        )

    with tabs[1]:
        st.subheader("2. Komponen Utama")
        data = {
            "Komponen": [
                "Hardware", "Network", "Software", "Server / Cloud",
                "Database", "Integration", "Security"
            ],
            "Fungsi": [
                "Perangkat fisik",
                "Menghubungkan perangkat",
                "Menjalankan proses bisnis",
                "Menjalankan aplikasi dan komputasi",
                "Menyimpan data",
                "Menghubungkan beberapa sistem",
                "Melindungi sistem dan data",
            ],
            "Contoh": [
                "Laptop, smartphone, server",
                "Internet, Wi-Fi, LAN",
                "Website, aplikasi, ERP",
                "Cloud server",
                "Data pelanggan dan transaksi",
                "API",
                "Password, firewall, enkripsi",
            ],
        }
        st.dataframe(data, use_container_width=True, hide_index=True)

        st.markdown("### Contoh alur kasir digital")
        st.markdown("""
        <div class="flow">
        Barcode Scanner → Komputer Kasir → Database Stok → Transaksi Tercatat → Stok Berkurang
        </div>
        """, unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("3. Internet, Intranet, dan Extranet")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("### 🌍 Internet")
            st.write("Jaringan publik yang dapat digunakan masyarakat luas.")
            st.caption("Contoh: website publik, marketplace, media sosial.")
        with c2:
            st.markdown("### 🏢 Intranet")
            st.write("Jaringan atau portal untuk kebutuhan internal organisasi.")
            st.caption("Contoh: portal HR, absensi, SOP internal.")
        with c3:
            st.markdown("### 🤝 Extranet")
            st.write("Akses terbatas yang diberikan kepada pihak eksternal tertentu.")
            st.caption("Contoh: portal supplier atau mitra.")

        st.info("Cara cepat mengingat: Internet = umum, Intranet = internal, Extranet = internal + pihak tertentu.")

    with tabs[3]:
        st.subheader("4. Server dan Cloud Computing")
        st.write(
            "Server adalah sistem yang menyediakan layanan kepada perangkat lain, misalnya menjalankan "
            "website, aplikasi, pemrosesan transaksi, atau akses ke database."
        )
        st.markdown("""
        <div class="flow">
        Smartphone → Internet → Server → Aplikasi / Database → Respons kembali ke pengguna
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Cloud Computing")
        st.write(
            "Cloud computing memungkinkan bisnis menggunakan sumber daya komputasi melalui internet "
            "tanpa harus memiliki seluruh infrastruktur fisik sendiri."
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Server sendiri**")
            st.write("Perusahaan membeli dan mengelola perangkat fisik sendiri.")
        with col2:
            st.markdown("**Cloud**")
            st.write("Perusahaan menggunakan sumber daya komputasi sesuai kebutuhan.")

        st.markdown("### Scalability")
        st.write(
            "Scalability adalah kemampuan sistem menyesuaikan kapasitas ketika jumlah pengguna atau transaksi bertambah."
        )

    with tabs[4]:
        st.subheader("5. Database dan Integrasi Sistem")
        st.write(
            "Database menyimpan data secara terstruktur seperti pelanggan, produk, stok, pembayaran, dan transaksi."
        )

        st.markdown("""
        <div class="flow">
        Pelanggan → Website / App → Server → Database → Payment → Inventory → Logistics
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### API")
        st.write(
            "API (Application Programming Interface) memungkinkan satu aplikasi berkomunikasi dengan aplikasi lainnya."
        )
        st.markdown("""
        <div class="flow">
        Website Toko → API → Payment Gateway → Bank / E-Wallet
        </div>
        """, unsafe_allow_html=True)

    with tabs[5]:
        st.subheader("6. Keamanan Infrastruktur Digital")
        st.write("Risiko yang dapat muncul antara lain:")
        st.markdown("""
        - Pencurian password
        - Kebocoran data
        - Malware
        - Akses tanpa izin
        - Kehilangan data
        """)

        st.write("Beberapa bentuk perlindungan:")
        st.markdown("""
        - Password yang kuat
        - Authentication
        - Access control
        - Firewall
        - Encryption
        - Backup
        """)

        st.markdown("### Backup dan Recovery")
        st.write(
            "**Backup** adalah membuat salinan data. **Recovery** adalah proses memulihkan sistem atau data "
            "setelah terjadi gangguan."
        )

    with tabs[6]:
        st.subheader("7. Karakteristik Infrastruktur yang Baik")
        metrics = [
            ("Availability", "Sistem tersedia ketika dibutuhkan."),
            ("Performance", "Sistem memberikan respons dengan cepat."),
            ("Scalability", "Kapasitas dapat menyesuaikan pertumbuhan."),
            ("Security", "Data dan transaksi terlindungi."),
            ("Reliability", "Sistem berjalan stabil dan konsisten."),
            ("Integration", "Sistem dapat terhubung dengan sistem lainnya."),
        ]
        for i in range(0, len(metrics), 2):
            c1, c2 = st.columns(2)
            for col, item in zip([c1, c2], metrics[i:i+2]):
                with col:
                    st.markdown(f"""
                    <div class="card">
                    <b>{item[0]}</b><br>{item[1]}
                    </div>
                    """, unsafe_allow_html=True)

# -----------------------------
# SIMULASI
# -----------------------------
elif menu == "🔗 Simulasi Infrastruktur":
    st.subheader("Simulasi Alur Infrastruktur")
    business = st.selectbox("Pilih jenis bisnis", list(flows.keys()))
    selected = flows[business]
    steps = selected["steps"]

    st.write(f"**Kasus:** {selected['case']}")
    st.write(f"Contoh alur sederhana untuk **{business}**:")
    st.markdown(
        '<div class="flow">' + " → ".join(steps) + '</div>',
        unsafe_allow_html=True
    )
    st.caption(f"Fokus infrastruktur: {selected['focus']}")

    st.markdown("### Coba analisis")
    problem = st.selectbox(
        "Pilih situasi",
        [
            "Pengguna meningkat 10 kali lipat",
            "Database tidak dapat diakses",
            "Payment gagal terhubung",
            "Data pelanggan bocor",
            "Internet kantor terputus",
        ]
    )

    if problem == "Pengguna meningkat 10 kali lipat":
        st.success("Fokus analisis: scalability, kapasitas server/cloud, database, dan performance.")
    elif problem == "Database tidak dapat diakses":
        st.warning("Dampak: aplikasi bisa gagal membaca stok, pelanggan, transaksi, atau status order.")
    elif problem == "Payment gagal terhubung":
        st.warning("Fokus analisis: integrasi/API antara sistem bisnis dengan payment gateway.")
    elif problem == "Data pelanggan bocor":
        st.error("Fokus analisis: security, access control, authentication, encryption, dan prosedur perlindungan data.")
    else:
        st.info("Fokus analisis: network availability dan konektivitas antara perangkat, aplikasi, dan layanan online.")

# -----------------------------
# 5 CONTOH ALUR
# -----------------------------
elif menu == "🧭 5 Contoh Alur":
    st.subheader("5 Contoh Alur Infrastruktur Bisnis Digital")
    st.write(
        "Walaupun jenis bisnis berbeda, pola infrastrukturnya umumnya mirip. "
        "Perbedaannya terutama terletak pada aplikasi, integrasi, dan proses bisnis akhirnya."
    )

    st.markdown("### Pola umum")
    st.markdown("""
    <div class="flow">
    Customer / User → Application → Internet → Cloud / Server → Database → Integration / API → Business Process → Customer / User
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Cara membacanya: pengguna berinteraksi melalui aplikasi, terhubung lewat internet, "
        "permintaan diproses di server/cloud, data disimpan di database, lalu sistem terhubung "
        "dengan layanan lain melalui integrasi/API sebelum proses bisnis dijalankan."
    )

    for i, (name, info) in enumerate(flows.items(), start=1):
        with st.expander(f"{i}. {name}", expanded=(i == 1)):
            st.markdown("**Gambaran kasus**")
            st.write(info["case"])

            st.markdown("**Alur infrastruktur digital**")
            st.markdown(
                '<div class="flow">' + " → ".join(info["steps"]) + '</div>',
                unsafe_allow_html=True
            )

            st.markdown("**Fokus yang perlu diperhatikan**")
            st.write(info["focus"])

            if name == "Coffee Shop Digital":
                st.caption(
                    "Contoh: setelah pelanggan memesan dan membayar, transaksi masuk ke POS, "
                    "stok dapat diperbarui, dan barista menerima order."
                )
            elif name == "Laundry Digital":
                st.caption(
                    "Contoh: status laundry diperbarui di sistem sehingga pelanggan bisa melihat "
                    "apakah cucian sedang diproses, selesai, atau dalam pengiriman."
                )
            elif name == "Marketplace / Toko Online":
                st.caption(
                    "Contoh: pembayaran yang berhasil memicu pengurangan stok dan proses fulfillment, "
                    "kemudian data pengiriman diteruskan ke layanan logistik."
                )
            elif name == "Kursus Online":
                st.caption(
                    "Contoh: setelah pembayaran berhasil, akses kelas dibuka dan progres belajar "
                    "disimpan di database sampai sertifikat diterbitkan."
                )
            elif name == "Restoran Digital":
                st.caption(
                    "Contoh: order yang masuk harus sinkron dengan POS, inventory, dapur, dan delivery "
                    "agar tidak terjadi pesanan ganda atau stok yang tidak sesuai."
                )

    st.divider()
    st.markdown("### Apa yang sama dari kelima kasus?")
    st.markdown("""
    - Semua memiliki **user/customer** sebagai titik awal.
    - Semua membutuhkan **application** sebagai media interaksi.
    - Semua bergantung pada **network/internet**.
    - Semua membutuhkan **server/cloud** untuk menjalankan proses.
    - Semua menyimpan data di **database**.
    - Semua membutuhkan **integrasi** dengan sistem lain.
    - Semua berakhir pada **proses bisnis nyata** yang memberi value kepada pengguna.
    """)

# -----------------------------
# LATIHAN
# -----------------------------
elif menu == "🧩 Latihan":
    st.subheader("Latihan Studi Kasus")

    with st.expander("Kasus 1 — Flash Sale Marketplace", expanded=True):
        st.write(
            "Sebuah marketplace biasanya melayani 20.000 pengguna aktif. Saat flash sale, jumlah pengguna "
            "meningkat menjadi 500.000 secara bersamaan. Website menjadi lambat dan beberapa pelanggan gagal checkout."
        )
        ans1 = st.text_area(
            "Identifikasi minimal tiga kemungkinan masalah infrastruktur.",
            key="lat1",
            height=120
        )
        if st.button("Lihat panduan jawaban Kasus 1"):
            st.info(
                "Panduan: kapasitas server/cloud, scalability, performa database, jaringan, aplikasi, "
                "integrasi payment, atau bottleneck pada proses checkout."
            )

    with st.expander("Kasus 2 — Laundry Digital"):
        st.write(
            "Sebuah laundry ingin memiliki aplikasi untuk pemesanan, penjemputan, pembayaran, "
            "tracking status, dan notifikasi."
        )
        ans2 = st.text_area(
            "Susun alur infrastrukturnya dari pelanggan hingga layanan selesai.",
            key="lat2",
            height=120
        )
        if st.button("Lihat panduan jawaban Kasus 2"):
            st.info(
                "Contoh: Pelanggan → Aplikasi → Internet → Server/Cloud → Database → Payment → "
                "Pickup/Delivery → Status Laundry → Notifikasi."
            )

    with st.expander("Kasus 3 — Restoran Digital"):
        st.write(
            "Restoran memiliki aplikasi pemesanan, kasir, database pelanggan, sistem stok, pembayaran, dan delivery."
        )
        ans3 = st.text_area(
            "Apa masalah yang terjadi jika sistem pembayaran tidak terintegrasi dengan sistem order?",
            key="lat3",
            height=120
        )
        if st.button("Lihat panduan jawaban Kasus 3"):
            st.info(
                "Kemungkinan terjadi pengecekan pembayaran manual, keterlambatan order, kesalahan status pembayaran, "
                "serta proses operasional menjadi kurang efisien."
            )

    st.divider()
    st.subheader("Tugas Kelompok")
    st.write(
        "Pilih satu bisnis: toko online, coffee shop, laundry, restoran, travel, jasa fotografi, atau kursus online."
    )
    st.markdown("""
    Rancang infrastrukturnya dan jelaskan:
    1. Aplikasi apa yang digunakan.
    2. Data apa yang disimpan.
    3. Bagaimana pelanggan membayar.
    4. Bagaimana sistem saling terhubung.
    5. Risiko keamanan yang mungkin muncul.
    6. Apa yang terjadi jika pengguna meningkat 10 kali lipat.
    """)

# -----------------------------
# QUIZ
# -----------------------------
elif menu == "🏆 Kuis 10 Soal":
    st.subheader("Kuis Infrastruktur Bisnis Digital")
    st.caption("Pilih satu jawaban pada setiap soal. Klik tombol Periksa Jawaban setelah selesai.")

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    for i, item in enumerate(quiz):
        st.markdown(f'<div class="quiz-box"><b>Soal {i+1}.</b> {item["q"]}</div>', unsafe_allow_html=True)
        st.radio(
            "Pilih jawaban:",
            item["options"],
            key=f"q_{i}",
            index=None,
            label_visibility="collapsed",
        )
        if st.session_state.quiz_submitted:
            selected = st.session_state.get(f"q_{i}")
            if selected is None:
                st.warning("Belum dijawab.")
            else:
                idx = item["options"].index(selected)
                if idx == item["answer"]:
                    st.success("Jawaban benar.")
                else:
                    st.error(f"Jawaban yang tepat: {item['options'][item['answer']]}")
                st.caption(item["explanation"])
        st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✅ Periksa Jawaban", use_container_width=True):
            st.session_state.quiz_submitted = True
            st.rerun()
    with col2:
        if st.button("🔄 Ulangi Kuis", use_container_width=True):
            for i in range(len(quiz)):
                st.session_state.pop(f"q_{i}", None)
            st.session_state.quiz_submitted = False
            st.rerun()

    if st.session_state.quiz_submitted:
        score = 0
        answered = 0
        for i, item in enumerate(quiz):
            selected = st.session_state.get(f"q_{i}")
            if selected is not None:
                answered += 1
                if item["options"].index(selected) == item["answer"]:
                    score += 1

        st.subheader("Hasil Kuis")
        c1, c2, c3 = st.columns(3)
        c1.metric("Skor", f"{score}/10")
        c2.metric("Nilai", f"{score*10}")
        c3.metric("Terjawab", f"{answered}/10")

        if score >= 8:
            st.success("Sangat baik. Pemahaman materi sudah kuat.")
        elif score >= 6:
            st.info("Cukup baik. Review kembali bagian yang masih salah.")
        else:
            st.warning("Perlu review materi sebelum mencoba kuis kembali.")

# -----------------------------
# RINGKASAN
# -----------------------------
elif menu == "✅ Ringkasan":
    st.subheader("Ringkasan Pertemuan")

    st.markdown("""
    **Inti materi yang perlu diingat:**

    - Infrastruktur bisnis digital adalah teknologi yang membuat proses bisnis digital dapat berjalan.
    - Komponen utamanya: **hardware, network, software, server/cloud, database, integration, security**.
    - **Internet** digunakan secara umum, **intranet** untuk internal, dan **extranet** untuk pihak eksternal tertentu.
    - **Cloud** membantu bisnis menggunakan sumber daya komputasi secara fleksibel.
    - **Database** menyimpan data bisnis secara terstruktur.
    - **API** menghubungkan satu sistem dengan sistem lain.
    - **Backup, recovery, access control, authentication, firewall, dan encryption** mendukung keamanan.
    - Infrastruktur yang baik mempertimbangkan **availability, performance, scalability, security, reliability, dan integration**.
    """)

    st.markdown("""
    <div class="flow">
    Device → Network → Application → Server / Cloud → Database → Integration → Business Service
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="note">
    <b>Pesan utama:</b> pelanggan hanya melihat aplikasi atau website, tetapi di belakangnya terdapat
    banyak komponen infrastruktur yang bekerja bersama agar bisnis dapat berjalan.
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption(
    "Materi Pertemuan 6 — Pengantar Bisnis Digital | Topik: Infrastruktur Bisnis Digital | "
    "Dikembangkan berdasarkan RPS mata kuliah dan referensi utama Dave Chaffey."
)
