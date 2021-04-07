from xml.dom import minidom
from conection import conexion

# cursor1=conexion.cursor()
# sql="insert into articulos(descripcion, precio) values (%s,%s)"
# datos=("naranjas", 23.50)
# cursor1.execute(sql, datos)
# conexion.commit()
# conexion.close()

route = "/home/kamila/Python/ECOINVENT_ROOT/3.6/ecoinvent 3.6_cut-off_ecoSpold02/MasterData/"
#
# def companies():
#     xmlReader = minidom.parse(route + "Companies.xml")
#     companies = xmlReader.getElementsByTagName("company")
#     i = 0
#     for company in companies:
#         id = company.getAttribute("id")
#         code = company.getAttribute("code")
#         website = company.getAttribute("website")
#         i += 1
#         if len(company.getElementsByTagName("name")) != 0:
#             try:
#                 name = company.getElementsByTagName("name")[0].firstChild.data
#             except AttributeError:
#                 name = "not name provided by the provider"
#         else:
#             name = "not name provided by the provider"
#
#         if len(company.getElementsByTagName("comment")) != 0:
#             try:
#                 comment = company.getElementsByTagName("comment")[0].firstChild.data
#             except AttributeError:
#                 comment = "not comment provided by the provider"
#         else:
#             comment = "not comment provided by the provider"
#         # print(f"%s id: %s code: %s website: %s name: %s comment: %s" % (i, id, code, website, name, comment))
#         # print(f"id %d: UUID: %s code: %s website: %s name: %s comment: %s" % (i, id, code, website, name, comment))
#         # print("id: %d %d" % (i, len(company.getElementsByTagName("comment"))))
#         insert = "insert into company(company_id, company_code, company_name, website, comment) values (%s,%s,%s,%s,%s)"
#         datos = (id, code, name, website, comment)
#         cursor1.execute(insert, datos)
#         conexion.commit()
#     print("deben ser 167 y salen -> %s" % i)
#     return

def sources():
    print('entra sources')
    xmlReader = minidom.parse(route + "Sources.xml")
    sources = xmlReader.getElementsByTagName("source")
    i = 0
    for source in sources:
        source_id = source.getAttribute("id")
        source_type = source.getAttribute("sourceType")
        year = source.getAttribute("year")
        volume_no = source.getAttribute("volumeNo")
        first_author = source.getAttribute("firstAuthor")
        additional_authors = source.getAttribute("additionalAuthors")
        title = source.getAttribute("title")
        names_of_editors = source.getAttribute("namesOfEditors")
        short_name = source.getAttribute("shortName")
        page_numbers = source.getAttribute("pageNumbers")
        journal = source.getAttribute("journal")
        title_of_anthology = source.getAttribute("titleOfAnthology")
        place_of_publications = source.getAttribute("placeOfPublications")
        publisher = source.getAttribute("publisher")
        i += 1
        if len(source.getElementsByTagName("comment")) != 0:
            try:
                aux = ""
                comment = ""
                j = 0
                for comm in source.getElementsByTagName("comment"):
                    aux = source.getElementsByTagName("comment")[j].firstChild.nodeValue
                    comment = comment + '_' + aux
                    j += 1
            except AttributeError:
                comment = "not comment provided by the provider"
        else:
            comment = "not comment provided by the provider"
        # print(f"%s id: %s comment: %s sourceType: %s year: %s volumeNo: %s firstAuthor: %s additionalAuthors: %s title: %s namesOfEditors: %s shortName: %s pageNumbers: %s journal: %s titleOfAnthology: %s placeOfPublications: %s publisher: %s" % (i, id, comment, sourceType, year, volumeNo, firstAuthor, additionalAuthors, title, namesOfEditors, shortName, pageNumbers, journal, titleOfAnthology, placeOfPublications, publisher))
        # print(f"id %d: UUID: %s code: %s website: %s name: %s comment: %s" % (i, id, code, website, name, comment))
        # print("id: %d %d" % (i, len(company.getElementsByTagName("comment"))))
        # insert = "insert into source(source_id, source_type, year, volume_no, first_author, additional_authors, title, names_of_editors, short_name, page_numbers, journal, title_of_anthology, place_of_publications, publisher, coment) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # datos = (source_id, source_type, year, volume_no, first_author, additional_authors, title, names_of_editors, short_name, page_numbers, journal, title_of_anthology, place_of_publications, publisher, coment)
        # cursor1.execute(insert, datos)
        # conexion.commit()
    print("deben ser 1275 y salen -> %s" % i)
    return

if __name__ == "__main__":
    # cursor1 = conexion.cursor()
    # companies()
    sources()

    # conexion.close()
    # print()