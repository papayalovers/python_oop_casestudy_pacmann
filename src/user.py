from tabulate import tabulate
import random
import string

class PacFlix:
    def __init__(self):
        self.plan_info = [
            ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Service'],
            [True, True, True, 'Streaming'],
            [True, True, True, 'Download'],
            [True, True, True, 'SD'],
            [False, True, True, 'HD'],
            [False, False, True, 'UHD'],
            [1, 2, 4, 'Number of Devices'],
            ['3rd party movie only', 
            'Basic Plan Content + Sports (F1, Football, Basketball)', 
            'Basic Plan + Standard Plan + PacFlix Original Series or Movie', 'Content'],
            [120_000, 160_000, 200_000, 'Price']
        ]
        self.user_data = {
                'Shandy' : ['Basic Plan', 12, 'shandy-1234'],
                'Cahya' : ['Standard Plan', 24, 'Cahya-abcd'],
                'Ana' : ['Premium Plan', 5, 'ana-2f9g'],
                'Bagus' : ['Basic Plan', 11, 'bagus-9f92']
            }

    def check_all_plan(self):
        print(tabulate(self.plan_info[1:], headers=self.plan_info[0], tablefmt='github'))

class User(PacFlix):
    def __init__(self, username):
        super().__init__()
        self.subs_price = None

        if username in self.user_data.keys():
            self.username = username
            self.plan = self.user_data[username][0]
            self.duration = self.user_data[username][1]
            self.referral = self.user_data[username][2]
            print(f'Halo {username}, kamu telah berlangganan selama {self.duration} bulan di PacFlix')
        else:
            self.username = username
            self.plan = None
            self.duration = 1
            # generate referral code for the new user 
            self.referral = username.lower()+'-'+''.join(random.choices(string.ascii_letters + string.digits, k=4)) 
            # adding to database pacflix
            self.user_data[username] = [self.plan, self.duration, self.referral]
            print('Selamat Anda Telah Terdaftar di PacFlix')
            print(f'Kode Refferal Anda adalah {self.referral}')
            print('Silahkan gunakan kode tersebut kepada teman anda untuk mendapatkan potongan 4%!')
            print(50*'-')

    def subs_plan(self, new_plan):
        price_basic = self.plan_info[-1][0]
        price_standard = self.plan_info[-1][1]
        price_premium = self.plan_info[-1][2]   
        referral_code = str(input('Code Refferal: '))
        # check the referral code if its available it will be get 4% discount
        for _, values in self.user_data.items():
            if referral_code in values[-1]:
                if new_plan == 'Basic Plan': 
                    self.subs_price = price_basic - (price_basic * 0.04)
                elif new_plan == 'Standard Plan':
                    self.subs_price = price_standard - (price_standard * 0.04)
                elif new_plan == 'Premium Plan':
                    self.subs_price = price_premium - (price_premium * 0.04)
                else:
                    raise ValueError('Plan tidak ditemukan')
        # change in database
        self.user_data[self.username][0] = new_plan
        # change atribut instance value
        self.plan = new_plan
        print('Terima Kasih Telah Berlangganan di PacFlix')
                    
    def check_plan(self):
        if self.plan:
            idx_plan = self.plan_info[0].index(self.plan) # get the index of plan
            user_plan = [[row[idx_plan], row[-1]] for row in self.plan_info]
            print(44*'-')
            print(tabulate(user_plan[1:], user_plan[0], tablefmt='github'))
            print(44*'-')
            print(f'Kamu sedang berlangganan {self.plan}')
            if self.subs_price:
                print(f'Biaya langganan setelah diskon Rp. {self.subs_price:,}')
            else:
                print(f'Biaya langganan Rp. {self.plan_info[-1][idx_plan]:,}')
        else:
            print('Anda belum berlangganan di PacFlix, silahkan langganan terlebih dahulu.')

    def upgrade_plan(self, upgraded_plan):
        idx_current_plan = self.plan_info[0].index(self.plan)
        idx_new_upgrade_plan = self.plan_info[0].index(upgraded_plan)

        # get duration time subscription
        if idx_new_upgrade_plan > idx_current_plan:
            # change in database
            self.user_data[self.username][0] = upgraded_plan
            # change atribut instance value
            self.plan = upgraded_plan
            if self.duration > 12:
                self.subs_price = self.plan_info[-1][idx_new_upgrade_plan] - (self.plan_info[-1][idx_new_upgrade_plan] * 0.05)
        else:
            print('Tidak bisa Downgrade !')
        
        





               
