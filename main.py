from xml.dom import minidom
from conection import conexion
import os

# cursor1=conexion.cursor()
# sql="insert into articulos(descripcion, precio) values (%s,%s)"
# datos=("naranjas", 23.50)
# cursor1.execute(sql, datos)
# conexion.commit()
# conexion.close()

routeMD = "/home/kamila/Python/ECOINVENT_ROOT/3.6/ecoinvent 3.6_cut-off_ecoSpold02/MasterData/"
routeDS = "/home/kamila/Python/ECOINVENT_ROOT/3.6/ecoinvent 3.6_cut-off_ecoSpold02/datasets/"

def companies():
    xmlReader = minidom.parse(routeMD + "Companies.xml")
    companies = xmlReader.getElementsByTagName("company")
    i = 0
    for company in companies:
        id = company.getAttribute("id")
        code = company.getAttribute("code")
        website = company.getAttribute("website")
        i += 1
        if len(company.getElementsByTagName("name")) != 0:
            try:
                name = company.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                name = "not name provided by the provider"
        else:
            name = "not name provided by the provider"

        if len(company.getElementsByTagName("comment")) != 0:
            try:
                comment = company.getElementsByTagName("comment")[0].firstChild.data
            except AttributeError:
                comment = "not comment provided by the provider"
        else:
            comment = "not comment provided by the provider"
        insert = "insert into company(id, code, name, website, comment) values (%s,%s,%s,%s,%s)"
        datos = (id, code, name, website, comment)
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 167 y salen -> %s" % i)
    return

def sources():
    xmlReader = minidom.parse(routeMD + "Sources.xml")
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
        insert = "insert into source(id, type, year, volume_no, first_author, additional_authors, title, names_of_editors, short_name, page_numbers, journal, title_of_anthology, place_of_publications, publisher, comment) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (source_id, source_type, year, volume_no, first_author, additional_authors, title, names_of_editors, short_name, page_numbers, journal, title_of_anthology, place_of_publications, publisher, comment)
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 1275 y salen -> %s" % i)
    return

def persons():
    xmlReader = minidom.parse(routeMD + "Persons.xml")
    sources = xmlReader.getElementsByTagName("person")
    i = 0
    for source in sources:
        person_id = source.getAttribute("id")
        person_name = source.getAttribute("name")
        person_address = source.getAttribute("address")
        person_telephone = source.getAttribute("telephone")
        person_telefax = source.getAttribute("telefax")
        person_email = source.getAttribute("email")
        company_id = source.getAttribute("companyId")
        i += 1
        if len(source.getAttribute("companyId")) == 0:
            company_id = "00000000-0000-0000-0000-000000000000"
        insert = "insert into person(id, name, email, address, telephone, telefax, company_id) values (%s, %s, %s, %s, %s, %s, %s)"
        datos = (person_id, person_name, person_email, person_address, person_telephone, person_telefax, company_id)
        print("%s, id: %s company: %s,"%(i, person_id, company_id))
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 381 y salen -> %s" % i)
    return

def dataEntryBy():
    """Esta funcion no sirve de nada OMITIR"""
    xmlReader = minidom.parse(routeMD + "0122d540-58ed-4a1b-8ce3-8437827cd3ac_71e2f1db-a2c5-44d0-8337-dfff15be974d.spold")
    sources = xmlReader.getElementsByTagName("dataEntryBy")
    i = 0
    for source in sources:
        person_id = source.getAttribute("personId")
        is_active_author = source.getAttribute("isActiveAuthor")

        i += 1
        if len(source.getAttribute("companyId")) == 0:
            company_id = "00000000-0000-0000-0000-000000000000"
        # print(f"%s id: %s comment: %s sourceType: %s year: %s volumeNo: %s firstAuthor: %s additionalAuthors: %s title: %s namesOfEditors: %s shortName: %s pageNumbers: %s journal: %s titleOfAnthology: %s placeOfPublications: %s publisher: %s" % (i, id, comment, sourceType, year, volumeNo, firstAuthor, additionalAuthors, title, namesOfEditors, shortName, pageNumbers, journal, titleOfAnthology, placeOfPublications, publisher))
        # print(f"id %d: UUID: %s code: %s website: %s name: %s comment: %s" % (i, id, code, website, name, comment))
        # print("id: %d %d" % (i, len(company.getElementsByTagName("comment"))))
        insert = "insert into person(person_id, person_name, person_email, person_address, person_telephone, person_telefax, company_id) values (%s, %s, %s, %s, %s, %s, %s)"
        datos = (person_id, is_active_author)
        # print("%s, id: %s company: %s,"%(i, person_id, company_id))
        # cursor1.execute(insert, datos)
        # conexion.commit()
    print("deben ser 381 y salen -> %s" % i)
    return

