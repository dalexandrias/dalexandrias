from zeep import Client, Settings
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from requests import Session
from requests.auth import HTTPBasicAuth

# URL do WSDL
wsdl = 'URL_DO_SEU_WSDL'

# Configuração de autenticação, se necessário
session = Session()
session.auth = HTTPBasicAuth('seu_usuario', 'sua_senha')

# Configurar o transporte e histórico
transport = Transport(session=session)
history = HistoryPlugin()

# Inicializar o cliente
client = Client(wsdl=wsdl, transport=transport, plugins=[history])

# XML de exemplo
xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:toatech:agent">
    <soapenv:Header/>
    <soapenv:Body>
        <send_message xmlns:cdpre="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/confirmDisconnectionPhysicalResource/V4" xmlns:rdpr="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/requestDisconnectionPhysicalResourceEntities/V4" xmlns:ccabrel="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagement/consultCabinetRelease" xmlns:actv="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/activateNetworkResourcesEntities/V4" xmlns:rme="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/cancelReservedExternalResourceEntities/V4" xmlns:der="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/deallocateExternalResourceEntities/V4" xmlns:rii="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagement/RetrieveInventoryInformationEntities/V4" xmlns:rim="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/ConfirmReserveEntities/V4" xmlns:rir="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/reserveInternalResource/V4" xmlns:rem="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagement/RemoveInventoryInformationEntities/V4" xmlns:wor="http://www.gvt.com.br/ResourceManagement/WorkforceManagement/WorkOrderTrackingAndManagement/WorkOrderTracking/workOrderTrackingEntities" xmlns:rer="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/reserveExternalResource/V4" xmlns:apr="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/activatePhysicalResourceEntities/V4" xmlns:prs="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/getPhysicalResourceSummary/V4" xmlns:rrnr="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/releaseReservedNetworkResourcesEntities/V4" xmlns:rnr="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/reserveNetworkResourcesEntities/V4" xmlns:cerd="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/cancelExternalResourceDesignEntities/V4" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:rapr="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/releaseActivePhysicalResource/V4" xmlns:retr="http://www.gvt.com.br/ResourceManagement/ResourceDomainManagement/ResourceActivation/ResourceActivation/V2/retrieveResourceActivationEntities" xmlns:save="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagement/SaveInventoryInformationEntities/V4" xmlns:deac="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/deactivateNetworkResourcesEntities/V4" xmlns:aer="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/activateExternalResourceEntities/V4" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:uer="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/updateExternalResource/V4" xmlns:gvt="http://www.gvt.com.br/GvtCommonEntities" xmlns:gnr="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/getNetworkResourcesEntities/V4" xmlns:upda="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagement/UpdateResourceEntities/V4" xmlns:cr="http://services.telefonica.com/Resource/ResourceProvisioning/ConfigureAndActivateResource/ConfigureActiveResourceEntities" xmlns:rdc="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/getResourceDesignCircuitEntities/V4" xmlns:rde="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/requestDisconnectExternalResourceEntities/V4" xmlns:crir="http://www.gvt.com.br/ResourceManagement/ResourceInventoryManagement/ResourceInventoryManagementV4/cancelReservedInternalResourceEntities/V4" xmlns:tns="urn:toatech:agent" xmlns="urn:toatech:agent">
            <tns:messages>
                <tns:message>
                    <tns:app_host>162.47.272.33</tns:app_host>
                    <tns:app_port>15001</tns:app_port>
                    <tns:app_url>/outbound/</tns:app_url>
                    <tns:message_id>1680361748</tns:message_id>
                    <!--Optional:-->
                    <tns:company_id>oss_sustentacao_wa_notdone</tns:company_id>
                    <!--Optional:-->
                    <tns:send_to>2023-09-05 20:43:47</tns:send_to>
                    <!--Optional:-->
                    <tns:subject>Atividade Não Concluída</tns:subject>
                    <tns:body>&lt;message xmlns:sme="http://www.gvt.com.br/ResourceManagement/WorkforceManagement/WorkOrderTrackingAndManagement/WorkOrderTracking/workOrderTrackingEntities"&gt;        
                        &lt;sme:type&gt;NOT_DONE&lt;/sme:type&gt;        
                        &lt;sme:workOrderItem&gt;                
                        &lt;sme:id&gt;5521766881:64483508&lt;/sme:id&gt;           
                        &lt;sme:workOrder&gt;                        
                        &lt;sme:id&gt;5521766881&lt;/sme:id&gt;       
                        &lt;/sme:workOrder&gt;                
                        &lt;sme:work&gt;                        
                        &lt;sme:id&gt;252807412&lt;/sme:id&gt;                        
                        &lt;sme:notDoneReason&gt;TUBULACAO INTERNA OBSTRUIDA&lt;/sme:notDoneReason&gt;                        
                        &lt;sme:endDate&gt;2024-05-13 13:28&lt;/sme:endDate&gt;              
                        &lt;sme:TimeZone&gt;-180&lt;/sme:TimeZone&gt;                 
                        &lt;sme:microArea&gt;Teresina Leste&lt;/sme:microArea&gt;             
                        &lt;sme:operationControllerNote&gt;&lt;![CDATA[13/05/2024 13:28:19	A0153531	TECNICO NAO CONSEGUIU FAZER TODA A PASSAGEM DA FIBRA, CONDOMINIO PRECISA COMPLETAR PASSAGEM. SEOERVISORA MARCELA CIENTE
13/05/2024 13:11:14	G0030464	Agendamento Controle NE- Simone Pedrosa\nEscalonado Coord. Elano ,ciente da  ordem iniciada período manhã
10/05/2024 10:23:12	A0153531	EM CONTATO COM CLIENTE 86981279412 NAO ACEITA ANTECIPAÇÃO, AGENDA MANTIDA. 
10/05/2024 08:26:33	G0030464	Agendamento Controle NE  Simone Pedrosa -INJECAO\nRealizado tentativas de contato no telefone 86981279412\ncaixa postal . Ação ferramenta \n]]&gt;&lt;/sme:operationControllerNote&gt;                        
                        &lt;sme:technicianNote&gt;&lt;![CDATA[]]&gt;&lt;/sme:technicianNote&gt;                        
                        &lt;sme:externalSystemsNote&gt;&lt;/sme:externalSystemsNote&gt;                        
                        &lt;sme:technician&gt;                                
                        &lt;sme:id&gt;80624758&lt;/sme:id&gt;                           
                        &lt;sme:identity&gt;&lt;/sme:identity&gt;                                
                        &lt;sme:name&gt;Francisco Adriel Araujo Soares&lt;/sme:name&gt;                         
                        &lt;sme:contractor&gt;&lt;/sme:contractor&gt;                                
                        &lt;sme:supervisor&gt;                                        
                        &lt;sme:id&gt;&lt;/sme:id&gt;                                        
                        &lt;sme:name&gt;&lt;/sme:name&gt;                                        
                        &lt;sme:contractor&gt;&lt;/sme:contractor&gt;                                        
                        &lt;sme:email&gt;&lt;/sme:email&gt;                                        
                        &lt;sme:mobilePhone&gt;&lt;/sme:mobilePhone&gt;                                
                        &lt;/sme:supervisor&gt;                        
                        &lt;/sme:technician&gt;                        
                        &lt;sme:customerContacted&gt;&lt;/sme:customerContacted&gt;                
                        &lt;/sme:work&gt;        
                        &lt;/sme:workOrderItem&gt;&lt;/message&gt;
                    </tns:body>
                </tns:message>
            </tns:messages>
        </send_message>
    </soapenv:Body>
</soapenv:Envelope>
"""

# Fazer a chamada SOAP
response = client.service.send_message(__inject={'msg': xml})

# Verificar a resposta
print(response)
