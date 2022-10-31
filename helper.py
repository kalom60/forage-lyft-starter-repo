def curr_date(last_serviced, years_to_add):
    years = last_serviced.replace(year=last_serviced.year + years_to_add)
    return years