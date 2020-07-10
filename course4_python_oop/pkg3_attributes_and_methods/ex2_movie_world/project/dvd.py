import calendar


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name, self.id, self.creation_year, self.creation_month, self.age_restriction, self.is_rented \
            = name, id, creation_year, creation_month, age_restriction, False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        split = date.split('.')
        year = int(split[-1])
        month = int(split[1])
        m_abre = calendar.month_name[month]
        return cls(name, id, year, m_abre, age_restriction)

    def __repr__(self):
        return "{}: {} ({} {}) has age restriction {}. Status: {}" \
            .format(self.id,
                    self.name,
                    self.creation_month,
                    self.creation_year,
                    self.age_restriction,
                    ["rented" if self.is_rented else "not rented"][0])
