# %%


class Holiday:
    def __init__(
        self,
        date,
        localName,
        name,
        countryCode,
        fixed,
        _global,
        counties,
        launchYear,
        types,
    ):
        self.date = date
        self.localName = localName
        self.name = name
        self.countryCode = countryCode
        self.fixed = fixed
        self._global = _global
        self.counties = counties
        self.launchYear = launchYear
        self.types = types

    def __str__(self):
        return f"{self.date} - {self.localName} - {self.name} - {self.countryCode} - {self.fixed} - {self._global} - {self.counties} - {self.launchYear} - {self.types}"


# %%