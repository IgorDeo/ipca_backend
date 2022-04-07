import pandas as pd
from date_handler import DateHandler


class Ipca:
    
    def __init__(self):
        self.df_ipca = None
        self.most_recent_date = None
        self.date_handler = DateHandler()
        self.floor_date = ''
        self.ceil_date = ''
        
    def init_ipca_data(self):
        ipca_dataframe = pd.read_excel('./src/sheets/ipca_com_tratativa_2.xlsx')
        ipca_dataframe['data'] = pd.to_datetime(ipca_dataframe['data'])
        self.df_ipca = ipca_dataframe
        self.most_recent_date = self.df_ipca['data'].max()
    
    def __slice_ipca_data(self, start_date, end_date):
        
        self.floor_date, self.ceil_date = self.date_handler.handle_range_dates(start_date, end_date, self.most_recent_date)
       
        self.floor_date = self.floor_date.strftime('%d-%m-%Y')
        self.ceil_date = self.ceil_date.strftime('%d-%m-%Y')

        print(self.floor_date, self.ceil_date)

        bottom_index = (self.df_ipca.index[self.df_ipca['data'] == self.floor_date])[0]
        top_index = (self.df_ipca.index[self.df_ipca['data'] == self.ceil_date])[0]

        return self.df_ipca.loc[bottom_index:top_index]

    def accumulated_tax(self, start_date, end_date):
        self.init_ipca_data()
        ipca_data = self.__slice_ipca_data(start_date, end_date)

        initial_price = final_price = 100
        price_at_month = 0

        for row in ipca_data.values:
            price_at_month = (1+(row[1]/100))*final_price
            final_price = price_at_month

        return {
            'accumulated_tax': (final_price - initial_price)/100,
            'period': (self.floor_date,self.ceil_date)
        }
        