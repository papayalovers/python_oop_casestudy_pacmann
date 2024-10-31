from tabulate import tabulate


class PacFlix:

    plan_info = [
        ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Service'],
        [True, True, True, 'Streaming'],
        [True, True, True, 'Download'],
        [True, True, True, 'SD'],
        [False, True, True, 'HD'],
        [False, False, True, 'UHD'],
        [1, 2, 4, 'Number of Devices'],
        ['3rd party movie only', 
         'Basic Plan Content + Sports (F1, Football, Basketball)', 
         'Basic Plan + Standard Plan + PacFlix Original Series or Movie', 'Content']
    ]

    def __init__(self):
        self.user_data = {
            'Shandy' : ['Basic Plan', 12, 'shandy-1234'],
            'Cahya' : ['Standard Plan', 24, 'Cahya-abcd'],
            'Ana' : ['Premium Plan', 5, 'ana-2f9g'],
            'Bagus' : ['Basic Plan', 11, 'bagus-9f92']
        }

    def check_plan(self):
        print(tabulate(self.plan_info[1:], headers=self.plan_info[0], tablefmt='github'))

    