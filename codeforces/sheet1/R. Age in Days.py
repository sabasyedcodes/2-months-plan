n = int(input())
years = n//365
rem_days_year = n%365
months = rem_days_year//30
total_days_month = rem_days_year%30
print(str(years)+" years")
print(str(months)+" months")
print(str(total_days_month)+" days")