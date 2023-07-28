import pandas as pd
from sodapy import Socrata
from config import PSW_API, USUARI_API, API_GEN

                    ### NO AUTENTICAT ###
#client = Socrata("analisi.transparenciacatalunya.cat", None)

                     ### AUTENTICAT ###
client = Socrata("analisi.transparenciacatalunya.cat",
                 API_GEN,
                 username=USUARI_API,  # USUARI I CONTRASSENYA VOSTRES. REGISTRE: https://analisi.transparenciacatalunya.cat/login
                 password=PSW_API)

results = client.get("gn9e-3qhr", limit=9)  # EL "limit = 9" ENS DONA LES DADES DELS 9 EMBASSAMENTS EXACTES.

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df.head(10))