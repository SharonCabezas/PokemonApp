from PIL import Image
import random
from pathlib import Path
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.models import load_model
import requests
from streamlit_option_menu import option_menu
import os
import time
from tensorflow.keras.models import load_model
import plotly.express as px
import streamlit as st


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title='Pokedex', layout='wide')

st.image('pokemonlogo.png')

selected = option_menu(
    options=['Introducción', 'Identificador', 'Información', 'Estrategia', 'Entrenabilidad', 'iPokemon'],
    menu_title=None,
    icons=['book', 'search', 'bar-chart-line', 'bar-chart-steps', 'chat-heart', 'person'],
    menu_icon=None,
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red"},
    }
)

if selected == 'Introducción':
    st.markdown("<h1 style='text-align: center;'>Introducción</h1>", unsafe_allow_html=True)
    page_zz_img = """
    <style>
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        background-color: rgba(255, 255, 255, 0.9); /* Ajusta el valor alpha (0.0 - 1.0) para controlar la transparencia del fondo */
    }

    [data-testid="stAppViewContainer"] > .main {
        position: relative;
        width: auto;
        height: auto;
    }

    [data-testid="stAppViewContainer"] > .main::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://i.imgur.com/6R0Q1DU.jpeg');
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.2;
    }
    </style>
    """
    st.markdown(page_zz_img, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1.container():

        st.title('Descripción de la Base de Datos')
        st.write("¡Bienvenidos al universo de Pokémon! Este dataset contiene información sobre los 802 Pokémon de las siete generaciones. Desde estadísticas base hasta rendimiento contra otros tipos, altura, peso, clasificación y más. Se recopiló estos datos de http://serebii.net/, ¡donde la magia Pokémon cobra vida!Cada entrada revela joyas como nombres en inglés y japonés, número en la Pokédex, y porcentaje de género. Se pueden descubrir tipos primarios y secundarios, clasificación y datos curiosos como tasa de captura y pasos para eclosionar huevos. ¿Te preguntas cómo tu Pokémon favorito se defiende contra diferentes tipos de ataques? Tenemos la respuesta. ¡Atrapa la diversión y explora el mundo de Pokémon como nunca antes! La base de datos fue adquirida desde [Kaggle]('https://www.kaggle.com/datasets/rounakbanik/pokemon') 🌟📊🎮")
        pokemon = pd.read_csv('pokemon.csv')
        st.write(pokemon.head(12))

    with col2.container():
        lottie_pokeball = load_lottieurl('https://lottie.host/03f2eb09-e287-4e48-b782-09e81e949bce/TEPbLma2Jw.json')
        st_lottie(
          lottie_pokeball,
          speed = 1,
          reverse = False,
          loop = True,
          height = 800,
          width = 800,
        )

    agradecimiento_persona = {
            'Mensaje': 'Quiero agradecer a Damian Boh, un destacado científico de datos y desarrolador el cual compartió una herramienta de aprendizaje: ¡un Pokedex en Python! Este proyecto, disponible en su repositorio de GitHub [aquí](https://github.com/damianboh/pokedex), es una joya para aquellos que desean explorar y aprender. También extendemos nuestro agradecimiento a Gunjan Dhanuka, un apasionado investigador. Actualmente inmerso en el aprendizaje profundo, Gunjan ha compartido su conocimiento al desarrollar un modelo de machine learning para identificar Pokémones. Se puede explorar su proyecto y aprender cómo implementar el código en su repositorio de GitHub [aquí](https://github.com/GunjanDhanuka/PokeDex_Classifier/blob/master/PokemonClassifier.ipynb).👋🔍🤖'}

    st.markdown("""
        <style>
            .credits-section {
                background-color: #EDEDED;
                padding: 20px;
                margin-top: 30px;
                border-radius: 10px;
                overflow: hidden;
            }
            .credits-column {
                text-align: left;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: left; font-size: 30px;'>Agradecimientos</h2>", unsafe_allow_html=True)

    st.markdown("""
        <div class="credits-section">
            <div class="credits-column">
                <p>{}</p>
            </div>
        </div>
    """.format(agradecimiento_persona['Mensaje']), unsafe_allow_html=True)

if selected == 'Identificador':
    pokemon = pd.read_csv('pokemon.csv')
    page_zz_img = """
    <style>
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        background-color: rgba(255, 255, 255, 0.9); /* Ajusta el valor alpha (0.0 - 1.0) para controlar la transparencia del fondo */
    }

    [data-testid="stAppViewContainer"] > .main {
        position: relative;
        width: auto;
        height: auto;
    }

    [data-testid="stAppViewContainer"] > .main::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://i.imgur.com/6R0Q1DU.jpeg');
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.2;
    }
    </style>
    """
    st.markdown(page_zz_img, unsafe_allow_html=True)

    st.title("¿Quieres identificar un pokemón?")
    st.write('Imagina que estás explorando el emocionante universo de Pokémon y te encuentras con un Pokémon misterioso...que parece desafiar tu conocimiento.\n'
    '¡No te preocupes! Nuestro clasificador de Pokémon está listo para el desafío.\n'
    'Solo sube la foto del intrépido Pokémon y descubre quién se esconde detrás de esa mirada enigmática.\n'
    '¡La diversión y la emoción te esperan, así que descubre quién está listo para unirse a tu equipo!')

    class_names = ['Abra', 'Aerodactyl', 'Alakazam', 'Alolan Sandslash', 'Arbok', 'Arcanine', 'Articuno', 'Beedrill', 'Bellsprout', 'Blastoise', 'Bulbasaur', 'Butterfree', 'Caterpie', 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 'Clefable', 'Clefairy', 'Cloyster', 'Cubone', 'Dewgong', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 'Dragonair', 'Dragonite', 'Dratini', 'Drowzee', 'Dugtrio', 'Eevee', 'Ekans', 'Electabuzz', 'Electrode', 'Exeggcute', 'Exeggutor', 'Farfetchd', 'Fearow', 'Flareon', 'Gastly', 'Gengar', 'Geodude', 'Gloom', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Graveler', 'Grimer', 'Growlithe', 'Gyarados', 'Haunter', 'Hitmonchan', 'Hitmonlee', 'Horsea', 'Hypno', 'Ivysaur', 'Jigglypuff', 'Jolteon', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan', 'Kingler', 'Koffing', 'Krabby', 'Lapras', 'Lickitung', 'Machamp', 'Machoke', 'Machop', 'Magikarp', 'Magmar', 'Magnemite', 'Magneton', 'Mankey', 'Marowak', 'Meowth', 'Metapod', 'Mew', 'Mewtwo', 'Moltres', 'MrMime', 'Muk', 'Nidoking', 'Nidoqueen', 'Nidorina', 'Nidorino', 'Ninetales', 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Paras', 'Parasect', 'Persian', 'Pidgeot', 'Pidgeotto', 'Pidgey', 'Pikachu', 'Pinsir', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Porygon', 'Primeape', 'Psyduck', 'Raichu', 'Rapidash', 'Raticate', 'Rattata', 'Rhydon', 'Rhyhorn', 'Sandshrew', 'Sandslash', 'Scyther', 'Seadra', 'Seaking', 'Seel', 'Shellder', 'Slowbro', 'Slowpoke', 'Snorlax', 'Spearow', 'Squirtle', 'Starmie', 'Staryu', 'Tangela', 'Tauros', 'Tentacool', 'Tentacruel', 'Vaporeon', 'Venomoth', 'Venonat', 'Venusaur', 'Victreebel', 'Vileplume', 'Voltorb', 'Vulpix', 'Wartortle', 'Weedle', 'Weepinbell', 'Weezing', 'Wigglytuff', 'Zapdos', 'Zubat']

    def main():
        file_uploaded = st.file_uploader("Seleccione una imagen", type=["png", "jpg", "jpeg"])
        class_btn = st.button("Clasificar")
        if file_uploaded is not None:
            image = Image.open(file_uploaded)
            st.image(image, caption='¡Imagen subida!', use_column_width=True)

        if class_btn:
            if file_uploaded is None:
                st.warning("Invalido, suba un archivo en el formato adecuado.")
            else:
                with st.spinner('Model working....'):
                    predictions = predict(image)
                    time.sleep(1)
                    st.success('El pokemón fue clasificado correctamente.')
                    print_data(predictions)

    def path_to_image_html(path):
        return '<img src="'+ path + '" width="60" >'

    def predict(image):
        classifier_model = "model_pokemon (1).h5"
        IMAGE_SHAPE = (128, 128, 3)
        model = load_model(classifier_model)
        test_image = image.convert("RGB").resize((128, 128))
        test_image = np.array(test_image)
        test_image = test_image / 255.0
        img_array = tf.expand_dims(test_image, 0)

        predictions = model.predict(img_array)
        scores = tf.nn.softmax(predictions[0])
        scores = scores.numpy()
        highest = scores.argsort()[-5:][::-1]
        result = []
        for i in range(5):
            result += f"{class_names[highest[i]]} with a { (100 * scores[highest[i]]).round(2) } % confidence."
            result += '\n'
            result.append(class_names[highest[i]])
            i += 1

        return result

    def print_data(pokelist):
        url = 'https://pokeapi.co/api/v2/pokemon/'
        df = pd.DataFrame(data=np.zeros((5, 4)),
                          columns=['Nombre',  'Tipo', 'Descripción', 'Image'],
                          index=np.linspace(1, 5, 5, dtype=int)
                          )
        i = 0
        sprites_path = 'https://github.com/GunjanDhanuka/PokeDex_Classifier/blob/master/sprites/'
        sprites = []
        for poke in pokelist:
            response = requests.get(url+poke.lower())
            if(response.status_code != 200):

                df.iloc[i, 0] = poke
                df.iloc[i, 1] = 'Error fetching data from API'
                df.iloc[i, 2] = 'Error fetching data from API'
                sprites.append(sprites_path+'0.png?raw=true')

            else:
                jresponse = response.json()
                type = jresponse['types'][0]['type']['name']
                id = jresponse['id']
                species_url = jresponse['species']['url']
                species_response = requests.get(species_url)
                species_response = species_response.json()
                description = ''
                for d in species_response['flavor_text_entries']:
                    if d['language']['name'] == 'en':
                        description = d['flavor_text']
                        break
                df.iloc[i, 0] = poke.capitalize()
                df.iloc[i, 1] = type.capitalize()
                description = description.replace('\n', ' ')
                description = description.replace(' ', ' ')
                df.iloc[i, 2] = description
                sprites.append(sprites_path+str(id)+'.png?raw=true')

            i += 1
        df['Image'] = sprites
        st.title("¡Estos son los cinco Pokémon más probables!")
        st.caption("en orden decreciente de confianza..")
        st.write(df.to_html(escape=False, formatters=dict(Image=path_to_image_html)), unsafe_allow_html=True)

    if __name__ == "__main__":
        main()


if selected == 'Información':

    def get_image_path(pokemon_number):
        image_folder_path = '/content/drive/MyDrive/pokemon_images/'
        return f'{image_folder_path}{pokemon_number}.png'

    page_zz_img = """
    <style>
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        background-color: rgba(255, 255, 255, 0.9);
    }

    [data-testid="stAppViewContainer"] > .main {
        position: relative;
        width: auto;
        height: auto;
    }

    [data-testid="stAppViewContainer"] > .main::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://i.imgur.com/6R0Q1DU.jpeg');
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.2;
    }
    </style>
    """
    st.markdown(page_zz_img, unsafe_allow_html=True)

    sidebar_bg_url = "https://wallpapers.com/images/hd/awesome-pokeball-cover-yr2d9wxouqfbvcol.jpg"

    sidebar_custom_style = f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: url('{sidebar_bg_url}');
        background-size: cover;
        background-position: down;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(sidebar_custom_style, unsafe_allow_html=True)

    pokemon = pd.read_csv('pokemon.csv')
    columna_cambiar = 'is_legendary'
    pokemon[columna_cambiar].replace(0, "No", inplace=True)
    pokemon[columna_cambiar].replace(1, "Si", inplace=True)

    st.title("Información de Pokémon")
    st.write('¡Hey Entrenador! ¿Te has preguntado alguna vez cómo sería ser un maestro Pokémon? 🌟\n'
         '¡Ahora es tu momento! Ingresa las iniciales del Pokémon en el sidebar si no conoces su nombre completo.\n'
         '¡Verás cómo aparecen mágicamente en el select box! 🚀 Y si ya eres un experto y conoces el nombre...\n'
         'búscalo en el select box para descubrir toda la información sobre ese asombroso Pokémon.\n'
         '¡Atrévete a ser el mejor maestro Pokémon! 🎉')

    st.sidebar.header('Controles')

    ingresado = st.sidebar.text_input('Ingresar nombre del Pokémon:', '').lower()

    if 'name' in pokemon.columns:
      matches = pokemon[pokemon['name'].str.lower().str.startswith(ingresado)]
      if not matches.empty:
          opciones_pokemon = matches['name'].tolist()
          seleccion = st.sidebar.selectbox("Selecciona un Pokémon:", opciones_pokemon)

          # Verificar si la opción seleccionada está en la columna 'name'
          if seleccion in pokemon['name'].values:

              # Obtener información del Pokémon seleccionado
              pokemon_seleccionado = pokemon[pokemon['name'] == seleccion].iloc[0]
              name = pokemon_seleccionado['name']
              altura = str(pokemon_seleccionado['height_m'])
              peso = str(pokemon_seleccionado['weight_kg'])
              especie = ' '.join(pokemon_seleccionado['classfication'].split(' ')[:-1])
              tipo1 = pokemon_seleccionado['type1']
              tipo2 = pokemon_seleccionado['type2']
              generacion = pokemon_seleccionado['generation']
              legendario = pokemon_seleccionado['is_legendary']

              st.subheader(name)

              col1, col2, col3 = st.columns(3)

              with col2.container():
                  col2.metric('Tipo', tipo1, tipo2)
                  col2.metric("Altura", altura + " m")
                  col2.metric("Peso", peso + " kg")

              with col3.container():
                  col3.metric('Especie', especie)
                  col3.metric('Generación', generacion)
                  col3.metric('Legendario', legendario)

              try:
                  # Obtener el número de la Pokédex del Pokémon seleccionado
                  pokedex_number = pokemon_seleccionado['pokedex_number']

                  # Obtener la ruta de la imagen en Google Drive
                  path = get_image_path(pokedex_number)

                  # Imprimir la ruta de la imagen (opcional, para verificar)
                  print("Ruta de la imagen:", path)

                  # Abrir la imagen y mostrarla en la columna col1
                  image = Image.open(path)
                  col1.image(image, caption=f'Imagen del Pokémon {seleccion}')
              except:
                  col1.write('No existe la imagen.')

    st.title("Información General")

    st.write('🌟 Te has preguntado cuántos Pokémon hay de ciertos tipos principales y secundarios?\n'
     '¡Pues estás a punto de descubrirlo de la manera más divertida posible!\n'
      '¿Cuántos Pokémon tipo Fuego 🔥 y Agua 💧 hay?No te preocupes, no necesitas una Pokédex para esto.\n'
      'Solo desliza tu mouse hacia nuestro sidebar y elige tus opciones favoritas.\n'
      '¿Quieres todos los Pokémon tipo Planta? ¡Claro, lo tenemos! ¿O prefieres algo más exótico, como Pokémon tipo Psíquico?\n'
      '¡No hay problema, estamos aquí para satisfacer tus necesidades Pokémonicas más específicas! 🌿🔮')

    tipo1 = [
          "water",
          "normal",
          "grass",
          "bug",
          "psychic",
          "fire",
          "rock",
          "electric",
          "poison",
          "ground",
          "dark",
          "fighting",
          "ghost",
          "dragon",
          "steel",
          "ice",
          "fairy",
          "flying"
    ]

    tipo2 = [
          "flying",
          "poison",
          "ground",
          "fairy",
          "psychic",
          "fighting",
          "steel",
          "dark",
          "grass",
          "water",
          "dragon",
          "ice",
          "rock",
          "ghost",
          "fire",
          "electric",
          "bug",
          "normal"
    ]

    tipo1_seleccionado = st.sidebar.multiselect("Selecciona el tipo principal:", tipo1, key="multi_tipo1")

    tipo2_seleccionado = st.sidebar.multiselect("Selecciona el tipo secundario:", tipo2, key="multi_tipo2")

    tipo1_barra = pokemon[pokemon['type1'].isin(tipo1_seleccionado)]
    tipo2_barra = pokemon[pokemon['type2'].isin(tipo2_seleccionado)]

    col1, col2 = st.columns(2)



    contados_tipo1 = tipo1_barra['type1'].value_counts().reset_index()
    contados_tipo1.columns = ['Tipo', 'Cantidad']
    fig_tipo1 = px.bar(contados_tipo1, x='Tipo', y='Cantidad', title=f'Pokémon por Tipo 1', color_discrete_sequence=['#3365A6'])
    col1.plotly_chart(fig_tipo1)



    contados_tipo2 = tipo2_barra['type2'].value_counts().reset_index()
    contados_tipo2.columns = ['Tipo', 'Cantidad']
    fig_tipo2 = px.bar(contados_tipo2, x='Tipo', y='Cantidad', title=f'Pokémon por Tipo 2', color_discrete_sequence=['#3365A6'])
    col2.plotly_chart(fig_tipo2)


    st.write('¿Quieres descubrir las especies Pokémon más populares? ¡Es fácil! Solo elige cuántas especies quieres en tu top: 3, 5 o 7.\n'
    'A continuación, podrás explorar el gráfico de pastel para conocer las especies más destacadas. ¡Haz tu selección y disfruta!\n'
    '¡Conviértete en un maestro Pokémon experto con solo un par de clics! 🚀')

    cantidad_especies = st.sidebar.selectbox("Selecciona el número del top de especies que desea ver:", [3, 5, 7])

    conteo = pokemon['classfication'].value_counts().head(cantidad_especies)
    conteo1 = pokemon['classfication'].value_counts().head(cantidad_especies).index
    fig_top = px.pie(conteo, names=conteo1, values=conteo, color_discrete_sequence=['#3365A6', '#BF212E', '#F2B90C'])
    fig_top.update_traces(textposition='inside', textinfo='percent+label')
    fig_top.update_layout(title=f'Top especies pokemón', width=800, height=600)

    st.plotly_chart(fig_top, use_container_width=True)

    st.write('Explora la diversidad de tipos de Pokémon en cada generación. Selecciona una generación en el sunburst y descubre cuántos Pokémon hay por cada tipo en esa generación.\n'
    'El gráfico Sunburst te proporcionará una visión interactiva y colorida de la distribución de tipos')

    resultado_groupby = pokemon.groupby(['generation', 'type1'])['type1'].count().reset_index(name='conteo')

    resultado = pd.DataFrame(resultado_groupby)

    fig_gen = px.sunburst(resultado, path=['generation', 'type1'], values='conteo', color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])
    fig_gen.update_layout(title=f'Distribución por Generación y Tipo 1', width=800, height=600)


    st.plotly_chart(fig_gen, use_container_width=True)

if selected == 'Estrategia':
    pokemon = pd.read_csv('pokemon.csv')
    page_zz_img = """
    <style>
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        background-color: rgba(255, 255, 255, 0.9); /* Ajusta el valor alpha (0.0 - 1.0) para controlar la transparencia del fondo */
    }

    [data-testid="stAppViewContainer"] > .main {
        position: relative;
        width: auto;
        height: auto;
    }

    [data-testid="stAppViewContainer"] > .main::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://i.imgur.com/6R0Q1DU.jpeg');
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.2;
    }
    </style>
    """
    st.markdown(page_zz_img, unsafe_allow_html=True)

    sidebar_bg_url = "https://wallpapers.com/images/hd/awesome-pokeball-cover-yr2d9wxouqfbvcol.jpg"

    sidebar_custom_style = f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: url('{sidebar_bg_url}');
        background-size: cover;
        background-position: down;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(sidebar_custom_style, unsafe_allow_html=True)

    pokemon = pd.read_csv('pokemon.csv')

    def get_image_path(pokemon_number):
        image_folder_path = '/content/drive/MyDrive/pokemon_images/'
        return f'{image_folder_path}{pokemon_number}.png'

    st.title("Análisis de Batalla")

    st.sidebar.header('Controles')

    ingresado = st.sidebar.text_input('Ingresar nombre del Pokémon:', '').lower()

    if 'name' in pokemon.columns:
      matches = pokemon[pokemon['name'].str.lower().str.startswith(ingresado)]
      if not matches.empty:
          opciones_pokemon = matches['name'].tolist()
          seleccion = st.sidebar.selectbox("Selecciona un Pokémon:", opciones_pokemon)

          if seleccion in pokemon['name'].values:

              pokemon_seleccionado = pokemon[pokemon['name'] == seleccion].iloc[0]
              name = pokemon_seleccionado['name']
              st.subheader(name)

              col1, col2, col3 = st.columns(3)

              with col2.container():
                  velocidad = pokemon_seleccionado['speed']
                  sp_ataque = pokemon_seleccionado['sp_attack']
                  sp_defensa = pokemon_seleccionado['sp_defense']
                  HP = pokemon_seleccionado['hp']
                  defensa = pokemon_seleccionado['defense']
                  ataque = pokemon_seleccionado['attack']

                  stats_data = {
                  'Stats': ['Velocidad', 'Ataque Especial', 'Defensa Especial', 'HP', 'Defensa', 'Ataque'],
                  'Valor': [velocidad, sp_ataque, sp_defensa, HP, defensa, ataque]
                  }

                  pokemon_stats = pd.DataFrame(stats_data)

                  fig_stats = px.bar(pokemon_stats, x='Valor', y='Stats', orientation='h', labels={'Valor': 'Valor de la Estadística'},  color_discrete_sequence=['#3365A6'])

                  fig_stats.update_layout(title=f'Estadísticas de Batalla de {name}', xaxis_title='Valor', yaxis_title='Estadística')

                  # Mostrar el gráfico
                  col2.plotly_chart(fig_stats,use_container_width=True)

              with col3.container():

                a_bug = pokemon_seleccionado['against_bug']
                a_dark = pokemon_seleccionado['against_dark']
                a_dragon = pokemon_seleccionado['against_dragon']
                a_electric = pokemon_seleccionado['against_electric']
                a_fairy = pokemon_seleccionado['against_fairy']
                a_fight = pokemon_seleccionado['against_fight']
                a_fire = pokemon_seleccionado['against_fire']
                a_flying = pokemon_seleccionado['against_flying']
                a_ghost = pokemon_seleccionado['against_ghost']
                a_grass = pokemon_seleccionado['against_grass']
                a_ground = pokemon_seleccionado['against_ground']
                a_ice = pokemon_seleccionado['against_ice']
                a_normal = pokemon_seleccionado['against_normal']
                a_poison = pokemon_seleccionado['against_poison']
                a_psychic = pokemon_seleccionado['against_psychic']
                a_rock = pokemon_seleccionado['against_rock']
                a_steel = pokemon_seleccionado['against_steel']
                a_water = pokemon_seleccionado['against_water']

                weekness_data = {
                'Debilidades': ['Insecto', 'Oscuro', 'Dragon', 'Eléctrico', 'Hada', 'Peleador','Fuego', 'Volador','Fantasma','Hierba','Tierra','Hielo','Normal','Venenoso','Psíquico','Roca','Acero','Agua'],
                'Valor': [a_bug, a_dark, a_dragon, a_electric, a_fairy, a_fight,a_fire,a_flying,a_ghost,a_grass,a_ground,a_ice,a_normal,a_poison,a_psychic,a_rock,a_steel,a_water]
                }

                pokemon_weekness = pd.DataFrame(weekness_data)

                fig_weekness = px.bar(pokemon_weekness, x='Valor', y='Debilidades', orientation='h', labels={'Valor': 'Valor de la debilidad'},  color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

                fig_weekness.update_layout(title=f'Débilidades en Batalla de {name}', xaxis_title='Valor', yaxis_title='Debilidades')


                st.plotly_chart(fig_weekness, use_container_width=True)

              try:
                    pokedex_number = pokemon_seleccionado['pokedex_number']

                    path = get_image_path(pokedex_number)

                    image = Image.open(path)
                    col1.image(image, caption=f'Imagen del Pokémon {seleccion}')
              except:
                    col1.write('No existe la imagen.')

    selected = option_menu(
        options=['Búsqueda Personalizada', 'Análisis General'],
        menu_title=None,
        icons=['search', 'bar-chart-line'],
        menu_icon=None,
        default_index=0,
        orientation='horizontal',
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "red"},
        }
    )

    if selected == 'Búsqueda Personalizada':

      st.title('¿Quieres encontrar un Pokémon por sus Estadísticas de Batalla?')
      st.subheader('Selecciona las estadísticas con las cuales quieres filtrar:')

      col1, col2 = st.columns(2)

      with st.form(key='my_form'):
        with col1:

            min_speed, max_speed = st.slider('speed', min_value=0, max_value=250, value=[0, 250])
            min_sp_def, max_sp_def = st.slider('sp_defense', min_value=0, max_value=250, value=[0, 250])
            min_sp_atk, max_sp_atk = st.slider('sp_attack', min_value=0, max_value=250, value=[0, 250])
            min_def, max_def = st.slider('defense', min_value=0, max_value=250, value=[0, 250])
            min_atk, max_atk = st.slider('attack', min_value=0, max_value=250, value=[0, 250])
            min_hp, max_hp = st.slider('hp', min_value=0, max_value=250, value=[0, 250])


        with col2:
            # Filtrar el DataFrame usando los valores seleccionados
            filtered_data = pokemon[
            (pokemon['speed'] >= min_speed) & (pokemon['speed'] <= max_speed) &
            (pokemon['sp_defense'] >= min_sp_def) & (pokemon['sp_defense'] <= max_sp_def) &
            (pokemon['sp_attack'] >= min_sp_atk) & (pokemon['sp_attack'] <= max_sp_atk) &
            (pokemon['defense'] >= min_def) & (pokemon['defense'] <= max_def) &
            (pokemon['attack'] >= min_atk) & (pokemon['attack'] <= max_atk) &
            (pokemon['hp'] >= min_hp) & (pokemon['hp'] <= max_hp)
            ]

            columnas = ['name', 'speed', 'sp_attack', 'sp_defense', 'hp', 'defense', 'attack']

            st.table(filtered_data[columnas])

    if selected == 'Análisis General':

      st.title('Estadísticas Generales de Batalla')

      col1, col2 = st.columns(2)

      top_n = st.sidebar.selectbox("Selecciona el top N:", [3, 5, 7, 10])

      with col1.container():

        top_speed = pokemon.nlargest(top_n, 'speed')

        fig_speed = px.bar(top_speed, x='speed', y='name', orientation='h', text='speed',
                    labels={'speed': 'Velocidad', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones más veloces',color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col1.plotly_chart(fig_speed, use_container_width=True)


        top_atackk = pokemon.nlargest(top_n, 'attack')

        fig_attack= px.bar(top_atackk, x='attack', y='name', orientation='h', text='attack',
                    labels={'attack': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con mayor ataque',color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col1.plotly_chart(fig_attack, use_container_width=True)


        top_defense = pokemon.nlargest(top_n, 'defense')

        fig_defense= px.bar(top_defense, x='defense', y='name', orientation='h', text='attack',
                    labels={'defense': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con mayor defensa',color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col1.plotly_chart(fig_defense, use_container_width=True)

        top_sdefense = pokemon.nlargest(top_n, 'sp_defense')

        fig_sdefense= px.bar(top_sdefense, x='sp_defense', y='name', orientation='h', text='sp_defense',
                    labels={'sp_defense': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con mayor defensa especial',color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col1.plotly_chart(fig_sdefense, use_container_width=True)

        top_sattack = pokemon.nlargest(top_n, 'sp_attack')

        fig_sattack= px.bar(top_sattack, x='sp_attack', y='name', orientation='h', text='sp_attack',
                    labels={'sp_attack': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con mayor ataque especial',color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col1.plotly_chart(fig_sattack, use_container_width=True)


      with col2.container():

        top_speed = pokemon.nsmallest(top_n, 'speed')

        fig_speed = px.bar(top_speed, x='speed', y='name', orientation='h', text='speed',
                    labels={'speed': 'Velocidad', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones menos veloces',color_discrete_sequence=['#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col2.plotly_chart(fig_speed, use_container_width=True)


        top_atackk = pokemon.nsmallest(top_n, 'attack')

        fig_attack= px.bar(top_atackk, x='attack', y='name', orientation='h', text='attack',
                    labels={'attack': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con menor ataque',color_discrete_sequence=['#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col2.plotly_chart(fig_attack, use_container_width=True)


        top_defense = pokemon.nsmallest(top_n, 'defense')

        fig_defense= px.bar(top_defense, x='defense', y='name', orientation='h', text='attack',
                    labels={'defense': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con menor defensa',color_discrete_sequence=['#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col2.plotly_chart(fig_defense, use_container_width=True)

        top_sdefense = pokemon.nsmallest(top_n, 'sp_defense')

        fig_sdefense= px.bar(top_sdefense, x='sp_defense', y='name', orientation='h', text='sp_defense',
                    labels={'sp_defense': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con menor defensa especial',color_discrete_sequence=['#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col2.plotly_chart(fig_sdefense, use_container_width=True)

        top_sattack = pokemon.nsmallest(top_n, 'sp_attack')

        fig_sattack= px.bar(top_sattack, x='sp_attack', y='name', orientation='h', text='sp_attack',
                    labels={'sp_attack': 'Ataque', 'name': 'Pokemón'},
                    title=f'Top {top_n} Pokemones con menor ataque especial',color_discrete_sequence=['#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

        col2.plotly_chart(fig_sattack, use_container_width=True)



if selected == 'Entrenabilidad':
    pokemon = pd.read_csv('pokemon.csv')
    page_zz_img = """
    <style>
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        background-color: rgba(255, 255, 255, 0.9); /* Ajusta el valor alpha (0.0 - 1.0) para controlar la transparencia del fondo */
    }

    [data-testid="stAppViewContainer"] > .main {
        position: relative;
        width: auto;
        height: auto;
    }

    [data-testid="stAppViewContainer"] > .main::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://i.imgur.com/6R0Q1DU.jpeg');
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.2;
    }
    </style>
    """
    st.markdown(page_zz_img, unsafe_allow_html=True)

    sidebar_bg_url = "https://wallpapers.com/images/hd/awesome-pokeball-cover-yr2d9wxouqfbvcol.jpg"

    sidebar_custom_style = f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: url('{sidebar_bg_url}');
        background-size: cover;
        background-position: down;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(sidebar_custom_style, unsafe_allow_html=True)

    pokemon = pd.read_csv('pokemon.csv')

    st.title("Perfil de Entrenabilidad")

    def get_image_path(pokemon_number):
      image_folder_path = '/content/drive/MyDrive/pokemon_images/'
      return f'{image_folder_path}{pokemon_number}.png'

    st.sidebar.header('Controles')

    ingresado = st.sidebar.text_input('Ingresar nombre del Pokémon:', '').lower()

    if 'name' in pokemon.columns:
      matches = pokemon[pokemon['name'].str.lower().str.startswith(ingresado)]
      if not matches.empty:
          opciones_pokemon = matches['name'].tolist()
          seleccion = st.sidebar.selectbox("Selecciona un Pokémon:", opciones_pokemon)

          if seleccion in pokemon['name'].values:

              pokemon_seleccionado = pokemon[pokemon['name'] == seleccion].iloc[0]
              name = pokemon_seleccionado['name']
              felicidad = str(pokemon_seleccionado['base_happiness'])
              crecimiento = pokemon_seleccionado['experience_growth']
              captura = pokemon_seleccionado['capture_rate']
              pasos_base_huevo = pokemon_seleccionado['base_egg_steps']

              st.subheader(name)

              col1, col2, col3 = st.columns(3)

              with col2.container():
                  col2.metric('Felicidad Base', felicidad)
                  col2.metric("Tasa de Captura", captura)

              with col3.container():
                  col3.metric('Pasos Base de Huevo', pasos_base_huevo)
                  col3.metric('Crecimiento de Experiencia', crecimiento)

              try:
                  pokedex_number = pokemon_seleccionado['pokedex_number']

                  path = get_image_path(pokedex_number)

                  print("Ruta de la imagen:", path)

                  image = Image.open(path)
                  col1.image(image, caption=f'Imagen del Pokémon {seleccion}')
              except:
                  col1.write('No existe la imagen.')


    st.title('Estadíasticas Generales de Entrenabilidad')

    col1, col2 = st.columns(2)

    with col1.container():
        top_felicidad = st.sidebar.selectbox("Selecciona el número del top de felicidad base que deseas ver:", [3, 5, 7])

        felicidad_por_tipo = pokemon.groupby('type1')['base_happiness'].sum()

        top_tipos_felicidad = felicidad_por_tipo.nlargest(top_felicidad).index

        pokemon_top_felicidad = pokemon[pokemon['type1'].isin(top_tipos_felicidad)]

        conteo = pokemon_top_felicidad['type1'].value_counts(1)

        fig_top = px.pie(conteo, names=conteo.index, values=conteo, color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])
        fig_top.update_traces(textposition='inside', textinfo='percent+label')
        fig_top.update_layout(title=f'Top {top_felicidad} tipos de Pokémon más felices', width=800, height=600)

        st.plotly_chart(fig_top,use_container_width=True)


    with col2.container():

        top_deseado = st.sidebar.selectbox("Selecciona el tamaño del top:", [5, 15, 30])

        pokemon['capture_rate'] = pd.to_numeric(pokemon['capture_rate'], errors='coerce')

        top_capturas = pokemon.nlargest(top_deseado, 'capture_rate')

        st.write(f"**Top {top_deseado} Pokémon con las tasas de captura más altas:**")

        st.write(top_capturas[['name', 'capture_rate','pokedex_number','type1','is_legendary']])

        pokemon['capture_rate'] = pd.to_numeric(pokemon['capture_rate'], errors='coerce')

        top_capturas = pokemon.nsmallest(top_deseado, 'capture_rate')

        st.write(f"**Top {top_deseado} Pokémon con las tasas de captura más bajas:**")

        st.write(top_capturas[['name', 'capture_rate','pokedex_number','type1','is_legendary']])


    st.title('Exploración de los Pasos para la Eclosión de los tipo de Pokémon')

    grupo1 = pokemon.groupby(['base_egg_steps', 'type1', 'generation']).size().reset_index(name='conteo')

    resultado = pd.DataFrame(grupo1)

    fig_sun = px.sunburst(resultado, path=['generation', 'type1', 'base_egg_steps'], values='conteo',color_discrete_sequence=['#BF212E', '#3365A6', '#F2B90C','#BF920B', '#FF7609','#7DA2E1', '#F20505'])

    st.plotly_chart(fig_sun,use_container_width=True)


if selected == 'iPokemon':
    pokemon = pd.read_csv('pokemon.csv')

    page_zz_img = """
    <style>
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        background-color: rgba(255, 255, 255, 0.2);
    }
    </style>
    """
    st.markdown(page_zz_img, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1.container():
      st.title("¿Quieres saber qué Pokémon eres?")
      st.write('Responde las preguntas a continuación y descubre que pokemon eres.🤩✨')

      pregunta1 = st.selectbox("Pregunta 1: ¿Qué te gusta más?", ['Playa', 'Naturaleza', 'Ciudad', 'Nieve'])

      if pregunta1 == 'Playa':
          pokemon = pokemon[pokemon['type1'] == 'fire']
      if pregunta1 == 'Naturaleza':
          pokemon = pokemon[pokemon['type1'] == 'grass']
      if pregunta1 == 'Ciudad':
          pokemon = pokemon[pokemon['type1'] == 'normal']
      if pregunta1 == 'Nieve':
          pokemon = pokemon[pokemon['type1'] == 'ice']

      pregunta2 = st.selectbox("Pregunta 2: ¿Hablas antes de pensar o piensas antes de hablar?", ['Hablo antes', 'Pienso antes'])

      if pregunta2 == 'Hablo antes':
          min_attack = 100
          max_attack = 180
      if pregunta2 == 'Pienso antes':
          max_attack = 100
          min_attack = 50

      pokemon_filtrado = pokemon[(pokemon['attack'] >= min_attack) & (pokemon['attack'] <= max_attack)]

      pregunta3 = st.selectbox("Pregunta 3: ¿Eres veloz?", ['Sí', 'No', 'Medio'])

      if pregunta3 == 'Sí':
          min_speed = 100
          max_speed = 180
      if pregunta3 == 'No':
          min_speed = 0
          max_speed = 50
      if pregunta3 == 'Medio':
          min_speed = 50
          max_speed = 100

      pokemon_filtrado = pokemon[(pokemon['speed'] >= min_speed) & (pokemon['speed'] <= max_speed)]

      pregunta4 = st.selectbox("Pregunta 4: ¿Qué generación eres?", ['Milenial', 'Z', 'Boomer', 'Alfa'])

      if pregunta4 == 'Milenial':
          pokemon_filtrado = pokemon[(pokemon['generation'] == 1) | (pokemon['generation'] == 2) | (pokemon['generation'] == 3)]
      if pregunta4 == 'Z':
          pokemon_filtrado = pokemon[(pokemon['generation'] == 3) | (pokemon['generation'] == 4) | (pokemon['generation'] == 5)]
      if pregunta4 == 'Boomer':
          pokemon_filtrado = pokemon[(pokemon['generation'] == 5) | (pokemon['generation'] == 6) | (pokemon['generation'] == 7)]
      if pregunta4 == 'Alfa':
          pokemon_filtrado = pokemon[(pokemon['generation'] == 1) | (pokemon['generation'] == 2)]

      pregunta5 = st.selectbox("Pregunta 5: ¿Prefieres aparecer en una leyenda mítica o en un periódico famoso a nivel mundial?", ['Leyenda', 'Periódico'])

      if pregunta5 == 'Leyenda':
          pokemon_filtrado = pokemon[pokemon['is_legendary'] == 1]
      if pregunta5 == 'Periódico':
          pokemon_filtrado = pokemon[pokemon['is_legendary'] == 0]

      boton_mostrar_tabla = st.button("¿Quién soy?")

      if boton_mostrar_tabla:
          columnas_mostrar = ['name', 'type1', 'generation', 'is_legendary', 'abilities','attack','defense','classfication','height_m','hp','weight_kg','japanese_name']
          resultado_final = pokemon_filtrado[columnas_mostrar]

          if not resultado_final.empty:
              fila_aleatoria = resultado_final.sample()
              st.write("Eres....")
              st.table(fila_aleatoria)
              st.success('¡Felicidades! Te recomendamos revisar sus características para conocerlo mejor.')
          else:
              st.write("Eres único, no existe ningún pokemón que te represente.")

    with col2.container():
      lottie_pokemon_2 = load_lottieurl('https://lottie.host/cd7f9772-4dce-4dc6-b2f7-6a26c366903f/BTTnDxgUAJ.json')
      st_lottie(
          lottie_pokemon_2,
          speed=1,
          reverse=False,
          loop=True,
          quality='high',
          height=800,
          width=800,
          key=None,
      )
