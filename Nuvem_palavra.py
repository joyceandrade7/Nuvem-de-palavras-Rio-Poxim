# Importar bibliotecas necessárias
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# 📌 Novo texto fornecido
novo_texto = """
ESPAÇOS LIVRES (ELs) PÚBLICOS: COROA DO MEIO E O RIO POXIM EM ARACAJU/SE
O bairro Coroa do Meio encontra-se com uma elevada urbanização e o trecho referente ao rio Poxim sofre intensas ações antrópicas...
REPARTIÇÃO DA PRECIPITAÇÃO PLUVIAL EM UM FRAGMENTO DE MATA ATLÂNTICA NO TABULEIRO COSTEIRO DO NORDESTE BRASILEIRO
A análise da repartição da precipitação pluvial e sua interação com o ciclo hidrológico...
MAPEAMENTO E DIAGNÓSTICO DOS REMANESCENTES FLORESTAIS DA BACIA HIDROGRÁFICA DO RIO POXIM-SE
Os governos de diversos países têm somado esforços para combater o aquecimento global...
OS IMPACTOS SOCIOAMBIENTAIS NO BAIRRO JABOTIANA EM ARACAJU/SE: A LUDICIDADE ATRAVÉS DO TEATRO DE FANTOCHES
As discussões pedagógicas que buscam instigar nos discentes a curiosidade para a construção do conhecimento...
ÁREAS ALAGADAS QUE MARGEIAM O RIO POXIM: O CASO DO BAIRRO JABOTIANA, EM ARACAJU/SE
O objetivo deste capítulo é analisar as áreas alagadas no bairro Jabotiana...
ANÁLISE BIBLIOMÉTRICA DA PRODUÇÃO CIENTÍFICA SOBRE O RIO POXIM
Afetam o seu ecossistema e, para buscar soluções e melhorar tais problemas...
ANÁLISE DE SUSTENTABILIDADE HÍDRICA NO RIO POXIM
As alterações ambientais em virtude do crescimento desordenado na cidade de Aracaju...
"""

# 📌 Função para limpar o texto e preservar expressões compostas
def limpar_texto(texto):
    substituicoes = {
        "Mata Atlântica": "Mata_Atlântica",
        "instigar curiosidade": "Instigar_Curiosidade",
        "teatro de fantoches": "Teatro_Fantoches",
        "espaços livres públicos": "Espaços_Livres_Públicos",
        "tabuleiro costeiro": "Tabuleiro_Costeiro",
        "nordeste brasileiro": "Nordeste_Brasileiro",
        "ciclo hidrológico": "Ciclo_Hidrológico",
        "rio poxim": "Rio_Poxim",
        "coroa do meio": "Coroa_Do_Meio",
        "aracaju/se": "Aracaju"
    }
    
    for padrao, substituto in substituicoes.items():
        texto = re.sub(padrao, substituto, texto, flags=re.IGNORECASE)
    
    # Remover pontuação, números e caracteres especiais
    texto = re.sub(r"[^a-zA-Zà-úÀ-Ú_\s]", "", texto)
    
    return texto.lower()

# 📌 Lista de stopwords personalizadas
stopwords_personalizadas = {
    "e", "da", "de", "do", "em", "o", "a", "os", "as", "que", "para", "uma", "um",
    "é", "se", "foi", "dos", "das", "por", "no", "na", "como", "sua", "com", "mais",
    "ao", "às", "este", "isso", "pelo", "pelos", "elas", "eles", "também", "entre",
    "esperase", "deste", "notouse", "zero", "técnicas", "apresentado", "coroa", "b",
    "citados", "melhor", "análise", "capítulo", "pesquisa", "objetivo", "analisar",
    "dados", "produção", "referente", "uso", "gestão", "bairro", "têm", "caso", "seu", "sobre", 
    "somado", "buscam", "buscar", "tais", "nos", "elevada", "encontrase", "através", "discentes", 
    "diversos", "global", "margeiam", "repartição", "trecho", "virtude"
}

# 📌 Função para remover stopwords
def remover_stopwords(texto, stopwords):
    palavras = texto.split()
    return " ".join([palavra for palavra in palavras if palavra not in stopwords])

# 📌 Processar o texto
texto_limpo = limpar_texto(novo_texto)
texto_sem_stopwords = remover_stopwords(texto_limpo, stopwords_personalizadas)

# 📌 Gerar a nuvem de palavras com expressões compostas preservadas
wordcloud = WordCloud(
    width=3000,
    height=2000,
    background_color="white",
    colormap="coolwarm",  # Define a paleta de cores
    scale=2
).generate(texto_sem_stopwords)

# 📌 Exibir a nova nuvem de palavras
plt.figure(figsize=(15, 10), dpi=300)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Remove os eixos
plt.show()