def activity_name():
    xmlReader = minidom.parse(routeMD + "ActivityNames.xml")
    activity_names = xmlReader.getElementsByTagName("activityName")
    i = 0
    for activity_name in activity_names:
        activity_name_id = activity_name.getAttribute("id")
        i += 1
        if len(activity_name.getElementsByTagName("name")) != 0:
            try:
                activity_name = activity_name.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                activity_name = "not name provided by the provider"
        else:
            activity_name = "not name provided by the provider"
        insert = "insert into activity_name(id, activity_name) values (%s, %s)"
        datos = (activity_name_id, activity_name)
        print("%s, id: %s activity_name: %s,"%(i, activity_name_id, activity_name))
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 7485 y salen -> %s" % i)
    return

def geography():
    xmlReader = minidom.parse(routeMD + "Geographies.xml")
    geographies = xmlReader.getElementsByTagName("geography")
    i = 0
    for geography in geographies:
        geography_id = geography.getAttribute("id")
        longitude = geography.getAttribute("longitude")
        latitude = geography.getAttribute("latitude")
        un_code = geography.getAttribute("uNCode")
        un_region_code = geography.getAttribute("uNRegionCode")
        un_subregion_code = geography.getAttribute("uNSubregionCode")
        i += 1
        if len(geography.getElementsByTagName("name")) != 0:
            try:
                name = geography.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                name = "not name provided by the provider"
        else:
            name = "not name provided by the provider"

        if len(geography.getElementsByTagName("shortname")) != 0:
            try:
                short_name = geography.getElementsByTagName("shortname")[0].firstChild.data
            except AttributeError:
                short_name = "not shortname provided by the provider"
        else:
            short_name = "not shortname provided by the provider"
        insert = "insert into geography(id, longitude, latitude, un_code, un_region_code, un_subregion_code, name, short_name) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (geography_id, longitude, latitude, un_code, un_region_code, un_subregion_code, name, short_name)
        # print("%s, id: %s geography: %s,"%(i, geography_id, longitude, latitude, un_code, un_region_code, un_subregion_code, name, short_name))
        print("%s, id: %s "%(i, geography_id))
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 479 y salen -> %s" % i)
    return

def unit():
    xmlReader = minidom.parse(routeMD + "Units.xml")
    units = xmlReader.getElementsByTagName("unit")
    i = 0
    for unit in units:
        unit_id = unit.getAttribute("id")
        i += 1
        if len(unit.getElementsByTagName("name")) != 0:
            try:
                unit_name = unit.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                unit_name = "not name provided by the provider"
        else:
            unit_name = "not name provided by the provider"
        if len(unit.getElementsByTagName("comment")) != 0:
            try:
                unit_comment = unit.getElementsByTagName("comment")[0].firstChild.data
            except AttributeError:
                unit_comment = "not comment provided by the provider"
        else:
            unit_comment = "not comment provided by the provider"
        insert = "insert into unit(id, name, comment) values (%s, %s, %s)"
        datos = (unit_id, unit_name, unit_comment)
        print("%s, id: %s unit_name: %s,"%(i, unit_id, unit_name))
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 124 y salen -> %s" % i)
    return

def system_model():
    xmlReader = minidom.parse(routeMD + "SystemModels.xml")
    systemModels = xmlReader.getElementsByTagName("systemModel")
    i = 0
    for systemModel in systemModels:
        unit_id = systemModel.getAttribute("id")
        i += 1
        if len(systemModel.getElementsByTagName("name")) != 0:
            try:
                system_model_name = systemModel.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                system_model_name = "not name provided by the provider"
        else:
            system_model_name = "not name provided by the provider"
        if len(systemModel.getElementsByTagName("shortname")) != 0:
            try:
                system_model_short_name = systemModel.getElementsByTagName("shortname")[0].firstChild.data
            except AttributeError:
                system_model_short_name = "not shortname provided by the provider"
        else:
            system_model_short_name = "not shortname provided by the provider"
        insert = "insert into system_model(id, name, short_name) values (%s, %s, %s)"
        datos = (unit_id, system_model_name, system_model_short_name)
        print("%s, id: %s system_model_name: %s,"%(i, unit_id, system_model_name))
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 10 y salen -> %s" % i)
    return

def property():
    xmlReader = minidom.parse(routeMD + "Properties.xml")
    properties = xmlReader.getElementsByTagName("property")
    i = 0
    for property in properties:
        property_id = property.getAttribute("id")
        default_variable_name = property.getAttribute("defaultVariableName")
        unit_id = property.getAttribute("unitId")
        i += 1
        if len(property.getAttribute("unitId")) == 0:
            unit_id = "00000000-0000-0000-0000-000000000000"
        if len(property.getElementsByTagName("name")) != 0:
            try:
                property_name = property.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                property_name = "not name provided by the provider"
        else:
            property_name = "not name provided by the provider"
        insert = "insert into property(id, unit_id, default_variable_name, name) values (%s, %s, %s, %s)"
        datos = (property_id, unit_id, property_name, default_variable_name)
        print("%s, id: %s property_name: %s,"%(i, property_id, property_name))
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 947 y salen -> %s" % i)
    return

