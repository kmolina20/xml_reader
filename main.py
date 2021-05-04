from builtins import print
from xml.dom import minidom
from conection import conexion
import os
import numpy as np

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
        '''obtener los rows que ya han sido ingresados para comprobar que no se repita pero que si esten todos'''
        select = "SELECT * FROM activity_index where id='" + id + "' and activity_name_id='"+activity_name_id+"' and geography_id='"+geography_id+"' and start_date='"+start_date+"' and end_date='"+end_date+"' and special_activity_type='"+special_activity_type+"' and system_model_id='"+system_model_id+"';"
        cursor1.execute(select)
        activity_index = cursor1.fetchall()
        if len(activity_index) == 0:
            insert = "insert into activity_index(id, activity_name_id, geography_id, start_date, end_date, special_activity_type, system_model_id, version) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            datos = (id, activity_name_id, geography_id, start_date, end_date, special_activity_type, system_model_id, version)
            cursor1.execute(insert, datos)
            conexion.commit()
    print("deben ser 35708 y salen -> %s" % i)
    return

def intermediateExchange():
    xmlReader = minidom.parse(routeMD + "IntermediateExchanges.xml")
    intermediateExchanges = xmlReader.getElementsByTagName("intermediateExchange")
    i = 0
    for intermediateExchange in intermediateExchanges:
        id = intermediateExchange.getAttribute("id")
        unit_id = intermediateExchange.getAttribute("unitId")
        i += 1
        if len(intermediateExchange.getElementsByTagName("name")) != 0:
            try:
                name = intermediateExchange.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                name = "not name provided by the provider"
        else:
            name = "not name provided by the provider"
        if len(intermediateExchange.getElementsByTagName("name")) != 0:
            try:
                name = intermediateExchange.getElementsByTagName("name")[0].firstChild.data
            except AttributeError:
                name = "not name provided by the provider"
        else:
            name = "not name provided by the provider"
        insert = "insert into intermediate_exchange(id, unit_id, name) values (%s, %s, %s)"
        datos = (id, unit_id, name)
        cursor1.execute(insert, datos)
        conexion.commit()
    print("deben ser 3205 y salen -> %s" % i)
    return

