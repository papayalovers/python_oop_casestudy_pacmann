from tabulate import tabulate as t
from math import sqrt

class Membership:
    """
    Kelas Membership ini digunakan untuk mengelola data dan prediksi keanggotaan 
    berdasarkan pengeluaran dan pendapatan bulanan pelanggan. Kelas ini juga dapat 
    menampilkan manfaat keanggotaan, persyaratan, dan menghitung harga diskon berdasarkan 
    tingkat keanggotaan yang terdaftar.

    Atribut:
        membership (dict): Menyimpan data jenis keanggotaan yang tersedia (Platinum, Gold, Silver).
        benefits (dict): Menyimpan informasi manfaat yang diterima berdasarkan keanggotaan.
        requirements (dict): Menyimpan persyaratan pengeluaran dan pendapatan bulanan untuk tiap keanggotaan.
        data_member (dict): Menyimpan data nama dan keanggotaan pelanggan yang sudah terdaftar.
    
    Metode:
        show_benefit(): Menampilkan manfaat yang tersedia untuk setiap jenis keanggotaan.
        show_requirements(): Menampilkan persyaratan pengeluaran dan pendapatan bulanan untuk setiap jenis keanggotaan.
        predict_membership(monthly_expense, monthly_income): Menghitung jarak Euclidean untuk memprediksi jenis keanggotaan 
            yang sesuai berdasarkan pengeluaran dan pendapatan bulanan pelanggan baru.
        calculate_price(membership, price_list): Menghitung harga setelah diskon berdasarkan jenis keanggotaan dan daftar harga.
    """

    membership  = {
        'Membership' : ['Platinum','Gold','Silver']
    }
    
    benefits = {
        'Discount' : ['15%','10%','8%'],
        "Another Benefit": [
            "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%",
            "Benefit Silver + Voucher Ojek Online",
            "Voucher Makanan",
        ]
    }

    requirements = {
        "Monthly Expense (juta)": [8, 6, 5],
        "Monthly Income (juta)": [15, 10, 7]
    }

    data_member = {
        'Name' : ['Sumbul', 'Ana', 'Cahya'],
        'Membership' : ['Platinum', 'Gold', 'Platinum']
    }

    def __init__(self, username):
        """
        Konstruktor untuk menginisialisasi objek Membership dengan username tertentu.

        Args:
            username (str): Nama pengguna yang akan digunakan untuk prediksi keanggotaan dan perhitungan harga.
        """
        self.username = username 

    def show_benefit(self):
        """
        Menampilkan manfaat yang tersedia untuk setiap jenis keanggotaan.
        Setiap jenis keanggotaan memiliki diskon dan manfaat tambahan yang berbeda.
        """
        membership_benefits = list(self.benefits.items())
        membership_benefits.insert(0, list(self.membership.items())[0])
        print('Membership benefit for each tier'.center(91))
        print(91*'-')
        print(t(dict(membership_benefits), headers='keys', tablefmt="github", stralign='center'))

    def show_requirements(self):
        """
        Menampilkan persyaratan pengeluaran dan pendapatan bulanan yang dibutuhkan untuk masing-masing 
        jenis keanggotaan.
        """
        requirements_info = list(self.requirements.items())
        requirements_info.insert(0, list(self.membership.items())[0])
        print('Requirements for Membership'.center(69))
        print(69*'-')
        print(t(dict(requirements_info), headers='keys', tablefmt="github", stralign='center'))

    def predict_membership(self, monthly_expense, monthly_income):
        """
        Memprediksi jenis keanggotaan yang sesuai untuk pelanggan berdasarkan 
        pengeluaran dan pendapatan bulanan menggunakan perhitungan jarak Euclidean.
        
        Jarak Euclidean digunakan untuk membandingkan pengeluaran dan pendapatan 
        pelanggan dengan data persyaratan keanggotaan dan menentukan keanggotaan 
        yang paling sesuai.

        Args:
            monthly_expense (float): Pengeluaran bulanan pelanggan dalam juta.
            monthly_income (float): Pendapatan bulanan pelanggan dalam juta.
        
        Raises:
            ValueError: Jika username pelanggan sudah terdaftar.
        """
        membership_expense = list(self.requirements.values())[0]
        membership_income =  list(self.requirements.values())[1]

        result = {}

        for (idx, expense), income in zip(enumerate(membership_expense), membership_income):
            distance = sqrt((monthly_expense-expense)**2 + (monthly_income-income)**2)
            result[list(self.membership.values())[0][idx]] = round(distance, 2)

        print(f'Hasil perhitungan dari Username {self.username} dengan jarak Euclidean adalah {result}')

        membership_recommended = min(list(result.items()), key=lambda x: x[1])[0]
        print('')
        print(f'Membership registered with: {membership_recommended}')

        if self.username not in self.data_member['Name']:
            self.data_member['Name'].append(self.username)
            self.data_member['Membership'].append(membership_recommended)
        else:
            raise ValueError('Username already exits!')

    def calculate_price(self, membership, price_list):
        """
        Menghitung harga akhir setelah diskon berdasarkan jenis keanggotaan yang dipilih.
        
        Harga akhir dihitung dengan mengurangi diskon yang sesuai berdasarkan jenis 
        keanggotaan (Platinum, Gold, Silver) dari total harga yang diberikan.

        Args:
            membership (str): Jenis keanggotaan pelanggan (Platinum, Gold, Silver).
            price_list (list of float): Daftar harga yang akan dihitungkan diskonnya.

        Returns:
            None: Menampilkan harga akhir setelah diskon.
        """
        pos = list(self.membership['Membership']).index(membership)

        discount_according_to_membership = list(self.benefits['Discount'])[pos]

        price_after_discount = sum(price_list) * (1-(int(discount_according_to_membership[:2])/100))
        print(f'Final Price: Rp.{price_after_discount:,}')
