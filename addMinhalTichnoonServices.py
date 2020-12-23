'''
SCRIPT FOR ADDING ALL GEO SERVICES OF MINHAL HATICHNOON
More info on different services: https://www.gov.il/he/departments/guides/geogeographic_packaging
based on this stackexchange answer: https://gis.stackexchange.com/questions/296636/adding-arcgis-feature-service-connections-to-qgis-3-using-python-api

RUN IN QGIS PYTHON CONSOLE
'''

services=['compilation_tmm_darom', 'compilation_tmm_haifa', 'compilation_tmm_merkaz','compilation_tmm_tzafonn','gaz_compilation','gvulot_retzef','plan_index','road_compilation', 
          'reka', 'tama35_hanchayot_svivatiot','TAMA_1','Tama_35_1','tma_14_b', 'tma_34_b_3', 'tmm_1_30', 'tmm_2_9', 'tmm_3_21', 'tmm_4_14',
          'tmm_5','tmm_5_5','tmm_6','train_compilation','ttl_all_blue_lines', 'vatmal_mitchamim_muchrazim','Xplan_2039','Xplan_NoKanam','Xplan']

for s in services:
    QgsSettings().setValue('qgis/connections-arcgisfeatureserver/{}/url'.format(s), 'https://ags.iplan.gov.il/arcgisiplan/rest/services/PlanningPublic/{}/MapServer/'.format(s))
    iface.reloadConnections()



