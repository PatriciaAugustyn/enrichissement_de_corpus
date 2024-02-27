import spacy


nlp = spacy.load("fr_core_news_sm")

# Charger le contenu du fichier
with open("bonheur.txt", 'r') as fichier:
    test = fichier.read()

def return_token(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc]

def return_token_sent(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc.sents]

def return_POS(sentence):
    doc = nlp(sentence)
    return [(X.text, X.pos_) for X in doc]

# Récupérer les résultats
tokens = return_token(test)
sentences = return_token_sent(test)
pos_tags = return_POS(test)

# Enregistrer les résultats dans un fichier texte
with open("resultat_spacy_bonheur.txt", 'w') as resultat_fichier:

    resultat_fichier.write("\nEtiquetage morpho-syntaxique:\n")
    resultat_fichier.write("\t".join(["#", "Token", "POS"]) + "\n")
    for i, (token, pos) in enumerate(pos_tags):
        resultat_fichier.write(f"\t{i+1}\t{token}\t{pos}\n")

print("Les résultats ont été enregistrés dans le fichier 'resultat_spacy_bonheur.txt'.")