def activityIndexEntry():
    xmlReader = minidom.parse(routeMD + "ActivityIndex.xml")
    activityIndexEntry = xmlReader.getElementsByTagName("activityIndexEntry")
    version = "ecoinvent 3.6_cut-off_ecoSpold02"
    i = 0
    for activityIndex in activityIndexEntry:
        id = activityIndex.getAttribute("id")
        activity_name_id = activityIndex.getAttribute("activityNameId")
        geography_id = activityIndex.getAttribute("geographyId")
        start_date = activityIndex.getAttribute("startDate")
        end_date = activityIndex.getAttribute("endDate")
        special_activity_type = activityIndex.getAttribute("specialActivityType")
        system_model_id = activityIndex.getAttribute("systemModelId")
        i += 1

        insert = "insert into activity_index(id, activity_name_id, geography_id, start_date, end_date, special_activity_type, system_model_id, version) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (id, activity_name_id, geography_id, start_date, end_date, special_activity_type, system_model_id, version)
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser +19999 (19749) y salen -> %s" % i)
    return

def select():
    select = "SELECT * FROM activity_index where id='00093951-0c71-4a74-96d8-ece56003838a' ORDER BY id ASC;"
    cursor1.execute(select)

def leerActividad():
    # os.rename(routeDS + "New folder/0122d540-58ed-4a1b-8ce3-8437827cd3ac_71e2f1db-a2c5-44d0-8337-dfff15be974d.spold", routeDS+"New folder/0122d540-58ed-4a1b-8ce3-8437827cd3ac_71e2f1db-a2c5-44d0-8337-dfff15be974d.xml")
    xmlReader = minidom.parse(routeDS+"New folder/0122d540-58ed-4a1b-8ce3-8437827cd3ac_71e2f1db-a2c5-44d0-8337-dfff15be974d.xml")
    activityDescriptions = xmlReader.getElementsByTagName("activityDescription")
    i = 0
    j = 1
    for activityDescription in activityDescriptions:
        for activity in activityDescription.getElementsByTagName("activity"):
            activity_index_id = activity.getAttribute("id")
            if len(activity.getElementsByTagName("allocationComment")) != 0:
                try:
                    property_name = property.getElementsByTagName("allocationComment")[0].firstChild.data
                except AttributeError:
                    property_name = "not allocationComment provided by the provider"
            else:
                property_name = "not allocationComment provided by the provider"
            for generalComment in activity.getElementsByTagName("generalComment"):
                for text in generalComment.getElementsByTagName("text"):
                    print(generalComment.getElementsByTagName("text")[j].firstChild.data)
                    # print("index: %s" % text.getAttribute("index"))

                    # # print(len(generalComment.getElementsByTagName("text")))
                    # for k in str(len(generalComment.getElementsByTagName("text"))):
                    #     if (text.getAttribute("index") == str(1)):
                    #         print(generalComment.getElementsByTagName("text")[int(k)].firstChild.data)
                    #         print("k: %s" % k)
                    j += 1
                    print("j: %s" % (j-1))

        # property_id = property.getAttribute("id")
        # default_variable_name = property.getAttribute("defaultVariableName")
        # unit_id = property.getAttribute("unitId")
        # i += 1
        # if len(property.getAttribute("unitId")) == 0:
        #     unit_id = "00000000-0000-0000-0000-000000000000"
        # if len(property.getElementsByTagName("name")) != 0:
        #     try:
        #         property_name = property.getElementsByTagName("name")[0].firstChild.data
        #     except AttributeError:
        #         property_name = "not name provided by the provider"
        # else:
        #     property_name = "not name provided by the provider"
        # insert = "insert into property(id, unit_id, default_variable_name, name) values (%s, %s, %s, %s)"
        # datos = (property_id, unit_id, property_name, default_variable_name)
        # print("%s, id: %s property_name: %s," % (i, property_id, property_name))
        # cursor1.execute(insert, datos)
        # conexion.commit()
    # print("deben ser 947 y salen -> %s" % i)
    return

if __name__ == "__main__":
    cursor1 = conexion.cursor()
    # activityIndexEntry()
    # select()
    leerActividad()
    # companies()
    # sources()
    # persons()
    # activity_name()
    # geography()
    # unit()
    # system_model()
    # property()

    conexion.close()

    # print("")