def ordenamientoBurbuja(matriz,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(int(matriz[j][0]) > int(matriz[j+1][0])):
                n = matriz[j+1][0]
                o = matriz[j+1][1]
                matriz[j+1][0] = matriz[j][0]
                matriz[j+1][1] = matriz[j][1]
                matriz[j][0] = n
                matriz[j][1] = o

def leerActividad():
    """data_generator_and_publication - activity - acitivity_intermediate_exchange - activity_person"""
    # os.rename(routeDS + "New folder/0122d540-58ed-4a1b-8ce3-8437827cd3ac_71e2f1db-a2c5-44d0-8337-dfff15be974d.spold", routeDS+"New folder/0122d540-58ed-4a1b-8ce3-8437827cd3ac_71e2f1db-a2c5-44d0-8337-dfff15be974d.xml")
    # os.rename(routeDS + "New folder/0a3b32da-3a5d-4ece-98b7-2c30fa78be34_66c93e71-f32b-4591-901c-55395db5c132.spold", routeDS+"New folder/0a3b32da-3a5d-4ece-98b7-2c30fa78be34_66c93e71-f32b-4591-901c-55395db5c132.xml")
    # os.rename(routeDS + "New folder/0b5c13c7-820e-47d3-aa39-ed2fb6612ec3_9cdb112b-0d90-4d76-9cec-412b0c67d8bb.spold", routeDS+"New folder/0b5c13c7-820e-47d3-aa39-ed2fb6612ec3_9cdb112b-0d90-4d76-9cec-412b0c67d8bb.xml")
    # os.rename(routeDS + "New folder/0b818f0b-39a8-45a8-a1b1-a3b791e1b1c6_7566f905-29c9-45d6-b2ff-65980f38e3a0.spold", routeDS+"New folder/0b818f0b-39a8-45a8-a1b1-a3b791e1b1c6_7566f905-29c9-45d6-b2ff-65980f38e3a0.xml")
    xmlReader = minidom.parse(routeDS+"New folder/0b818f0b-39a8-45a8-a1b1-a3b791e1b1c6_7566f905-29c9-45d6-b2ff-65980f38e3a0.xml")
    activityDescriptions = xmlReader.getElementsByTagName("activityDescription")
    i = 0
    general_comment = ""
    print("for activityDescription in activityDescriptions:")
    for activityDescription in activityDescriptions:
        for activity in activityDescription.getElementsByTagName("activity"):
            activity_index_id = activity.getAttribute("id")
            if len(activity.getElementsByTagName("allocationComment")) != 0:
                try:
                    allocation_comment = property.getElementsByTagName("allocationComment")[0].firstChild.data
                except AttributeError:
                    allocation_comment = "not allocationComment provided by the provider"
            else:
                allocation_comment = "not allocationComment provided by the provider"
            included_processes = "includedActivitiesStart" +activity.getElementsByTagName("includedActivitiesStart")[0].firstChild.data
            """VALIDAR CUANDO NO TENGA UN END -check-"""
            if len(activity.getElementsByTagName("includedActivitiesEnd")) != 0:
                included_processes = included_processes + "includedActivitiesEnd" + activity.getElementsByTagName("includedActivitiesEnd")[0].firstChild.data
            '''ORDENAMIENTO DE generalComment -check-'''
            for generalComment in activity.getElementsByTagName("generalComment"):
                matriz = []
                for text in generalComment.getElementsByTagName("text"):
                    filas = len(generalComment.getElementsByTagName("text"))
                    columnas = 2
                    for j in range(columnas):
                        if (j == 0):
                            a = str(text.getAttribute("index"))
                        if (j == 1):
                            b = str(generalComment.getElementsByTagName("text")[i].firstChild.data)
                    i += 1
                    array = np.array([a,b])
                    matriz.append(array)
                # print(matriz)
                ordenamientoBurbuja(matriz, len(matriz))
                # print(matriz)
                for q in range(0,filas):
                    general_comment = general_comment + "\n" + matriz[q][1]
    print("administrativeInformations = xmlReader.getElementsByTagName(administrativeInformation)")
    administrativeInformations = xmlReader.getElementsByTagName("administrativeInformation")
    for administrativeInformation in administrativeInformations:
        for dataGeneratorAndPublication in administrativeInformation.getElementsByTagName("dataGeneratorAndPublication"):
            personName = dataGeneratorAndPublication.getAttribute("personName")
            source_id = dataGeneratorAndPublication.getAttribute("publishedSourceId")
            if len(dataGeneratorAndPublication.getAttribute("publishedSourceId")) == 0:
                source_id = "00000000-0000-0000-0000-000000000000"
            is_copyright_protected = dataGeneratorAndPublication.getAttribute("isCopyrightProtected")
            '''obtener el id de la persona en base al nombre dado los diferentes id's por las versiones'''
            select = "SELECT id FROM person where name='" + personName + "';"
            cursor1.execute(select)
            person_id = cursor1.fetchall()
            '''colocar validacion de si no encuentra el nombre, debe crear una nueva persona'''
            if len(person_id) == 0:
                print("no encuentra nombre->crear nueva 'persona' -> %s" % personName)
            insert = "insert into data_generator_and_publication(person_id, source_id, is_copyright_protected) values (%s, %s, %s)"
            datos = (person_id[0], source_id, is_copyright_protected)
            cursor1.execute(insert, datos)
            conexion.commit()
        for timePeriod in activityDescription.getElementsByTagName("timePeriod"):
            is_data_valid_for_entire_period = timePeriod.getAttribute("isDataValidForEntirePeriod")
        '''VALIDAR  CIANDO NO HAYA comment_technology - check'''
        for technology in activityDescription.getElementsByTagName("technology"):
            if len(technology.getElementsByTagName("comment")) != 0:
                for comment in technology.getElementsByTagName("comment"):
                    comment_technology = comment.getElementsByTagName("text")[0].firstChild.data
            else:
                comment_technology = "NO COMMENT TECHNOLOGY"
        '''obtener el ultimo id de data_generator_and_publication ingresado en la base'''
        select = "SELECT MAX(id) AS id FROM data_generator_and_publication"
        cursor1.execute(select)
        data_generator_and_publication = cursor1.fetchall()
        insert = "insert into activity(activity_index_id, allocation_comment, general_comment, included_processes, comment_technology, is_data_valid_for_entire_period, data_generator_and_publication_id) values (%s, %s, %s, %s, %s, %s, %s)"
        datos = (activity_index_id, allocation_comment, general_comment, included_processes, comment_technology, is_data_valid_for_entire_period, data_generator_and_publication[0])
        cursor1.execute(insert, datos)
        conexion.commit()
    print("flowDatas = xmlReader.getElementsByTagName(flowData)")
    i = 0  # contador para comprabar la cantidad que se ingresa en la tabla
    flowDatas = xmlReader.getElementsByTagName("flowData")
    for flowData in flowDatas:
        for intermediateExchange in flowData.getElementsByTagName("intermediateExchange"):
            # id = intermediateExchange.getAttribute("id")
            intermediate_exchange_id = intermediateExchange.getAttribute("intermediateExchangeId")
            variable_name = intermediateExchange.getAttribute("variableName")
            i += 1
            '''debe buscar el ultimo id ingresado, ahora se manda el 1 pero debe buscar el ultimo id ingresado enla tabla activity'''
            select = "SELECT MAX(id) AS id FROM activity"
            cursor1.execute(select)
            activity_id = cursor1.fetchall()
            insert = "insert into acitivity_intermediate_exchange(activity_id, intermediate_exchange_id, variable_name) values (%s, %s, %s)"
            datos = (activity_id[0], intermediate_exchange_id, variable_name)
            cursor1.execute(insert, datos)
            conexion.commit()
    print("acitivity_intermediate_exchange -> deben ser 15-42 y salen -> %s" % i)
    print("modellingAndValidations = xmlReader.getElementsByTagName(modellingAndValidation)")
    i = 0 #contador para comprabar la cantidad que se ingresa en la tabla
    modellingAndValidations = xmlReader.getElementsByTagName("modellingAndValidation")
    for modellingAndValidation in modellingAndValidations:
        for review in modellingAndValidation.getElementsByTagName("review"):
            reviewerName = review.getAttribute("reviewerName")
            '''obtener el id de la persona en base al nombre dado los diferentes id's por las versiones'''
            select = "SELECT id FROM person where name='"+reviewerName+"';"
            cursor1.execute(select)
            person_id = cursor1.fetchall()
            person_id2 = "".join(map(str, person_id[0]))
            # print(person_id2)
            '''colocar validacion de si no encuentra el nombre, debe crear una nueva persona'''

            '''buscar el ultimo id de activity ingresado'''
            select = "SELECT MAX(id) AS id FROM activity"
            cursor1.execute(select)
            activity_id = cursor1.fetchall()
            activity_id2 = "".join(map(str, activity_id[0]))
            '''validar si ya se agregaron esos dos id's dado que puede repetirse por ser varias veces revisor pero solo nos importa que se ingrese una vez a nosotros'''
            select = "SELECT person_id, activity_id FROM activity_person where person_id='"+person_id2+"' and activity_id='"+activity_id2+"';"
            cursor1.execute(select)
            verifica = cursor1.fetchall()
            # print(len(verifica))
            if len(verifica) == 0:
                insert = "insert into activity_person(person_id, activity_id) values (%s, %s)"
                datos = (person_id[0], activity_id[0])
                cursor1.execute(insert, datos)
            # else:
            #     print("ya existe")
            conexion.commit()
            i += 1
    print("activity_person -> deben ser 16-16 y salen -> %s" % i)
    return

if __name__ == "__main__":
    cursor1 = conexion.cursor()
    # intermediateExchange()
    # companies()
    # sources()
    # persons()
    # activity_name()
    # geography()
    # unit()
    # system_model()
    # property()
    # activityIndexEntry()
    leerActividad()

    conexion.close()

    print("end")