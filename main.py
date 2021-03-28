import ex1, ex2, ex3, ex4, ex5
""" Exemplos extraidos de https://www.datacamp.com/community/tutorials/fuzzy-string-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1031782&gclid=Cj0KCQjw0oCDBhCPARIsAII3C_E2K94MrFFRN7rHsJiZsN20k86xxFCLT17KDZFiXIZwhhQ-9DIfo2saApVJEALw_wcB"""

presidentes = {'afonso pena': {'afonso', 'pena'},
 'artur bernardes': {'artur', 'bernardes'},
 'artur da costa e silva': {'artur', 'costa', 'da', 'e', 'silva'},
 'cafe filho': {'cafe', 'filho'},
 'campos sales': {'campos', 'sales'},
 'carlos luz': {'carlos', 'luz'},
 'delfim moreira': {'delfim', 'moreira'},
 'deodoro da fonseca': {'da', 'deodoro', 'fonseca'},
 'dilma rousseff': {'dilma', 'rousseff'},
 'emilio garrastazu medici': {'emilio', 'garrastazu', 'medici'},
 'epitacio pessoa': {'epitacio', 'pessoa'},
 'ernesto geisel': {'ernesto', 'geisel'},
 'eurico gaspar dutra': {'dutra', 'eurico', 'gaspar'},
 'fernando collor': {'collor', 'fernando'},
 'fernando henrique cardoso': {'cardoso', 'fernando', 'henrique'},
 'floriano peixoto': {'floriano', 'peixoto'},
 'getulio vargas': {'getulio', 'vargas'},
 'hermes da fonseca': {'da', 'fonseca', 'hermes'},
 'humberto castelo branco': {'branco', 'castelo', 'humberto'},
 'itamar franco': {'franco', 'itamar'},
 'jair bolsonaro': {'bolsonaro', 'jair'},
 'jose linhares': {'jose', 'linhares'},
 'jose sarney': {'jose', 'sarney'},
 'joao figueiredo': {'figueiredo', 'joao'},
 'joao goulart': {'goulart', 'joao'},
 'junta governativa provisoria de 1930': {'1930',
  'de',
  'governativa',
  'junta',
  'provisoria'},
 'junta governativa provisoria de 1969': {'1969',
  'de',
  'governativa',
  'junta',
  'provisoria'},
 'juscelino kubitschek': {'juscelino', 'kubitschek'},
 'janio quadros': {'janio', 'quadros'},
 'julio prestes': {'julio', 'prestes'},
 'luiz inacio lula da silva': {'da', 'inacio', 'luiz', 'lula', 'silva'},
 'michel temer': {'michel', 'temer'},
 'nereu ramos': {'nereu', 'ramos'},
 'nilo pecanha': {'nilo', 'pecanha'},
 'pedro aleixo': {'aleixo', 'pedro'},
 'prudente de morais': {'de', 'morais', 'prudente'},
 'ranieri mazzilli': {'mazzilli', 'ranieri'},
 'rodrigues alves': {'alves', 'rodrigues'},
 'tancredo neves': {'neves', 'tancredo'},
 'venceslau bras': {'bras', 'venceslau'},
 'washington luis': {'luis', 'washington'}}


def run():
    str1 = ""
    str2 = ""
    print(ex1.ratio(str1, str2))
    print('===')

    Str1 = "Los Angeles Lakers"
    Str2 = "Lakers"
    print(ex2.Ratio(Str1, Str2))
    print(ex2.Partial_Ratio(Str1, Str2))
    print('===')

    Str1 = "united states v. nixon"
    Str2 = "Nixon v. United States"
    print(ex3.Ratio(Str1, Str2))
    print(ex3.Partial_Ratio(Str1, Str2))
    print(ex3.Token_Sort_Ratio(Str1, Str2))
    print('===')

    Str1 = "The supreme court case of Nixon vs The United States"
    Str2 = "Nixon v. United States"
    print(ex4.Ratio(Str1, Str2))
    print(ex4.Partial_Ratio(Str1, Str2))
    print(ex4.Token_Sort_Ratio(Str1, Str2))
    print(ex4.Token_Set_Ratio(Str1, Str2))
    print('===')

    str2Match = "apple inc"
    strOptions = ["Apple Inc.","apple park","apple incorporated","iphone"]

    print(ex5.Ratios(str2Match,strOptions))
    # You can also select the string with the highest matching percentage
    print(ex5.highest(str2Match,strOptions))
    print('===')

    print(ex5.highest('Rodrigues_Alves_3.jpg', presidentes.keys()))
    print(ex5.highest('Jair_Bolsonaro_em_24_de_abril_de_2019_(1)_(cropped).jpg', presidentes.keys()))
    print(ex5.highest('Márcio_Melo_-_Junta_militar_brasileira_de_1969.png', presidentes.keys()))
    print(ex5.highest('Presidente_Michel_Temer_(foto_oficial)_-_cortada.jpg', presidentes.keys()))
    print(ex5.highest('Cartão-postal_de_Campanha_de_Júlio_Prestes_-_1930_(cropped).jpg', presidentes.keys()))

if __name__ == "__main__":
    run()
