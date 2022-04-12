**Análise Exploratória de Dados da empresa Logística Loggi** 

Iremos analisar os dados da empresa de logística Loggi, na qual foram disponibilizados dados de entrega para o Distrito Federal.

Com base na extração de dados, iremos deduzir e curar informações a respeito das entregas efetuadas em 3 regiões: df-0, df-1 e df-2.

**Pacotes e bibliotecas**

Dados bruto em formato .json

![image](https://user-images.githubusercontent.com/101800412/163032618-30a35f9f-4177-4f2c-83ed-b8a0988dbf08.png)

Dados de geolocalização de entregas

![image](https://user-images.githubusercontent.com/101800412/163032721-8176d1b8-e2e4-45c5-afa7-3ff145fed1c5.png)

Dados extraídos do IBGE com mapa do Distrito Federal

![image](https://user-images.githubusercontent.com/101800412/163032919-eed27184-066a-47cd-b570-860f9f8fd340.png)

Pacote de instalação de geopandas para visualizar as coordenadas dos hubs e das entregas no mapa do Distrito Federal.

![image](https://user-images.githubusercontent.com/101800412/163032995-3dcc0f21-004a-4453-8329-eff1ff63f6f9.png)

**Processos de Exploração e Visualização por gráficos**

https://github.com/Vinicius-Arruda/Analise-Exploratoria-de-Dados-de-Logistica/blob/main/Analise%20Exploratoria%20de%20Dados%20de%20Logistica.ipynb

**Insights**

º Podemos visualizar que há uma grande concentração de serviços de entregas nas regiões df-1 e df-2, a ponto de terem até mesmo maior variedade de tipos de entregas em suas regiões.

º Com a materialização geográfica obtida com as coordenadas disponíveis, podemos assumir que o maior volume de entregas estão em polos mais próximos ao centro do Distrito Federal e menos entregas na zona de atendimento de df-0, que atende uma larga zona afastada do centro metropolitano, periferias e zonas rurais.
