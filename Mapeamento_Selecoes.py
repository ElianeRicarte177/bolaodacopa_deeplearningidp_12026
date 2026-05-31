# Mapeamento: nome na base results.csv → sigla oficial FIFA 2026
nome_para_sigla = {
    "Mexico":                  "MEX",
    "South Africa":            "RSA",
    "South Korea":             "KOR",
    "Czech Republic":          "CZE",
    "Canada":                  "CAN",
    "Bosnia and Herzegovina":  "BIH",
    "Qatar":                   "QAT",
    "Switzerland":             "SUI",
    "Haiti":                   "HAI",
    "Scotland":                "SCO",
    "Brazil":                  "BRA",
    "Morocco":                 "MAR",
    "United States":           "USA",
    "Paraguay":                "PAR",
    "Australia":               "AUS",
    "Turkey":                  "TUR",
    "Germany":                 "GER",
    "Curaçao":                 "CUW",
    "Ivory Coast":             "CIV",
    "Ecuador":                 "ECU",
    "Netherlands":             "NED",
    "Japan":                   "JPN",
    "Sweden":                  "SWE",
    "Tunisia":                 "TUN",
    "Saudi Arabia":            "KSA",
    "Uruguay":                 "URU",
    "Spain":                   "ESP",
    "Cape Verde":              "CPV",
    "Iran":                    "IRN",
    "New Zealand":             "NZL",
    "Belgium":                 "BEL",
    "Egypt":                   "EGY",
    "France":                  "FRA",
    "Senegal":                 "SEN",
    "Norway":                  "NOR",
    "Iraq":                    "IRQ",
    "Argentina":               "ARG",
    "Algeria":                 "ALG",
    "Austria":                 "AUT",
    "Jordan":                  "JOR",
    "Ghana":                   "GHA",
    "Panama":                  "PAN",
    "England":                 "ENG",
    "Croatia":                 "CRO",
    "Portugal":                "POR",
    "DR Congo":                "COD",
    "Uzbekistan":              "UZB",
    "Colombia":                "COL",
}

# Inverso: sigla → nome na base
sigla_para_nome = {v: k for k, v in nome_para_sigla.items()}

if __name__ == "__main__":
    print(f"Total de seleções mapeadas: {len(nome_para_sigla)}")
    for nome, sigla in nome_para_sigla.items():
        print(f"  {sigla} → {nome}")
