import streamlit as st

# Data NRP dan Nama Mahasiswa
mahasiswa_data = {
    "5003231034": "Nuris Candra Ramadhani",
    "5003241059": "Wildan Afif Ghulwani",
    "5003241060": "Shafadel Lestariyan Lainy",
    "5003241061": "Laksita Rachim Sheika Hafiza",
    "5003241063": "Muhammad Farhan",
    "5003241064": "Endah Sotyaningtyas Kusumastuti",
    "5003241065": "Sheva Tafaul Samsea",
    "5003241067": "Muh. Mikyal Ihfad S.",
    "5003241068": "Rameyza Elya Mukhbita",
    "5003241069": "Zunnuroin Aulia Azmi",
    "5003241070": "Hasna Bekti Novitasari",
    "5003241071": "Akbar Kurnia Habibi",
    "5003241072": "Fitriana Puji Setyowati",
    "5003241073": "Excellius Sutan Christian",
    "5003241074": "Mohammad Fariz Irwansyah",
    "5003241075": "Adila Nurlaily",
    "5003241077": "Dyllan Daviandra Sanrevano",
    "5003241078": "Renata Jefri Nur Adia",
    "5003241079": "Fika Naila Rabbani",
    "5003241080": "Nadia Shafa Rizki Meitaputri",
    "5003241081": "Faris Irsyad",
    "5003241082": "Sevi Diah Raniri",
    "5003241083": "Irfan Maulana",
    "5003241087": "Helmi Noor Fauzi",
    "5003241162": "Diah Ayu Nurfadilah",
    "5003241163": "Lutfiana Kartika Devi",
    "5003241164": "Dwi Putri Setiya Wicaksono",
    "5003241165": "Istianatul Latifah",
    "5003241166": "Najwa Azzahra Sulaiman",
    "5003241167": "Al Faruq Dhiya' Ridho",
    "5003241168": "Aurellia Saltsa Billah",
    "5003241170": "Stanislaus Wisnu Putra Yovianto",
    "5003241171": "Marolop William Daud",
    "5003241172": "Nabila Najwa Azzahra",
    "5003241173": "Gea Artika Winata H. Ojai",
    "5003241174": "Amanda Salsabiila Supriyatmo",
    "5003241175": "Theresia Diva Callysta Anggoro",
    "5003241176": "Dendy Raffi Nur Achmad Dariswan",
    "5003241177": "Zahwa Erinda Putri",
    "5003241178": "Meidina Izzati Shaliha",
    "5003241179": "Agnita Safitri",
    "5003241180": "Zahrah Azzah Fairuzzah",
    "5003241181": "Donni Sondang Siagian Pardosi",
    "5003241182": "Natalie Syalomita Br Manjorang",
    "5003241183": "Muhammad Kevin Al-farisi",
    "5003241185": "Luthfi Adiyatma",
    "5003241186": "Indah Firdausia"
}

st.write("Halo, temen-temen Komstat C!")
st.write("Masukin NRP kalian di sini biar dapet A")

nrp = st.text_input("Masukkan NRP:")

if nrp:
    if nrp in mahasiswa_data:
        nama = mahasiswa_data[nrp]
        st.balloons()
        st.success(f"Dear, {nama}! 🎓\n\nSelamat! Kamu sudah menjalani praktikum komputasi statistika dan semester ini dengan sangat baik. Semangat terus belajar dan jangan lupa bahagia! 🤗\n\n—Kaka dan Nicole")
    else:
        st.error("Kamu bukan Komstat C yah💔")

