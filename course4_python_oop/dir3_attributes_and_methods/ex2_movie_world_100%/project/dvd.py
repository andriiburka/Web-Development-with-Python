import calendar


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name, self.id, self.creation_year, self.creation_month, self.age_restriction, self.is_rented \
            = name, id, creation_year, creation_month, age_restriction, False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        split = date.split('.')
        year, month = int(split[-1]), int(split[1])
        m_abre = calendar.month_name[month]
        return cls(name, id, year, m_abre, age_restriction)

    def __repr__(self):
        return '{id}: {name} ({month} {year}) has age restriction {age_restriction}. Status: {status}' \
            .format(id=self.id,
                    name=self.name,
                    month=self.creation_month,
                    year=self.creation_year,
                    age_restriction=self.age_restriction,
                    status=["rented" if self.is_rented else "not rented"][0])
