import requests
from bs4 import BeautifulSoup

def check_sites(sites):

    down_sites = []

    for site in sites:
        try:
            response = requests.get(site['url'])  # Use the 'url' from each site dict
            
            # Check if the status code is 200
            if response.status_code == 200:
                print(f"{site['name']} is up.")
            
            # If status code is 400, it's down
            elif response.status_code >= 400:
                print(f"{site['name']} is down.")
                down_sites.append(site)
            
            # If status code is 300, we need to check the content
            elif 300 <= response.status_code < 400:
                soup = BeautifulSoup(response.content, 'html.parser')
                images = soup.find_all('img', alt=True)  # Find all images with an alt attribute
                
                # Check if any image has 'error' in its alt text
                if any('error' in img['alt'].lower() for img in images):
                    print(f"{site['name']} might be up but showing a custom error image.")
                    down_sites.append(site)
                else:
                    print(f"{site['name']} is up with a redirection.")
                    
        except requests.exceptions.RequestException as e:
            # In case of a request exception (e.g., site not reachable), treat it as down
            print(f"{site['name']} is down due to an exception.")
            down_sites.append(site)

    return down_sites











# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
 
# # Encuentra los elementos que contienen noticias
# news_elements = soup.find_all('a', class_='headline-link')    
# # Acceder a los atributos
# #print(news_elements)
# # Lista para almacenar las URLs relevantes
# relevant_urls = []

# for news_element in news_elements:
#     print(type(news_element))
    
#     nombre_etiqueta = news_element.tag.attrs
#     print("Nombre de la etiqueta:", nombre_etiqueta)  # Imprime 'a'

#     atributos = news_element.tag.attrs
#     print("Atributos:", atributos)  # Imprime un diccionario con los atributos y sus valores

#     # Acceder a atributos específicos (como 'class', 'href', etc.)
#     clase = news_element.tag.get('class')
#     href = news_element.tag.get('href')
#     print("Clase:", clase)  # Imprime la lista de clases CSS si existen
#     print("Href:", href)    # Imprime el valor del atributo 'href'

#     # Acceder al contenido dentro de la etiqueta ('h2', texto, etc.)
#     contenido_etiqueta = news_element.tag.contents
#     print("Contenido de la etiqueta:", contenido_etiqueta)  # Imprime el contenido de la etiqueta (en este caso, h2)

#     # También puedes acceder a etiquetas anidadas (en este caso, h2) dentro de la etiqueta 'a'
#     etiqueta_h2 = news_element.tag.find('h2')
#     print("Etiqueta h2:", etiqueta_h2)  # Imprime la etiqueta h2 si está presente dentro de la etiqueta 'a'
 
#     title = news_element.get('h1')
#     content = news_element.find('p').text.strip()
#     article_url = news_element.find('a')['href']
 
#     # Verifica si alguna de las palabras clave está presente en el título o contenido
#     if any(keyword.lower() in title.lower() or keyword.lower() in content.lower() for keyword in keywords):
#         relevant_urls.append(article_url)
 
# # Imprime la lista de URLs relevantes
# print("URLs relevantes:")
# for url in relevant_urls:
#     print(url)