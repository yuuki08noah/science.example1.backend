import pandas as pd
import os

df = pd.read_csv('data/isotope.csv')
df = df.fillna(0)
df['weight'] = (df['mass_number#1']*df['percentage#1']/100 +
                df['mass_number#2']*df['percentage#2']/100 +
                df['mass_number#3']*df['percentage#3']/100 +
                df['mass_number#4']*df['percentage#4']/100 +
                df['mass_number#5']*df['percentage#5']/100 +
                df['mass_number#6']*df['percentage#6']/100)

def get_isotope_by_number(number):
    return df[df['number'] == number].squeeze()

def get_isotopes():
    return df
